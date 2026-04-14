#!/usr/bin/env python3
"""
ingest-youtube.py - Fetch YouTube transcripts into active_sources/youtube/

Usage:
    python scripts/ingest-youtube.py --video <url>
    python scripts/ingest-youtube.py --channel <url-or-handle>
    python scripts/ingest-youtube.py --from-queue

Output:
    active_sources/youtube/<channel>/<video-id>/
        transcript.txt   # plain text transcript (auto-captions if available)
        meta.json        # title, channel, upload_date, duration, url, tags

Required external tool:
    yt-dlp (install: pip install yt-dlp  OR  brew install yt-dlp)

Optional dependencies:
    pyyaml  (for --from-queue)
"""

import argparse
import hashlib
import json
import re
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ACTIVE_DIR = REPO_ROOT / "active_sources" / "youtube"
FINGERPRINTS = REPO_ROOT / "cold_storage" / "fingerprints.json"
QUEUE_FILE = REPO_ROOT / "queue.yml"


def check_ytdlp() -> None:
    try:
        subprocess.run(["yt-dlp", "--version"], capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        sys.exit("yt-dlp not found. Install with: pip install yt-dlp")


def slugify(text: str, max_len: int = 40) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text[:max_len] or "unknown"


def fetch_video_metadata(url: str) -> dict:
    """Use yt-dlp to dump metadata as JSON without downloading the video."""
    result = subprocess.run(
        ["yt-dlp", "--dump-json", "--skip-download", "--no-warnings", url],
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(result.stdout)


def fetch_transcript(url: str, out_dir: Path) -> Path | None:
    """Download auto-generated subtitles as VTT, then convert to plain text."""
    out_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "yt-dlp",
            "--write-auto-subs",
            "--skip-download",
            "--sub-langs", "en.*",
            "--sub-format", "vtt",
            "--no-warnings",
            "-o", str(out_dir / "%(id)s.%(ext)s"),
            url,
        ],
        capture_output=True,
        check=False,
    )

    vtt_files = list(out_dir.glob("*.vtt"))
    if not vtt_files:
        return None

    vtt = vtt_files[0].read_text()
    # Strip VTT timing lines and cue identifiers; keep only text
    lines = []
    for line in vtt.splitlines():
        if "-->" in line or line.strip().isdigit() or line.startswith("WEBVTT") or not line.strip():
            continue
        text = re.sub(r"<[^>]+>", "", line).strip()
        if text and (not lines or lines[-1] != text):
            lines.append(text)

    transcript_path = out_dir / "transcript.txt"
    transcript_path.write_text("\n".join(lines))
    for vtt_file in vtt_files:
        vtt_file.unlink()
    return transcript_path


def load_fingerprints() -> dict:
    if FINGERPRINTS.exists():
        return json.loads(FINGERPRINTS.read_text())
    return {}


def save_fingerprints(fps: dict) -> None:
    FINGERPRINTS.parent.mkdir(parents=True, exist_ok=True)
    FINGERPRINTS.write_text(json.dumps(fps, indent=2, sort_keys=True))


def ingest_video(url: str, tags: list[str] | None = None) -> Path | None:
    print(f"Fetching video {url}...", file=sys.stderr)
    meta = fetch_video_metadata(url)
    video_id = meta.get("id", "")
    channel = slugify(meta.get("channel", "unknown"))
    canonical_url = f"https://youtube.com/watch?v={video_id}"

    fps = load_fingerprints()
    fp_key = canonical_url
    if fp_key in fps:
        print(f"  SKIP: video {video_id} already ingested", file=sys.stderr)
        return None

    out_dir = ACTIVE_DIR / channel / video_id
    transcript = fetch_transcript(url, out_dir)

    record = {
        "url": canonical_url,
        "video_id": video_id,
        "title": meta.get("title", ""),
        "channel": meta.get("channel", ""),
        "channel_id": meta.get("channel_id", ""),
        "upload_date": meta.get("upload_date", ""),
        "duration_seconds": meta.get("duration"),
        "description": (meta.get("description") or "")[:1000],
        "chapters": meta.get("chapters") or [],
        "tags": tags or [],
        "has_transcript": transcript is not None,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }
    (out_dir / "meta.json").write_text(json.dumps(record, indent=2))

    fps[fp_key] = {
        "video_id": video_id,
        "channel": channel,
        "fetched_at": record["fetched_at"],
    }
    save_fingerprints(fps)

    status = "with transcript" if transcript else "no transcript available"
    print(f"  OK: active_sources/youtube/{channel}/{video_id}/ ({status})", file=sys.stderr)
    return out_dir


def channel_rss_url(channel_ref: str) -> str:
    """Resolve a channel URL or @handle to its RSS feed URL."""
    if channel_ref.startswith("UC") and len(channel_ref) == 24:
        return f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_ref}"

    # Fetch the channel page and grep for channelId
    if channel_ref.startswith("@"):
        url = f"https://www.youtube.com/{channel_ref}"
    elif "youtube.com" in channel_ref:
        url = channel_ref
    else:
        url = f"https://www.youtube.com/@{channel_ref}"

    with urllib.request.urlopen(url, timeout=30) as resp:
        html = resp.read().decode("utf-8", errors="replace")
    m = re.search(r'"channelId":"(UC[^"]+)"', html)
    if not m:
        raise RuntimeError(f"Could not resolve channel ID for {channel_ref}")
    return f"https://www.youtube.com/feeds/videos.xml?channel_id={m.group(1)}"


def ingest_channel(channel_ref: str, limit: int = 10, tags: list[str] | None = None) -> None:
    print(f"Fetching channel {channel_ref}...", file=sys.stderr)
    rss_url = channel_rss_url(channel_ref)
    with urllib.request.urlopen(rss_url, timeout=30) as resp:
        rss = resp.read().decode("utf-8", errors="replace")

    video_ids = re.findall(r"<yt:videoId>([^<]+)</yt:videoId>", rss)
    print(f"  Found {len(video_ids)} videos in feed; ingesting latest {min(limit, len(video_ids))}", file=sys.stderr)

    for vid in video_ids[:limit]:
        try:
            ingest_video(f"https://youtube.com/watch?v={vid}", tags=tags)
        except Exception as e:
            print(f"  ERROR ingesting {vid}: {e}", file=sys.stderr)


def process_queue() -> None:
    try:
        import yaml  # type: ignore
    except ImportError:
        sys.exit("pyyaml required for --from-queue (pip install pyyaml)")

    data = yaml.safe_load(QUEUE_FILE.read_text()) or {}
    yt = data.get("youtube") or {}
    for entry in (yt.get("videos") or []):
        url = entry if isinstance(entry, str) else entry.get("url")
        tags = entry.get("tags") if isinstance(entry, dict) else None
        if url:
            try:
                ingest_video(url, tags=tags)
            except Exception as e:
                print(f"  ERROR: {e}", file=sys.stderr)
    for entry in (yt.get("channels") or []):
        ref = entry if isinstance(entry, str) else entry.get("url")
        tags = entry.get("tags") if isinstance(entry, dict) else None
        limit = entry.get("limit", 10) if isinstance(entry, dict) else 10
        if ref:
            try:
                ingest_channel(ref, limit=limit, tags=tags)
            except Exception as e:
                print(f"  ERROR: {e}", file=sys.stderr)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--video", help="YouTube video URL")
    group.add_argument("--channel", help="YouTube channel URL or @handle")
    group.add_argument("--from-queue", action="store_true", help="Process all entries in queue.yml")
    ap.add_argument("--limit", type=int, default=10, help="Max videos when ingesting a channel (default: 10)")
    ap.add_argument("--tag", action="append", default=[], help="Tag to apply (repeatable)")
    args = ap.parse_args()

    check_ytdlp()

    if args.video:
        ingest_video(args.video, tags=args.tag)
    elif args.channel:
        ingest_channel(args.channel, limit=args.limit, tags=args.tag)
    elif args.from_queue:
        process_queue()


if __name__ == "__main__":
    main()

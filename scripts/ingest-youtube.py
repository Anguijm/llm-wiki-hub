#!/usr/bin/env python3
"""
ingest-youtube.py - Fetch YouTube transcripts into active_sources/youtube/

Usage:
    python scripts/ingest-youtube.py --video <url>
    python scripts/ingest-youtube.py --channel <url-or-handle>
    python scripts/ingest-youtube.py --from-queue     # one-shot URLs from queue.yml
    python scripts/ingest-youtube.py --from-tracked   # subscriptions from tracked_channels.yml

Output:
    active_sources/youtube/<channel>/<video-id>/
        transcript.txt   # plain-text transcript
        meta.json        # title, channel, published date, description, url, tags

Required dependencies:
    youtube-transcript-api  (pip install youtube-transcript-api)

Optional dependencies:
    pyyaml  (for --from-queue and --from-tracked)

Design note
-----------
This script deliberately avoids yt-dlp. YouTube aggressively blocks
bot-like traffic from datacenter IPs (GitHub Actions runners, AWS,
Azure), and yt-dlp's full-browser impersonation often fails with
HTTP 429 / sign-in-required errors. Instead we use two narrow APIs
that don't trigger bot detection:

  - Channel RSS feeds (https://www.youtube.com/feeds/videos.xml?channel_id=...)
    give us: video_id, title, published, author, description, view count.

  - youtube-transcript-api calls the public transcript endpoint
    (the same one the YouTube player uses for closed captions) --
    no JS runtime, no browser impersonation.

  - YouTube oEmbed (https://www.youtube.com/oembed?...) is the fallback
    for --video mode when we have a URL but no RSS entry, since it
    returns title + author_name without auth.
"""

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ACTIVE_DIR = REPO_ROOT / "active_sources" / "youtube"
FINGERPRINTS = REPO_ROOT / "cold_storage" / "fingerprints.json"
QUEUE_FILE = REPO_ROOT / "queue.yml"
TRACKED_FILE = REPO_ROOT / "tracked_channels.yml"

USER_AGENT = "Mozilla/5.0 (compatible; llm-wiki-hub/1.0)"

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "yt": "http://www.youtube.com/xml/schemas/2015",
    "media": "http://search.yahoo.com/mrss/",
}

VIDEO_ID_RE = re.compile(r"(?:v=|/watch\?v=|youtu\.be/|/embed/|/v/)([A-Za-z0-9_-]{11})")


def check_deps() -> None:
    try:
        import youtube_transcript_api  # noqa: F401
    except ImportError:
        sys.exit(
            "youtube-transcript-api not found. "
            "Install with: pip install youtube-transcript-api  (or pip install -r requirements.txt)"
        )


def slugify(text: str, max_len: int = 40) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text[:max_len] or "unknown"


def extract_video_id(url: str) -> str:
    m = VIDEO_ID_RE.search(url)
    if not m:
        raise ValueError(f"Could not extract video ID from URL: {url}")
    return m.group(1)


def load_fingerprints() -> dict:
    if FINGERPRINTS.exists():
        return json.loads(FINGERPRINTS.read_text())
    return {}


def save_fingerprints(fps: dict) -> None:
    FINGERPRINTS.parent.mkdir(parents=True, exist_ok=True)
    FINGERPRINTS.write_text(json.dumps(fps, indent=2, sort_keys=True))


def fetch_transcript(video_id: str) -> list[dict] | None:
    """Return transcript segments (or None if unavailable / private)."""
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api._errors import (
        TranscriptsDisabled,
        NoTranscriptFound,
        VideoUnavailable,
    )

    try:
        fetched = YouTubeTranscriptApi().fetch(video_id, languages=["en", "en-US", "en-GB"])
        return [
            {"text": seg.text, "start": seg.start, "duration": seg.duration}
            for seg in fetched
        ]
    except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable):
        return None
    except Exception as e:
        print(f"    transcript fetch error: {type(e).__name__}: {e}", file=sys.stderr)
        return None


def write_transcript(segments: list[dict], out_dir: Path) -> Path:
    """Write a plain-text transcript with blank lines between segments."""
    lines = []
    prev_text = None
    for seg in segments:
        text = seg["text"].strip()
        if text and text != prev_text:
            lines.append(text)
            prev_text = text
    path = out_dir / "transcript.txt"
    path.write_text("\n".join(lines))
    return path


def fetch_oembed(url: str) -> dict:
    """Fetch basic video metadata via the public oEmbed endpoint."""
    oembed_url = f"https://www.youtube.com/oembed?url={urllib.parse.quote(url, safe='')}&format=json"
    req = urllib.request.Request(oembed_url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def parse_rss_entry(entry: ET.Element) -> dict:
    """Extract metadata from a single <entry> in a YouTube channel RSS feed."""
    def text(path: str) -> str:
        el = entry.find(path, NS)
        return (el.text or "").strip() if el is not None and el.text else ""

    link = entry.find("atom:link", NS)
    author_name = entry.find("atom:author/atom:name", NS)
    description_el = entry.find("media:group/media:description", NS)
    stats = entry.find("media:group/media:community/media:statistics", NS)

    video_id = text("yt:videoId")
    return {
        "video_id": video_id,
        "channel_id": text("yt:channelId"),
        "title": text("atom:title"),
        "published": text("atom:published"),
        "updated": text("atom:updated"),
        "author": author_name.text.strip() if author_name is not None and author_name.text else "",
        "link": link.get("href") if link is not None else f"https://youtube.com/watch?v={video_id}",
        "description": (description_el.text or "").strip() if description_el is not None and description_el.text else "",
        "views": int(stats.get("views", 0)) if stats is not None and stats.get("views") else None,
    }


def ingest_from_metadata(metadata: dict, tags: list[str] | None = None) -> Path | None:
    """Common ingestion path: given metadata dict, fetch transcript and write output."""
    video_id = metadata["video_id"]
    channel = slugify(metadata.get("author") or metadata.get("channel") or "unknown")
    canonical_url = f"https://youtube.com/watch?v={video_id}"

    fps = load_fingerprints()
    if canonical_url in fps:
        print(f"  SKIP: {video_id} already ingested", file=sys.stderr)
        return None

    print(f"  fetching transcript for {video_id}...", file=sys.stderr)
    segments = fetch_transcript(video_id)

    out_dir = ACTIVE_DIR / channel / video_id
    out_dir.mkdir(parents=True, exist_ok=True)

    if segments is not None:
        write_transcript(segments, out_dir)

    record = {
        "url": canonical_url,
        "video_id": video_id,
        "title": metadata.get("title", ""),
        "channel": metadata.get("author") or metadata.get("channel") or "",
        "channel_id": metadata.get("channel_id", ""),
        "published": metadata.get("published", ""),
        "description": (metadata.get("description") or "")[:2000],
        "view_count": metadata.get("views"),
        "tags": tags or [],
        "has_transcript": segments is not None,
        "transcript_segments": len(segments) if segments else 0,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }
    (out_dir / "meta.json").write_text(json.dumps(record, indent=2))

    # Only fingerprint when transcript was obtained. Videos with no
    # transcript (disabled/unavailable) are re-tried on every run so a
    # transient failure doesn't permanently lock them out.
    if segments is not None:
        fps[canonical_url] = {
            "video_id": video_id,
            "channel": channel,
            "fetched_at": record["fetched_at"],
        }
        save_fingerprints(fps)
        status = f"with transcript ({len(segments)} segments)"
    else:
        status = "no transcript (will retry next run)"

    print(f"  OK: active_sources/youtube/{channel}/{video_id}/ ({status})", file=sys.stderr)
    return out_dir


def ingest_video(url: str, tags: list[str] | None = None) -> Path | None:
    """Ingest a single video given a URL (for --video mode)."""
    print(f"Fetching video {url}...", file=sys.stderr)
    video_id = extract_video_id(url)
    oembed = fetch_oembed(url)
    metadata = {
        "video_id": video_id,
        "title": oembed.get("title", ""),
        "author": oembed.get("author_name", ""),
        "channel_id": "",
        "published": "",
        "description": "",
        "views": None,
    }
    return ingest_from_metadata(metadata, tags=tags)


def channel_rss_url(channel_ref: str) -> str:
    """Resolve a channel URL or @handle to its RSS feed URL."""
    if channel_ref.startswith("UC") and len(channel_ref) == 24:
        return f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_ref}"

    if channel_ref.startswith("@"):
        url = f"https://www.youtube.com/{channel_ref}"
    elif "youtube.com" in channel_ref:
        url = channel_ref
    else:
        url = f"https://www.youtube.com/@{channel_ref}"

    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        html = resp.read().decode("utf-8", errors="replace")
    m = re.search(r'"channelId":"(UC[^"]+)"', html)
    if not m:
        raise RuntimeError(f"Could not resolve channel ID for {channel_ref}")
    return f"https://www.youtube.com/feeds/videos.xml?channel_id={m.group(1)}"


def ingest_channel(channel_ref: str, limit: int = 10, tags: list[str] | None = None) -> None:
    print(f"Fetching channel {channel_ref}...", file=sys.stderr)
    rss_url = channel_rss_url(channel_ref)

    req = urllib.request.Request(rss_url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        rss_bytes = resp.read()

    root = ET.fromstring(rss_bytes)
    entries = root.findall("atom:entry", NS)
    print(
        f"  Found {len(entries)} videos in feed; ingesting latest {min(limit, len(entries))}",
        file=sys.stderr,
    )

    for entry in entries[:limit]:
        try:
            metadata = parse_rss_entry(entry)
            if not metadata["video_id"]:
                continue
            ingest_from_metadata(metadata, tags=tags)
        except Exception as e:
            vid = metadata.get("video_id", "?") if "metadata" in locals() else "?"
            print(f"  ERROR ingesting {vid}: {type(e).__name__}: {e}", file=sys.stderr)


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


def process_tracked() -> None:
    """Re-scan every channel group in tracked_channels.yml.

    Unlike --from-queue, this does NOT mutate the input file: tracked
    channels are persistent subscriptions. Dedup via fingerprints.json
    ensures only new videos produce transcripts on each run.
    """
    try:
        import yaml  # type: ignore
    except ImportError:
        sys.exit("pyyaml required for --from-tracked (pip install pyyaml)")

    if not TRACKED_FILE.exists():
        sys.exit(f"No tracked_channels.yml at {TRACKED_FILE}")

    data = yaml.safe_load(TRACKED_FILE.read_text()) or {}
    groups = data.get("channels") or {}
    if not groups:
        print("No channel groups found in tracked_channels.yml", file=sys.stderr)
        return

    for group_name, group_config in groups.items():
        if not isinstance(group_config, dict):
            continue
        tags = group_config.get("tags") or [group_name]
        limit = group_config.get("limit", 10)
        sources = group_config.get("sources") or []

        print(
            f"\n=== Group: {group_name} ({len(sources)} channels, limit={limit}) ===",
            file=sys.stderr,
        )
        for source in sources:
            if isinstance(source, str):
                ref = source
            elif isinstance(source, dict):
                ref = source.get("channel_id") or source.get("handle") or source.get("url")
            else:
                continue
            if not ref:
                continue
            try:
                ingest_channel(ref, limit=limit, tags=tags)
            except Exception as e:
                print(f"  ERROR ingesting {ref}: {type(e).__name__}: {e}", file=sys.stderr)


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--video", help="YouTube video URL")
    group.add_argument("--channel", help="YouTube channel URL or @handle")
    group.add_argument(
        "--from-queue", action="store_true",
        help="Process all entries in queue.yml (one-shot)",
    )
    group.add_argument(
        "--from-tracked", action="store_true",
        help="Re-scan all channels in tracked_channels.yml (subscriptions)",
    )
    ap.add_argument("--limit", type=int, default=10, help="Max videos per channel (default: 10)")
    ap.add_argument("--tag", action="append", default=[], help="Tag to apply (repeatable)")
    args = ap.parse_args()

    check_deps()

    if args.video:
        ingest_video(args.video, tags=args.tag)
    elif args.channel:
        ingest_channel(args.channel, limit=args.limit, tags=args.tag)
    elif args.from_queue:
        process_queue()
    elif args.from_tracked:
        process_tracked()


if __name__ == "__main__":
    main()

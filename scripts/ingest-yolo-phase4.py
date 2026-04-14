#!/usr/bin/env python3
"""
ingest-yolo-phase4.py - Sync experiment summaries from yolo-projects Phase 4

Usage:
    python scripts/ingest-yolo-phase4.py              # from GitHub (default)
    python scripts/ingest-yolo-phase4.py --local PATH # from a local yolo-projects clone

This is a "fast-path" ingest that bypasses our YouTube scraping pipeline.
The upstream project (github.com/Anguijm/yolo-projects) already runs a
daily cron that scans 10 AI/dev YouTube channels, extracts experiment
cards via Gemini, and commits them to experiments.json. These entries
are pre-synthesized (hypothesis, actionable steps, outcome, verdict),
so we generate wiki pages directly from structured data — no Claude
summarization step needed.

Output:
    wiki/experiments/<experiment-id>.md         # generated wiki page
    cold_storage/yolo-phase4/<experiment-id>/   # raw data archive
        data.json                               # source experiment record
        phase4_run.json                         # upstream run metadata (once per sync)

Fingerprints are recorded under the "phase4:<id>" namespace in
cold_storage/fingerprints.json so re-runs only generate pages for
newly-added experiments.
"""

import argparse
import hashlib
import json
import re
import sys
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = REPO_ROOT / "wiki" / "experiments"
INDEX_PATH = REPO_ROOT / "wiki" / "experiments-index.md"
ARCHIVE_DIR = REPO_ROOT / "cold_storage" / "yolo-phase4"
FINGERPRINTS = REPO_ROOT / "cold_storage" / "fingerprints.json"

UPSTREAM = "Anguijm/yolo-projects"
UPSTREAM_BRANCH = "main"
RAW_BASE = f"https://raw.githubusercontent.com/{UPSTREAM}/{UPSTREAM_BRANCH}"
USER_AGENT = "Mozilla/5.0 (compatible; llm-wiki-hub/1.0)"


def fetch_json(url: str) -> dict | list:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def load_fingerprints() -> dict:
    if FINGERPRINTS.exists():
        return json.loads(FINGERPRINTS.read_text())
    return {}


def save_fingerprints(fps: dict) -> None:
    FINGERPRINTS.parent.mkdir(parents=True, exist_ok=True)
    FINGERPRINTS.write_text(json.dumps(fps, indent=2, sort_keys=True))


def slugify(text: str, max_len: int = 60) -> str:
    text = (text or "").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text[:max_len] or "untitled"


def normalize_channel(raw: str) -> str:
    """Normalize channel names: @NateBJones, NateBJones -> '@natebjones'."""
    if not raw:
        return ""
    return "@" + raw.lstrip("@").lower()


def render_wiki_page(exp: dict) -> str:
    src = exp.get("source", {}) or {}
    e = exp.get("experiment", {}) or {}
    title = e.get("title", "Untitled experiment")
    channel = src.get("channel", "")
    video_title = src.get("video_title", "")
    video_url = src.get("video_url", "")
    published = src.get("published_date", "")
    ingested = src.get("ingested_date", "")

    status = exp.get("status", "")
    verdict = exp.get("verdict", "")
    effort = e.get("effort_estimate", "")
    steps = e.get("actionable_steps") or []
    history = exp.get("status_history") or []
    targets = e.get("target_project_ids") or []

    lines: list[str] = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append("> Back to [[experiments-index]]")
    lines.append("")
    source_parts = [video_title and f"**[{video_title}]({video_url})**"]
    if channel:
        source_parts.append(channel)
    if published:
        source_parts.append(published)
    lines.append("Source: " + " · ".join(p for p in source_parts if p))
    lines.append("")
    badges = []
    if status:
        badges.append(f"**Status:** `{status}`")
    if verdict:
        badges.append(f"**Verdict:** `{verdict}`")
    if effort:
        badges.append(f"**Effort:** `{effort}`")
    if badges:
        lines.append(" · ".join(badges))
        lines.append("")
    lines.append("---")
    lines.append("")

    def section(heading: str, body: str) -> None:
        if body and body.strip():
            lines.append(f"## {heading}")
            lines.append("")
            lines.append(body.strip())
            lines.append("")

    section("Hypothesis", e.get("hypothesis", ""))
    section("What they did", e.get("what_they_did", ""))

    if steps:
        lines.append("## Actionable steps")
        lines.append("")
        for step in steps:
            lines.append(f"- {step}")
        lines.append("")

    section("Success metric", e.get("success_metric", ""))
    section("Relevance to YOLO loop", e.get("relevance_to_yolo_loop", ""))

    if targets:
        lines.append("## Target projects")
        lines.append("")
        for t in targets:
            # Map known upstream projects to wiki-links
            if t in {"yolo-loop-infrastructure", "yolo-projects"}:
                lines.append(f"- [[yolo-projects]] (`{t}`)")
            else:
                lines.append(f"- `{t}`")
        lines.append("")

    section("Outcome", exp.get("outcome", ""))
    section("Notes", exp.get("notes", ""))

    if history:
        lines.append("## Status history")
        lines.append("")
        lines.append("| Date | Status | Note |")
        lines.append("|---|---|---|")
        for h in history:
            note = (h.get("note", "") or "").replace("|", "\\|")
            lines.append(
                f"| {h.get('date', '')} | `{h.get('status', '')}` | {note} |"
            )
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Metadata")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append(f"| Experiment ID | `{exp.get('id', '')}` |")
    lines.append(f"| Channel | {channel} |")
    if video_url:
        lines.append(f"| Video | [{video_title or video_url}]({video_url}) |")
    if published:
        lines.append(f"| Published | {published} |")
    if ingested:
        lines.append(f"| Ingested upstream | {ingested} |")
    lines.append(
        f"| Source | [yolo-projects/experiments.json]"
        f"(https://github.com/{UPSTREAM}/blob/{UPSTREAM_BRANCH}/experiments.json) |"
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Related pages")
    lines.append("")
    lines.append("- [[yolo-projects]] - upstream pipeline that synthesized this experiment")
    lines.append("- [[yolo-phase4-integration]] - how experiments are synced into this wiki")
    lines.append("- [[experiments-index]] - all experiments")
    lines.append("- [[index]] - wiki home")
    return "\n".join(lines) + "\n"


def ingest_experiment(exp: dict, fps: dict) -> bool:
    """Write wiki page + archive + fingerprint. Returns True if newly added."""
    eid = exp.get("id")
    if not eid:
        return False

    fp_key = f"phase4:{eid}"
    content_hash = hashlib.sha256(
        json.dumps(exp, sort_keys=True).encode("utf-8")
    ).hexdigest()
    if fp_key in fps and fps[fp_key].get("hash") == content_hash:
        return False

    # Wiki page
    slug = slugify(eid)
    wiki_path = WIKI_DIR / f"{slug}.md"
    wiki_path.parent.mkdir(parents=True, exist_ok=True)
    wiki_path.write_text(render_wiki_page(exp))

    # Raw archive
    archive_dir = ARCHIVE_DIR / slug
    archive_dir.mkdir(parents=True, exist_ok=True)
    (archive_dir / "data.json").write_text(json.dumps(exp, indent=2))

    fps[fp_key] = {
        "slug": slug,
        "hash": content_hash,
        "synced_at": datetime.now(timezone.utc).isoformat(),
    }
    return True


def normalize_channel(raw: str) -> str:
    """Normalize '@NateBJones' and 'NateBJones' -> '@NateBJones' for index grouping."""
    if not raw:
        return ""
    return "@" + raw.lstrip("@")


def render_index(experiments: list[dict]) -> str:
    """Regenerate wiki/experiments-index.md from the full upstream list.

    Called on every sync so the index never drifts from the per-page
    set. Uses normalized channel names so '@NateBJones' and 'NateBJones'
    collapse into one row.
    """
    # Work on a copy with normalized channel names so we don't mutate callers.
    norm_exps = []
    for e in experiments:
        src = dict(e.get("source") or {})
        src["channel"] = normalize_channel(src.get("channel", ""))
        norm_exps.append({**e, "source": src})

    status_counts = Counter(e.get("status") or "(none)" for e in norm_exps)
    verdict_counts = Counter(e.get("verdict") or "(none)" for e in norm_exps)
    channel_counts = Counter(e["source"].get("channel", "") for e in norm_exps)

    sorted_exps = sorted(
        norm_exps,
        key=lambda e: (e["source"].get("published_date", ""), e.get("id", "")),
        reverse=True,
    )

    lines: list[str] = []
    lines.append("# Experiments Index")
    lines.append("")
    lines.append("> Back to [[index]]")
    lines.append("")
    lines.append(
        f"**{len(norm_exps)} experiments** synthesized from the [[yolo-projects]] "
        "Phase 4 YouTube research pipeline, covering AI/dev content from 10 tracked "
        "channels."
    )
    lines.append("")
    lines.append(
        "This page is regenerated automatically by `scripts/ingest-yolo-phase4.py` "
        "on every sync. See [[yolo-phase4-integration]] for the full flow."
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## By status")
    lines.append("")
    lines.append("| Status | Count |")
    lines.append("|---|---|")
    for st, n in sorted(status_counts.items(), key=lambda x: -x[1]):
        lines.append(f"| `{st}` | {n} |")
    lines.append("")
    lines.append("## By verdict")
    lines.append("")
    lines.append("| Verdict | Count |")
    lines.append("|---|---|")
    for v, n in sorted(verdict_counts.items(), key=lambda x: -x[1]):
        lines.append(f"| `{v}` | {n} |")
    lines.append("")
    lines.append("## By channel")
    lines.append("")
    lines.append("| Channel | Experiments |")
    lines.append("|---|---|")
    for ch, n in sorted(channel_counts.items(), key=lambda x: -x[1]):
        lines.append(f"| {ch} | {n} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## All experiments")
    lines.append("")
    lines.append("Ordered by published date, most recent first.")
    lines.append("")
    lines.append("| Date | Title | Channel | Verdict |")
    lines.append("|---|---|---|---|")
    for e in sorted_exps:
        eid = e.get("id", "")
        title = ((e.get("experiment") or {}).get("title") or "Untitled").replace("|", "\\|")
        ch = e["source"].get("channel", "")
        date = e["source"].get("published_date", "")
        verdict = e.get("verdict") or "-"
        lines.append(
            f"| {date} | [[experiments/{slugify(eid)}|{title}]] | {ch} | `{verdict}` |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Related pages")
    lines.append("")
    lines.append("- [[yolo-projects]] - upstream pipeline")
    lines.append("- [[yolo-phase4-integration]] - sync mechanism")
    lines.append("- [[tracked-channels-schema]] - the 10 source channels")
    lines.append("- [[index]] - wiki home")
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "--local",
        type=Path,
        default=None,
        help="Path to a local yolo-projects clone (default: fetch from GitHub raw)",
    )
    args = ap.parse_args()

    if args.local:
        base = args.local.resolve()
        print(f"Reading from local clone: {base}", file=sys.stderr)
        experiments = json.loads((base / "experiments.json").read_text())
        run_meta_path = base / "phase4_run.json"
        run_meta = json.loads(run_meta_path.read_text()) if run_meta_path.exists() else {}
    else:
        print(f"Fetching from {RAW_BASE}...", file=sys.stderr)
        experiments = fetch_json(f"{RAW_BASE}/experiments.json")
        try:
            run_meta = fetch_json(f"{RAW_BASE}/phase4_run.json")
        except Exception as e:
            print(f"  (could not fetch phase4_run.json: {e})", file=sys.stderr)
            run_meta = {}

    if not isinstance(experiments, list):
        sys.exit("experiments.json was not a list")

    fps = load_fingerprints()
    added = 0
    total = len(experiments)

    for exp in experiments:
        if ingest_experiment(exp, fps):
            added += 1

    # Record upstream run metadata
    if run_meta:
        (ARCHIVE_DIR / "phase4_run.json").parent.mkdir(parents=True, exist_ok=True)
        (ARCHIVE_DIR / "phase4_run.json").write_text(json.dumps(run_meta, indent=2))

    save_fingerprints(fps)

    # Regenerate the index every run so it always reflects the full
    # upstream set (new experiments, updated verdicts, etc.) rather
    # than drifting from the seed snapshot.
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(render_index(experiments))

    print(f"Synced {added} new experiments ({total} total upstream)", file=sys.stderr)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
ingest-article.py - Fetch a web article into active_sources/articles/

Usage:
    python scripts/ingest-article.py <url>
    python scripts/ingest-article.py --from-queue   # process queue.yml

Output:
    active_sources/articles/<slug>/
        content.md     # cleaned markdown
        meta.json      # url, title, author, date, tags, hash

Optional dependencies (graceful fallback if missing):
    - readability-lxml : better content extraction
    - html2text        : HTML -> markdown conversion
    - pyyaml           : queue.yml parsing

Install with: pip install readability-lxml html2text pyyaml
"""

import argparse
import hashlib
import json
import re
import sys
import urllib.request
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ACTIVE_DIR = REPO_ROOT / "active_sources" / "articles"
COLD_DIR = REPO_ROOT / "cold_storage" / "articles"
FINGERPRINTS = REPO_ROOT / "cold_storage" / "fingerprints.json"
QUEUE_FILE = REPO_ROOT / "queue.yml"

USER_AGENT = "Mozilla/5.0 (compatible; llm-wiki-hub/1.0)"


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def extract_content(html: str, url: str) -> tuple[str, str, str]:
    """Return (title, author, markdown_content). Falls back if deps missing."""
    title = ""
    author = ""

    # Try readability-lxml first
    try:
        from readability import Document  # type: ignore
        doc = Document(html)
        title = doc.short_title() or ""
        content_html = doc.summary()
    except ImportError:
        # Fallback: naive <title> + full body
        m = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
        title = m.group(1).strip() if m else ""
        content_html = html

    # Author extraction (meta tags)
    for pattern in [
        r'<meta\s+name="author"\s+content="([^"]+)"',
        r'<meta\s+property="article:author"\s+content="([^"]+)"',
        r'<meta\s+name="twitter:creator"\s+content="@?([^"]+)"',
    ]:
        m = re.search(pattern, html, re.IGNORECASE)
        if m:
            author = m.group(1).strip()
            break

    # Convert HTML to markdown
    try:
        import html2text  # type: ignore
        h = html2text.HTML2Text()
        h.body_width = 0
        h.ignore_images = False
        markdown = h.handle(content_html)
    except ImportError:
        # Fallback: strip tags
        markdown = re.sub(r"<[^>]+>", "", content_html)
        markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()

    return title, author, markdown


def slugify(text: str, max_len: int = 80) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text[:max_len] or "untitled"


def make_slug(url: str, author: str, title: str) -> str:
    author_part = slugify(author, 30) if author else urllib.parse.urlparse(url).netloc.split(".")[-2]
    title_part = slugify(title, 60) if title else hashlib.md5(url.encode()).hexdigest()[:8]
    return f"{author_part}-{title_part}"


def load_fingerprints() -> dict:
    if FINGERPRINTS.exists():
        return json.loads(FINGERPRINTS.read_text())
    return {}


def save_fingerprints(fps: dict) -> None:
    FINGERPRINTS.parent.mkdir(parents=True, exist_ok=True)
    FINGERPRINTS.write_text(json.dumps(fps, indent=2, sort_keys=True))


def ingest(url: str, tags: list[str] | None = None, note: str = "") -> Path | None:
    print(f"Fetching {url}...", file=sys.stderr)
    html = fetch(url)
    content_hash = hashlib.sha256(html.encode()).hexdigest()

    fps = load_fingerprints()
    if url in fps and fps[url]["hash"] == content_hash:
        print(f"  SKIP: already ingested with same content hash", file=sys.stderr)
        return None

    title, author, markdown = extract_content(html, url)
    slug = make_slug(url, author, title)
    out_dir = ACTIVE_DIR / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "content.md").write_text(markdown)
    meta = {
        "url": url,
        "title": title,
        "author": author,
        "slug": slug,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "content_hash": content_hash,
        "tags": tags or [],
        "note": note,
    }
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=2))

    fps[url] = {"hash": content_hash, "slug": slug, "fetched_at": meta["fetched_at"]}
    save_fingerprints(fps)

    print(f"  OK: active_sources/articles/{slug}/", file=sys.stderr)
    return out_dir


def process_queue() -> None:
    try:
        import yaml  # type: ignore
    except ImportError:
        sys.exit("pyyaml required for --from-queue (pip install pyyaml)")

    data = yaml.safe_load(QUEUE_FILE.read_text()) or {}
    articles = data.get("articles") or []
    for entry in articles:
        if isinstance(entry, str):
            ingest(entry)
        elif isinstance(entry, dict) and "url" in entry:
            ingest(entry["url"], tags=entry.get("tags"), note=entry.get("note", ""))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url", nargs="?", help="Article URL to ingest")
    ap.add_argument("--from-queue", action="store_true", help="Process all entries in queue.yml")
    ap.add_argument("--tag", action="append", default=[], help="Tag to apply (repeatable)")
    args = ap.parse_args()

    if args.from_queue:
        process_queue()
    elif args.url:
        ingest(args.url, tags=args.tag)
    else:
        ap.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

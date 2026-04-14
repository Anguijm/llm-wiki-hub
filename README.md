# llm-wiki-hub

**A personal, Git-backed wiki for documenting codebases, Medium articles, and YouTube transcripts.** Inspired by [Karpathy's LLMwiki](https://github.com/karpathy/LLMwiki).

Every source (a GitHub repo, a blog post, a video transcript) becomes a Markdown page in `wiki/`, interlinked via `[[wiki-links]]`, and browsable in Obsidian, Foam, or GitHub's web UI. A three-stage pipeline (`active_sources/` → `wiki/` → `cold_storage/`) keeps the repo lightweight while preserving full source access locally.

---

## Quick Start

```bash
git clone https://github.com/Anguijm/llm-wiki-hub.git
cd llm-wiki-hub
```

Open the `wiki/` directory in [Obsidian](https://obsidian.md/) as a vault for the best browsing experience (clickable `[[wiki-links]]` + graph view). Start at [`wiki/index.md`](wiki/index.md).

---

## How It Works

```
┌──────────────────┐      ┌──────────────┐      ┌──────────────────┐
│  active_sources/  │─────►│    wiki/     │─────►│  cold_storage/   │
│                   │      │              │      │                  │
│  Unprocessed      │      │  Generated   │      │  Processed       │
│  clones, articles,│      │  markdown    │      │  sources         │
│  transcripts      │      │  docs        │      │  (archived)      │
└──────────────────┘      └──────────────┘      └──────────────────┘
    Ingest scripts          Claude writes       Move after wiki
    drop sources here       wiki pages          page ships
```

Three source types, one pipeline:

| Type          | Ingest tool                             | Lands in                           | Wiki page                        |
| ------------- | --------------------------------------- | ---------------------------------- | -------------------------------- |
| GitHub repo   | `git clone`                             | `active_sources/repos/<name>/`     | `wiki/<name>.md`                 |
| Article       | `scripts/ingest-article.py`             | `active_sources/articles/<slug>/`  | `wiki/articles/<slug>.md`        |
| YouTube video | `scripts/ingest-youtube.py --video`     | `active_sources/youtube/<ch>/<id>/`| `wiki/videos/<ch>-<id>.md`       |

Contents of `active_sources/` and `cold_storage/` are gitignored; only the generated wiki content and directory structure are committed.

---

## How To: Add Sources

### Path A — Queue + auto-ingest (recommended)

1. **Add URLs to `queue.yml`** at the repo root:

   ```yaml
   articles:
     - https://medium.com/@author/some-post
     - url: https://simonwillison.net/2024/some-post
       tags: [llm, prompt-engineering]

   youtube:
     videos:
       - https://youtube.com/watch?v=VIDEO_ID
     channels:
       - https://youtube.com/@AndrejKarpathy

   repos:
     - https://github.com/karpathy/nanoGPT
   ```

2. **Run the ingest scripts** to fetch content into `active_sources/`:

   ```bash
   python scripts/ingest-article.py --from-queue
   python scripts/ingest-youtube.py --from-queue
   ```

3. **Ask Claude to generate wiki pages**:

   > "Process the new sources in `active_sources/` into wiki pages."

   Claude reads each source, writes a wiki page at the appropriate path, adds an entry to [`wiki/articles-index.md`](wiki/articles-index.md) or [`wiki/videos-index.md`](wiki/videos-index.md), cross-links to related projects/articles via `[[wiki-links]]`, and moves the source to `cold_storage/`.

4. **Clean the queue** — remove the processed URLs from `queue.yml`.

5. **Commit**:

   ```bash
   git add wiki/ queue.yml
   git commit -m "add: wiki pages for <sources>"
   git push
   ```

### Path B — One-off ingestion (no queue)

```bash
# Single article
python scripts/ingest-article.py https://example.com/article --tag llm

# Single video
python scripts/ingest-youtube.py --video https://youtube.com/watch?v=VIDEO_ID

# Latest 10 videos from a channel (uses YouTube's RSS feed, no API key needed)
python scripts/ingest-youtube.py --channel @AndrejKarpathy --limit 10
```

### Path C — GitHub repo

```bash
cd active_sources/repos
git clone https://github.com/<owner>/<repo>.git
cd ../..
```

Then ask Claude:

> "Read `active_sources/repos/<repo>/` and create a wiki page following the standard template."

---

## Requirements

| Tool                             | Required? | Why                                                   |
| -------------------------------- | --------- | ----------------------------------------------------- |
| Git ≥ 2.x                        | Yes       | Source control                                        |
| A Markdown viewer                | Yes       | Obsidian, Foam, VS Code, GitHub web UI, or any editor |
| Python ≥ 3.10                    | Optional  | Only if you want to run the ingest scripts            |

If you want richer ingest quality, install the optional Python packages:

```bash
pip install readability-lxml html2text pyyaml yt-dlp
```

| Package           | Purpose                                                 |
| ----------------- | ------------------------------------------------------- |
| `readability-lxml`| Clean article content extraction (vs. raw HTML)         |
| `html2text`       | HTML → Markdown conversion                              |
| `pyyaml`          | Required for `--from-queue` mode                        |
| `yt-dlp`          | YouTube transcript and metadata fetching                |

All scripts fall back to stdlib-only behavior when optional packages are missing; the fallbacks work, they just produce rougher output.

---

## Directory Layout

```
llm-wiki-hub/
├── README.md                    This file
├── queue.yml                    Inbox for URLs awaiting ingestion
│
├── scripts/
│   ├── ingest-article.py        Fetch web articles
│   └── ingest-youtube.py        Fetch YouTube transcripts via yt-dlp
│
├── active_sources/              Unprocessed (gitignored contents)
│   ├── repos/
│   ├── articles/
│   └── youtube/
│
├── cold_storage/                Processed (gitignored contents)
│   ├── fingerprints.json        URL → content hash (dedup + update detection)
│   ├── repos/
│   ├── articles/
│   └── youtube/
│
└── wiki/                        All wiki docs (committed)
    ├── index.md                 Central hub and table of contents
    ├── articles-index.md        Processed articles (chronological)
    ├── videos-index.md          Processed videos (chronological)
    ├── queue-schema.md          queue.yml format reference
    ├── <repo-name>.md           One page per GitHub repo
    ├── articles/<slug>.md       One page per article
    ├── videos/<slug>.md         One page per video
    └── [meta-docs]              architecture, dependencies, setup-guide, etc.
```

---

## Deduplication

`cold_storage/fingerprints.json` maps each ingested URL to a SHA-256 hash of its content. Re-queueing the same URL is a no-op if nothing changed; if the source was updated (e.g., a Medium article was edited), the hash changes and the ingest script fetches the new version.

Videos without available transcripts are **not** fingerprinted, so they'll be retried on each run (cheap — `yt-dlp` returns quickly when subs are unavailable). This prevents transient `yt-dlp` failures from permanently locking out retries.

---

## Where to Go Next

- [`wiki/index.md`](wiki/index.md) — Main table of contents
- [`wiki/architecture.md`](wiki/architecture.md) — Full pipeline architecture
- [`wiki/setup-guide.md`](wiki/setup-guide.md) — Detailed setup and usage
- [`wiki/queue-schema.md`](wiki/queue-schema.md) — Full `queue.yml` format reference
- [`wiki/dependencies.md`](wiki/dependencies.md) — Cross-project dependency map

---

## License

Personal project. See the repository root for license details if added.

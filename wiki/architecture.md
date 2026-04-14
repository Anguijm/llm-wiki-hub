# Architecture

> Back to [[index]]

---

## Overview

LLM Wiki Hub is a **static, file-based documentation system** with a three-stage processing pipeline that handles three source types: GitHub repos, articles, and YouTube videos. There is no runtime server or database.

## Processing Pipeline

```
                ┌─────────────────────┐
                │      queue.yml       │  (URLs waiting to be ingested)
                └──────────┬──────────┘
                           │
     ┌─────────────────────┼─────────────────────┐
     │                     │                     │
     ▼                     ▼                     ▼
┌──────────┐        ┌──────────┐          ┌──────────┐
│  git     │        │ ingest-  │          │ ingest-  │
│  clone   │        │ article  │          │ youtube  │
└────┬─────┘        └────┬─────┘          └────┬─────┘
     │                    │                     │
     ▼                    ▼                     ▼
┌─────────────────────────────────────────────────────┐
│  active_sources/                                     │
│    ├── repos/<name>/                                 │
│    ├── articles/<slug>/   content.md + meta.json     │
│    └── youtube/<channel>/<id>/  transcript.txt + ... │
└────────────────────────┬────────────────────────────┘
                         │  Claude reads source,
                         │  writes wiki page
                         ▼
┌─────────────────────────────────────────────────────┐
│  wiki/                                               │
│    ├── <repo>.md                                     │
│    ├── articles/<slug>.md                            │
│    └── videos/<channel>-<id>.md                      │
│    All cross-linked via [[wiki-links]]               │
└────────────────────────┬────────────────────────────┘
                         │  Archive after
                         │  documentation ships
                         ▼
┌─────────────────────────────────────────────────────┐
│  cold_storage/                                       │
│    ├── repos/<name>/                                 │
│    ├── articles/<slug>/                              │
│    ├── youtube/<channel>/<id>/                       │
│    └── fingerprints.json   (URL → content hash)      │
└─────────────────────────────────────────────────────┘
```

## Source Types

| Type | Ingest Tool | Active Path | Wiki Path |
|---|---|---|---|
| GitHub repo | `git clone` | `active_sources/repos/<name>/` | `wiki/<name>.md` |
| Article | `scripts/ingest-article.py` | `active_sources/articles/<slug>/` | `wiki/articles/<slug>.md` |
| YouTube video | `scripts/ingest-youtube.py --video` | `active_sources/youtube/<channel>/<id>/` | `wiki/videos/<channel>-<id>.md` |
| YouTube channel | `scripts/ingest-youtube.py --channel` | Same as video (per-video folders) | One page per video |

## Workflow

1. **Queue** - Drop URLs into `queue.yml` under the appropriate section (`articles`, `youtube.videos`, `youtube.channels`, `repos`). See [[queue-schema]].
2. **Ingest** - Run the matching ingest script. Content + metadata land in `active_sources/<type>/<slug>/`.
3. **Deduplicate** - Scripts check `cold_storage/fingerprints.json` (URL → content hash). Re-queuing a URL with unchanged content is a no-op; changed content triggers re-processing.
4. **Summarize** - Claude reads the source, generates a wiki page with summary, key ideas, quotes, and `[[wiki-links]]` to related projects and articles.
5. **Index** - Claude updates [[articles-index]] or [[videos-index]] with the new entry.
6. **Archive** - Source material moves to `cold_storage/<type>/<slug>/`. The fingerprint record persists.
7. **Remove from queue** - The URL is deleted from `queue.yml`.

## Design Decisions

### 1. Three source types, unified pipeline

Repos, articles, and YouTube transcripts share the same three-stage flow (`active_sources/` → `wiki/` → `cold_storage/`) and the same deduplication store (`fingerprints.json`). Adding a new source type (e.g., podcasts) means one more subdirectory and one more ingest script -- no architectural changes.

### 2. Queue file as the only "API"

`queue.yml` is the single inbox. You edit it, run an ingest script (or ask Claude), and the pipeline handles the rest. No web UI, no service to run, no scheduler.

### 3. Markdown-only output, tool-agnostic

All wiki content is GitHub-Flavored Markdown with `[[wiki-links]]`. Files render correctly in Obsidian, Foam, GitHub's web UI, and any Markdown viewer. No build step.

### 4. `.gitignore` sources, commit wiki

`active_sources/` and `cold_storage/` contents are gitignored. Only directory structure is tracked (via `.gitkeep`). This keeps the repo lightweight while preserving full local source access for re-processing.

### 5. Graceful dependency fallbacks

Ingest scripts use optional dependencies (`readability-lxml`, `html2text`, `yt-dlp`, `pyyaml`) and fall back to stdlib-only behavior when they're missing. The pipeline works on a clean machine; installing the optional deps just improves quality.

### 6. Content hashing for updates

`fingerprints.json` maps URL → SHA-256 of fetched content. If a Medium article is edited and re-queued, the hash changes and triggers re-ingestion; unchanged content is skipped. This catches meaningful updates without re-processing the whole queue on every run.

### 7. One page per source, flat namespaces

- Repos at top level of `wiki/`: `wiki/sportsdata.md`
- Articles in their own subdirectory: `wiki/articles/<slug>.md`
- Videos in their own subdirectory: `wiki/videos/<slug>.md`

This keeps [[wiki-links]] short while avoiding name collisions between source types.

## Future Considerations

| Consideration | Notes |
|---|---|
| Automated queue processing | Cron-triggered `python scripts/ingest-*.py --from-queue` on commit |
| Link validation | CI check to verify all `[[wiki-links]]` resolve |
| Static-site generation | MkDocs or Jekyll could render to a hosted site |
| Podcasts / PDFs | Add `active_sources/podcasts/` etc. with corresponding ingest scripts |
| Full-text search | Client-side Lunr.js index across all wiki pages |

---

## Related Pages

- [[project-overview]] - Why this wiki exists
- [[repository-structure]] - Detailed file layout
- [[queue-schema]] - Queue format and entry structure
- [[setup-guide]] - Running the pipeline
- [[dependencies]] - Cross-project and pipeline dependencies

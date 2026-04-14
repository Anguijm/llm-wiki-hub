# Queue Schema

> Back to [[index]]

---

## Overview

`queue.yml` is the central inbox for URLs awaiting wiki processing. It lives at the repository root (not inside `wiki/`) so it doesn't get rendered as wiki content.

## File Location

```
llm-wiki-hub/
├── queue.yml           <-- Here
├── scripts/
│   ├── ingest-article.py
│   └── ingest-youtube.py
└── wiki/
    └── queue-schema.md <-- This doc
```

## Schema

### Top-level sections

| Section | Type | Ingested by |
|---|---|---|
| `articles` | list | `scripts/ingest-article.py` |
| `youtube.channels` | list | `scripts/ingest-youtube.py --channel` |
| `youtube.videos` | list | `scripts/ingest-youtube.py --video` |
| `repos` | list | `git clone` (manual or scripted) |

### Entry formats

Each list item can be either:

**Simple form** (URL only):

```yaml
articles:
  - https://medium.com/@author/some-post
```

**Extended form** (URL + metadata):

```yaml
articles:
  - url: https://medium.com/@author/some-post
    tags: [llm, training]
    priority: high      # high | normal | low (default: normal)
    note: "Related to sportsdata ratchet loop work"
```

### YouTube-specific fields

```yaml
youtube:
  channels:
    - url: https://youtube.com/@AndrejKarpathy
      fetch_all: false         # if true, ingest every video (default: false = latest 10)
      since: 2024-01-01        # only ingest videos after this date
  videos:
    - url: https://youtube.com/watch?v=VIDEO_ID
      chapters: true           # include chapter timestamps (default: true)
      tags: [transformers]
```

## Processing Workflow

```
queue.yml
    │
    ▼
Ingest scripts     ──► active_sources/<type>/<slug>/
                        ├── content.md / transcript.txt
                        └── meta.json
    │
    ▼
Claude summarizes  ──► wiki/<type>/<slug>.md   (generated wiki page)
                        with [[wiki-links]] cross-refs
    │
    ▼
Archive            ──► cold_storage/<type>/<slug>/
                        (source material preserved for re-processing)
    │
    ▼
Remove from queue.yml
```

## Slug Generation

| Type | Slug format | Example |
|---|---|---|
| Article | `<author>-<title-slug>` | `karpathy-yes-you-should-understand-backprop` |
| YouTube video | `<channel-handle>-<video-id>` | `andrejkarpathy-zjkBMFhNj_g` |
| Repo | Repo name | `nanoGPT` |

Slugs must match `[a-z0-9-]+` and be unique within their type.

## Deduplication

Before ingesting, scripts check `cold_storage/fingerprints.json` (created on first run) which maps URL → content hash. This prevents re-processing the same article if it's queued again, and detects meaningful updates (e.g., Medium article edits).

## Related Pages

- [[setup-guide]] - How to run the ingest scripts
- [[architecture]] - Full pipeline architecture
- [[index]] - Main table of contents

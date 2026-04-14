# Setup Guide

> Back to [[index]]

---

## Prerequisites

### Required

- **Git** >= 2.x - [Download Git](https://git-scm.com/downloads)
- **Python** >= 3.10 - Only needed if you want to run the ingest scripts
- A **text editor** or Markdown viewer

### Optional (improves ingest quality)

```bash
pip install readability-lxml html2text pyyaml yt-dlp
```

| Package | Purpose |
|---|---|
| `readability-lxml` | Better article content extraction |
| `html2text` | Clean HTML → Markdown conversion |
| `pyyaml` | Required for `--from-queue` mode |
| `yt-dlp` | YouTube transcript fetching |

See [[dependencies]] for the full dependency map.

## Clone the Repository

```bash
git clone https://github.com/anguijm/llm-wiki-hub.git
cd llm-wiki-hub
```

## Browse the Wiki

| Option | Tool |
|---|---|
| **Best**: Graph view + clickable wiki-links | [Obsidian](https://obsidian.md/) -- open `wiki/` as vault |
| VS Code with wiki-link support | [Foam](https://foambubble.github.io/foam/) extension |
| Read-only on GitHub | Navigate to `wiki/` on github.com |
| Any text editor | Markdown renders readably even without link support |

## Adding Sources

### Path A: Queue + auto-ingest (recommended)

1. **Add URLs to `queue.yml`**:

   ```yaml
   articles:
     - https://medium.com/@author/some-post

   youtube:
     videos:
       - https://youtube.com/watch?v=VIDEO_ID
     channels:
       - https://youtube.com/@SomeChannel
   ```

2. **Run the ingest scripts**:

   ```bash
   python scripts/ingest-article.py --from-queue
   python scripts/ingest-youtube.py --from-queue
   ```

3. **Ask Claude to summarize**:

   > "Process the new sources in `active_sources/` into wiki pages."

   Claude will read each ingested source, generate a wiki page at `wiki/articles/<slug>.md` or `wiki/videos/<slug>.md`, add an entry to [[articles-index]] or [[videos-index]], cross-link to related projects, and move the source to `cold_storage/`.

4. **Clean the queue**: Remove the processed URLs from `queue.yml`.

5. **Commit**:

   ```bash
   git add wiki/ queue.yml
   git commit -m "add: wiki pages for <sources>"
   git push
   ```

### Path B: One-off ingestion (no queue)

```bash
# Single article
python scripts/ingest-article.py https://example.com/article --tag llm --tag training

# Single video
python scripts/ingest-youtube.py --video https://youtube.com/watch?v=VIDEO_ID --tag transformers

# Latest 10 videos from a channel
python scripts/ingest-youtube.py --channel @AndrejKarpathy --limit 10
```

### Path C: Adding a new GitHub repo

```bash
cd active_sources/repos
git clone https://github.com/Anguijm/<repo-name>.git
cd ../..
```

Then ask Claude:

> "Read `active_sources/repos/<repo-name>/` and create a wiki page following the standard template."

Claude will generate `wiki/<repo-name>.md`, add it to [[index]], cross-link related projects, and move the clone to `cold_storage/repos/`.

## Wiki Page Templates

### Per-repo

```markdown
# repo-name

> Back to [[index]]

**One-line description.**

| Property | Value |
|---|---|
| Repository | [Anguijm/repo-name](https://github.com/Anguijm/repo-name) |
| Language | ... |
| Status | Active / Archived / Empty |

---

## Overview
## Architecture
## Key Modules
## Dependencies
## Notable Design Decisions

---

## Related Pages
- [[related-project]]
- [[index]]
```

### Per-article

```markdown
# Article Title

> Back to [[articles-index]]

**Author · Published Date · [Source URL]**

---

## Summary
## Key Ideas
## Quotes
## Related Work

---

## Related Pages
- [[related-project-or-article]]
- [[articles-index]]
```

### Per-video

```markdown
# Video Title

> Back to [[videos-index]]

**Channel · Upload Date · Duration · [YouTube URL]**

---

## Summary
## Chapter Highlights
## Key Quotes
## Related Work

---

## Related Pages
- [[related-project-or-video]]
- [[videos-index]]
```

## Dedup and Updates

`cold_storage/fingerprints.json` records every ingested URL and its content hash. Re-queueing the same URL is a no-op if nothing changed; if a Medium article was edited, the hash changes and the ingest script will fetch it again.

---

## Related Pages

- [[dependencies]] - Required and optional tools
- [[queue-schema]] - `queue.yml` format reference
- [[contributing]] - Content style guidelines
- [[repository-structure]] - Where everything lives
- [[architecture]] - Processing pipeline design

# Tracked Channels Schema

> Back to [[index]]

---

## Overview

`tracked_channels.yml` at the repository root is a persistent subscription list of YouTube channels to re-scan on every run. It complements [[queue-schema|queue.yml]]:

| File                   | Semantics              | Lifetime                                  |
| ---------------------- | ---------------------- | ----------------------------------------- |
| `queue.yml`            | One-shot inbox         | Entries are removed after processing       |
| `tracked_channels.yml` | Persistent subscriptions | Entries stay; only new videos are fetched |

Deduplication uses `cold_storage/fingerprints.json` just like every other source type, so re-running `--from-tracked` is cheap after the initial sync.

## File Location

```
llm-wiki-hub/
├── queue.yml                 # one-shot URLs
├── tracked_channels.yml      # <-- here: persistent YouTube subscriptions
├── scripts/
│   └── ingest-youtube.py     # supports --from-tracked
└── wiki/
    └── tracked-channels-schema.md   # this doc
```

## Schema

```yaml
channels:
  <group-name>:
    tags: [<tag>, ...]        # optional; applied to every video in this group
    limit: 10                 # optional; max latest videos per channel per run
    sources:
      - handle: "@SomeHandle"
        channel_id: UC...     # preferred; bypasses handle resolution
      - "@OtherHandle"        # simple string also accepted
      - url: https://youtube.com/@Channel   # URL form also accepted
```

### Fields

| Field                      | Type          | Required? | Purpose                                                       |
| -------------------------- | ------------- | --------- | ------------------------------------------------------------- |
| `channels`                 | mapping       | Yes       | Top-level key; values are groups                              |
| `channels.<group>.tags`    | list[str]     | No        | Tags applied to every video in the group (default: `[group]`) |
| `channels.<group>.limit`   | int           | No        | Max latest videos per channel per run (default: 10)           |
| `channels.<group>.sources` | list          | Yes       | Channel references (string, or object with `handle` / `channel_id` / `url`) |

### Group Convention

Groups let you apply shared tags and rate limits to related channels. Use kebab-case group names (e.g., `yolo-phase4`, `security-research`, `llm-papers`).

### Channel Reference Forms

The script accepts three source formats, in order of preference:

1. **`channel_id`** - YouTube's `UC...` identifier. Fastest (no handle resolution), stable even if the channel renames itself.
2. **`handle`** - `@handle` form. Resolved to `channel_id` at runtime by scraping the channel page for `"channelId":"UC..."`.
3. **`url`** - Full channel URL.

Always prefer `channel_id` when known.

## Usage

```bash
# Scan every group, ingest new videos
python scripts/ingest-youtube.py --from-tracked
```

Per run, the script:

1. Loads `tracked_channels.yml`
2. For each group, iterates every source:
   - Resolves to an RSS feed URL: `https://www.youtube.com/feeds/videos.xml?channel_id=UC...`
   - Reads the feed, extracts video IDs for the latest `limit` videos
   - For each video not already in `fingerprints.json`, calls `ingest_video(...)` which fetches transcript + metadata via `yt-dlp`
3. Errors on any single channel or video are logged but do NOT abort the run

Videos whose transcript fetch fails (network, rate limit) are **not** fingerprinted, so they'll be retried on the next run.

## Seed List: yolo-phase4

The repository ships with one pre-populated group: `yolo-phase4`, ported from the [yolo-projects Phase 4 research pipeline](https://github.com/Anguijm/yolo-projects/blob/main/fetch_youtube_rss.py). 10 channels focused on AI dev / MLOps content:

| Handle          | Channel ID                |
| --------------- | ------------------------- |
| `@NateBJones`   | UC0C-17n9iuUQPylguM1d-lQ |
| `@MLOps`        | UCG6qpjVnBTTT8wLGBygANOQ |
| `@DavidOndrej`  | UCPGrgwfbkjTIgPoOh2q1BAg |
| `[un]prompted`  | UC5GCrYGsm7EHQzQZj65A-5w |
| `@NateHerk`     | UC2ojq-nuP8ceeHqiroeKhBA |
| `@swyx`         | UC50YKpKY_2Y86Qo4DZY3mMQ |
| `@GregKamradt`  | UC7mHKIdjuKTJVamHqR5JTRg |
| `@AIJasonZ`     | UCrXSVX9a1mj8l0CMLwKgMVw |
| `@echohive`     | UCL7przoMtZTmiQMhc9ifIww |
| `@ShawTalebi`   | UCa9gErQ9AE5jT2DZLjXBIdA |

## Adding a New Group

Edit `tracked_channels.yml` and append:

```yaml
channels:
  yolo-phase4:
    # ...existing...

  llm-interpretability:
    tags: [interpretability, research]
    limit: 5
    sources:
      - handle: "@AnthropicResearch"
        channel_id: UC...
      - handle: "@neelnanda-io"
        channel_id: UC...
```

Commit and push. Next `--from-tracked` run will pick it up.

## Related Pages

- [[queue-schema]] - One-shot URL queue (`queue.yml`)
- [[videos-index]] - Generated wiki pages for processed videos
- [[architecture]] - Full pipeline overview
- [[setup-guide]] - Running the ingest scripts
- [[yolo-projects]] - Source of the seed channel list
- [[index]] - Main table of contents

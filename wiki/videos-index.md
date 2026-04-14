# Videos Index

> Back to [[index]]

**Chronological list of processed YouTube video transcripts and channel scrapes.**

---

## Processed Videos

_No videos processed yet. Add URLs to `queue.yml` under `youtube.videos:` or `youtube.channels:` and run `python scripts/ingest-youtube.py --from-queue` to fetch transcripts. See [[queue-schema]] for full format._

<!--
Maintain this table as videos are processed. Format:

| Date | Channel | Title | Duration | Tags | Wiki Page |
|---|---|---|---|---|---|
| 2026-04-15 | @AndrejKarpathy | Let's build GPT | 1h56m | llm, transformers | [[videos/andrejkarpathy-kCc8FmEb1nY]] |

-->

---

## Processed Channels

_No channels processed yet._

<!--
| Channel | Handle | Videos Ingested | Last Updated |
|---|---|---|---|
| Andrej Karpathy | @AndrejKarpathy | 12 | 2026-04-15 |
-->

---

## How to Add a Video or Channel

### Single video

1. Add URL to `queue.yml` under `youtube.videos:`
2. Run `python scripts/ingest-youtube.py --from-queue`
3. Transcript lands in `active_sources/youtube/<channel>/<video-id>/`
4. Ask Claude to summarize into `wiki/videos/<channel>-<video-id>.md`

### Entire channel

1. Add channel URL or `@handle` to `queue.yml` under `youtube.channels:`
2. Run `python scripts/ingest-youtube.py --from-queue` (fetches latest 10 by default)
3. Each video is stored separately and can be summarized individually

Requires `yt-dlp` installed (`pip install yt-dlp`).

See [[setup-guide]] for the full workflow and [[queue-schema]] for queue format details.

---

## Related Pages

- [[articles-index]] - Medium articles and blog posts
- [[queue-schema]] - How `queue.yml` is structured
- [[setup-guide]] - Ingest script usage
- [[index]] - Main table of contents

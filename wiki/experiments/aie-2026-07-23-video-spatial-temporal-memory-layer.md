# Build a persistent spatiotemporal memory layer for video assets that supports cross-file entity continuity and moment retrieval

> Back to [[experiments-index]]

Source: **[Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs](https://www.youtube.com/watch?v=mOf-PP4mVjA)** · aie · 2026-07-23

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we index video content as spatiotemporal semantic chunks (not frames) with multimodal embeddings that preserve temporal relationships, then agents can answer cross-file, cross-episode queries (who appeared when, what changed, what caused what) that frame-level or transcript-only approaches cannot handle, because meaning in video derives from sequence and continuity rather than any individual frame.

## What they did

James Le from TwelveLabs described a five-layer video cognition stack: semantic temporal chunks → multimodal embeddings (Marengo encoder) that capture spatial-temporal relations → a context store preserving moments/entities/metadata → a video-aware language model (Pegasus) for reasoning → an API layer. He distinguished video memory from video search: search finds similar moments, memory links today's scene to something in another file/season/camera angle and preserves who appeared, what changed, and what caused what. He demonstrated the stack on soccer footage (player identification across scenes), traffic camera footage (vehicle counting, collision detection, condition awareness), and advertising footage (brand moment classification for ad placement). He framed the stack as infrastructure, not an application, for developers building content assembly, compliance review, highlight generation, and surveillance workflows.

## Relevance to YOLO loop

If our yolo loop processes or generates video content (screen recordings, demos, walkthroughs), a spatiotemporal memory layer would enable agents to query our own recorded sessions for specific moments, track what changed between runs, or build a searchable archive of agent behavior over time — capabilities unavailable with frame sampling or transcript-only indexing.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-23-video-spatial-temporal-memory-layer` |
| Channel | aie |
| Video | [Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs](https://www.youtube.com/watch?v=mOf-PP4mVjA) |
| Published | 2026-07-23 |
| Ingested upstream | 2026-07-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Build a Real-Time Narrated Film Generator by Chaining Claude, Grok CLI, and Local TTS

> Back to [[experiments-index]]

Source: **[world's fastest video maker app!](https://www.youtube.com/watch?v=IBzkb-DnUUo)** · eh · 2026-10-08

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we chain Claude Code (story writing) → Grok CLI (image generation) → local TTS voice synthesis into a single browser-triggered pipeline, then we can produce a narrated illustrated film faster than it plays back, because each tool runs concurrently and generation stays ahead of playback.

## What they did

The creator built an app where typing a topic triggers Claude to write a story, Grok's command-line tool to paint frames live in various styles (engraving, inkwash, gouache, etc.), and a local voice to narrate — all in the browser with no video model. A 32-second film was generated in ~22 seconds. Claude Opus was used as the building agent to orchestrate all tools. The app supports 7 painting styles, adjustable motion, word-by-word captions, and export to wide or vertical video with an end card.

## Relevance to YOLO loop

Demonstrates a multi-tool agentic pipeline pattern (LLM → image gen CLI → TTS → browser renderer) that could be adapted for automated demo or documentation video generation within a dev loop artifact pipeline.

## Notes

Requires Mac with Apple Silicon, Claude Code account, Grok CLI account. Windows/Linux adaptation requires pointing a coding agent at the folder. Startup time ~4 seconds for first frame. Times vary by topic and length.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `eh-2026-10-08-instant-video-pipeline-claude-grok` |
| Channel | eh |
| Video | [world's fastest video maker app!](https://www.youtube.com/watch?v=IBzkb-DnUUo) |
| Published | 2026-10-08 |
| Ingested upstream | 2026-10-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Integrate GPT Native Image Generation into Asset Pipeline

> Back to [[experiments-index]]

Source: **[OpenAI just destroyed all AI image tools… GPT Images 2.0](https://www.youtube.com/watch?v=XdQq90Ug8eY)** · DavidOndrej · 2026-04-24

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we replace external image generation tools (Midjourney, DALL-E via API, Stable Diffusion) with GPT's native image generation in our asset pipeline, then we can reduce tool-switching overhead and improve prompt-to-asset coherence because native generation uses the same context window and instruction-following as the rest of the dev loop.

## What they did

Speaker demonstrated GPT Images 2.0 capabilities including text rendering accuracy, instruction following for complex compositions, and style consistency — showing it outperforming dedicated image generation tools on practical use cases.

## Relevance to YOLO loop

Relevant to any asset generation step in our loop (UI mockups, diagrams, marketing assets). Native integration means one fewer external API call and tighter context continuity.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-04-24-gpt-images-native-gen` |
| Channel | DavidOndrej |
| Video | [OpenAI just destroyed all AI image tools… GPT Images 2.0](https://www.youtube.com/watch?v=XdQq90Ug8eY) |
| Published | 2026-04-24 |
| Ingested upstream | 2026-04-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

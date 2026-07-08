# Anchor AI game generation to a single key art image to enforce visual and tonal coherence

> Back to [[experiments-index]]

Source: **[Think You Can Build a Game with AI? Think Again! - Danielle An & David Hoe, Meta](https://www.youtube.com/watch?v=grdoOC1BT1s)** · aie · 2026-07-08

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we provide a single key art image as a reference anchor when prompting a model to generate a game, then the resulting game will have stronger visual and tonal cohesion across UI, story, and art because the image constrains the model's aesthetic search space to a single consistent style.

## What they did

Meta's AI game creation team demonstrated a workflow where an art director uses a single key art image (e.g., a bear illustration) as an anchor for the generative model. Instead of purely text-based prompts, the image guides the model's output so that all generated assets—UI, characters, environments—feel like they belong to the same visual universe. This was presented as a step change in output quality over pure text prompting.

## Relevance to YOLO loop

Applicable as a prompt-engineering technique: when generating any visual or structured creative output in our loop, providing a reference artifact as an anchor can reduce variance and improve coherence on the first pass.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-08-key-art-anchor-game-generation` |
| Channel | aie |
| Video | [Think You Can Build a Game with AI? Think Again! - Danielle An & David Hoe, Meta](https://www.youtube.com/watch?v=grdoOC1BT1s) |
| Published | 2026-07-08 |
| Ingested upstream | 2026-07-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

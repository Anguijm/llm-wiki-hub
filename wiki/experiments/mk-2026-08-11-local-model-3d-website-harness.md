# Add a skill-router function to a local agent harness for asset-type-aware generation

> Back to [[experiments-index]]

Source: **[3D Websites Just Became FREE (One Prompt)](https://www.youtube.com/watch?v=FSnubu4Lpz8)** · mk · 2026-08-11

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we extend a local agent harness (e.g., pi.dev) with a skill-router function that selects domain-specific generation skills (immersive web, editorial web, effects) based on the requested output type, then the local model can produce correctly structured visual assets without manual retries because the router constrains the model's approach before generation begins.

## What they did

Mark built on top of a pi.dev local harness using a Qwen 3.5 122B model (notes 27-40B is sufficient) and added three named skills: 'immersive web' for 3D scroll experiences, 'editorial web' for flat structured sites, and an 'effects menu' for load animations. He had a closed-source model (Codex) analyze his existing harness and write the skill-router and skill files. The agent then used browser-use to self-check its output in a loop, catching a blank-screen failure and iterating without human intervention. The full 3D website including video assets was generated locally in ~25 minutes hands-off.

## Relevance to YOLO loop

Maps directly to harness engineering in our dev loop — specifically the idea of adding a skill-router layer so agents select the right generation strategy per task type rather than defaulting to a generic approach, and the self-checking browser-use loop as an automated acceptance test.

## Notes

Mark mentions making a care package of skills and raw HTML available; worth retrieving as seed material for our own skill definitions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-08-11-local-model-3d-website-harness` |
| Channel | mk |
| Video | [3D Websites Just Became FREE (One Prompt)](https://www.youtube.com/watch?v=FSnubu4Lpz8) |
| Published | 2026-08-11 |
| Ingested upstream | 2026-08-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

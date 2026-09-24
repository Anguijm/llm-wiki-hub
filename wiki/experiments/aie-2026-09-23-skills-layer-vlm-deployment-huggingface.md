# Wrap VLMs in a Skills Layer Instead of Deploying Raw Models

> Back to [[experiments-index]]

Source: **[Skill issue: stop deploying vision language models, use them with Skills — Merve Noyan, Hugging Face](https://www.youtube.com/watch?v=dKcTBQzR7jI)** · aie · 2026-09-23

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we deploy vision language models wrapped in a structured Skills abstraction layer rather than as raw model endpoints, then we get more reliable, composable, and maintainable VLM-powered features because Skills enforce input/output contracts that raw VLM calls lack.

## What they did

Merve Noyan from Hugging Face argued against deploying raw VLMs and demonstrated the Skills framework — a structured way to define, version, and compose VLM capabilities as reusable skill units with defined interfaces.

## Relevance to YOLO loop

High relevance — our loop's vision-capable steps could adopt the Skills pattern to make VLM usage more modular and testable, reducing brittle prompt-level coupling between loop stages.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-23-skills-layer-vlm-deployment-huggingface` |
| Channel | aie |
| Video | [Skill issue: stop deploying vision language models, use them with Skills — Merve Noyan, Hugging Face](https://www.youtube.com/watch?v=dKcTBQzR7jI) |
| Published | 2026-09-23 |
| Ingested upstream | 2026-09-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

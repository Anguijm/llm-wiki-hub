# Evaluate Generalist Agent Foundation Model vs. Task-Specific Fine-Tunes

> Back to [[experiments-index]]

Source: **[Robotics Has Been Stuck for 70 Years — Deepak Pathak, Skild AI](https://www.youtube.com/watch?v=jFHteJjRl8A)** · aie · 2026-09-24

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we train or prompt a single generalist agent foundation model across diverse tasks rather than maintaining separate task-specific fine-tunes, then the generalist model will outperform specialists on novel tasks because broad pretraining builds transferable representations that narrow fine-tuning destroys.

## What they did

Deepak Pathak argued that the reason robotics has stagnated for 70 years is over-reliance on task-specific engineering, and described Skild AI's approach of building generalist robot foundation models that transfer across tasks and embodiments without task-specific retraining.

## Relevance to YOLO loop

We currently build task-specific agent configurations; this experiment would test whether a single generalist prompt/model configuration outperforms our specialized ones on a held-out task set, directly informing our architecture strategy.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-24-skild-ai-generalist-robot` |
| Channel | aie |
| Video | [Robotics Has Been Stuck for 70 Years — Deepak Pathak, Skild AI](https://www.youtube.com/watch?v=jFHteJjRl8A) |
| Published | 2026-09-24 |
| Ingested upstream | 2026-09-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

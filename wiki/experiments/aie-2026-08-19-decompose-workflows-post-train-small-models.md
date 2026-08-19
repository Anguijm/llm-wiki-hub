# Decompose Complex Workflows into Sub-Tasks and Post-Train Small Models Per Sub-Task to Reduce Cost and Latency

> Back to [[experiments-index]]

Source: **[From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge](https://www.youtube.com/watch?v=u6q-byPWUuo)** · aie · 2026-08-19

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we decompose a complex generative task (e.g. clinical note generation) into specific sub-tasks and post-train small specialized models for each sub-task rather than routing everything through a large frontier model, then we can achieve comparable or better quality at significantly lower cost and latency, because each sub-task is a simpler, more bounded problem that a smaller model can master with the right fine-tuning data.

## What they did

Abridge generates clinical notes from 100 million medical conversations per year. Rather than using a frontier model to generate all note sections, they decompose notes into sections (HPI, past medical history, assessment and plan, etc.) and post-train small specialized models for each section and even sub-section. For in-visit order detection, they use cheap fast gate models to detect order-relevant events in the conversation stream, only triggering heavier models when gates fire. They argue that where quality is already maxed out on a sub-task, train a smaller model to reduce cost/latency; where quality is not maxed out and they have unique data (100M medical conversations), they can beat frontier models on that specific sub-task by having better training data and tighter focus.

## Relevance to YOLO loop

The gating pattern (cheap model triggers expensive model only when needed) is immediately applicable to our agent loops to reduce token spend. The sub-task decomposition + specialized fine-tuning is a longer-term investment worth planning if we have a high-volume workflow with a proprietary data advantage.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-19-decompose-workflows-post-train-small-models` |
| Channel | aie |
| Video | [From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge](https://www.youtube.com/watch?v=u6q-byPWUuo) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

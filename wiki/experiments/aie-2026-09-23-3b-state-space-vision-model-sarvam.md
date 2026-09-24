# Train a 3B State-Space Vision Model from Scratch to SOTA

> Back to [[experiments-index]]

Source: **[From Scratch to SOTA: Training a 3B State-Space Vision Model — Krishna Prasad Srinivasan, Sarvam](https://www.youtube.com/watch?v=T72nqdC92PM)** · aie · 2026-09-23

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we train a 3B parameter state-space vision model from scratch using Sarvam's methodology, then we can achieve SOTA-level vision performance at a fraction of the typical compute cost because state-space architectures offer better sequence efficiency than transformer-based VLMs at this parameter scale.

## What they did

Krishna Prasad Srinivasan from Sarvam described their end-to-end process for training a 3B state-space vision model from scratch, covering architecture choices, training data, and the path to achieving state-of-the-art results.

## Relevance to YOLO loop

Relevant if we need a custom vision backbone in our loop — the state-space approach could replace heavier transformer VLMs for vision-based input parsing steps, reducing latency and cost.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-23-3b-state-space-vision-model-sarvam` |
| Channel | aie |
| Video | [From Scratch to SOTA: Training a 3B State-Space Vision Model — Krishna Prasad Srinivasan, Sarvam](https://www.youtube.com/watch?v=T72nqdC92PM) |
| Published | 2026-09-23 |
| Ingested upstream | 2026-09-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

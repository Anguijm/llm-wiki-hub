# Insert a mid-training phase with agentic traces and long-context data before RL post-training

> Back to [[experiments-index]]

Source: **[The Base Model Is Dead — Varun Singh, Arcee AI](https://www.youtube.com/watch?v=xbPriQWXtWM)** · aie · 2026-07-31

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we add a mid-training stage between pre-training and RL that exposes the model to long-context agentic trajectories, then RL training will be more stable and efficient because the model already has stable representations for the distribution it will encounter during rollouts.

## What they did

Varun Singh described mid-training as an emerging practice where models are exposed to the RL distribution (longer contexts, agentic traces, reasoning-style data) before the main RL phase. This bridges the gap between a general pre-trained model and the specialized distribution of RL environments. He noted this can be done even within pre-training for models with long context natively supported.

## Relevance to YOLO loop

Before running RL fine-tuning in our loop, consider a short mid-training run on domain-specific agentic traces to warm up the model to the task distribution, reducing RL instability and cold-start sample inefficiency.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-31 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-31-mid-training-agentic-distribution` |
| Channel | aie |
| Video | [The Base Model Is Dead — Varun Singh, Arcee AI](https://www.youtube.com/watch?v=xbPriQWXtWM) |
| Published | 2026-07-31 |
| Ingested upstream | 2026-07-31 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

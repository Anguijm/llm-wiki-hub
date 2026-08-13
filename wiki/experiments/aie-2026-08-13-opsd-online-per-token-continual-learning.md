# Prototype OPSD-Style Online Per-Token Reward Training from Production Agent Traces

> Back to [[experiments-index]]

Source: **[Scaling up Continual Learning — Ronak Malde, Trajectory](https://www.youtube.com/watch?v=zL1kLftVTlo)** · aie · 2026-08-13

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we replace offline batch RL training with an online, on-policy, single-parallelism algorithm that uses dense per-token rewards derived from real production agent traces, then continual learning will improve faster and more accurately than GRPO-style approaches because the training signal is tied to actual real-world task distributions rather than curated benchmarks.

## What they did

Ronak Malde diagnosed four failure modes in current post-training algorithms: task distribution mismatch (benchmarks divorced from reality), off-policy sampling, exploding parallelism requiring complex environment infrastructure, and sequence-level reward collapsing rich signal into a scalar. He introduced OPSD (Online Per-token Signal Distillation) as an algorithm achieving all four desiderata simultaneously — online task distribution, on-policy sampling, single-rollout parallelism, and per-token dense reward — and demonstrated it on a 12B model on Mercor Apex agents outperforming RL. He also described hint-based interpolation to avoid distribution collapse.

## Relevance to YOLO loop

Maps to continuous improvement of the YOLO loop's agent model: instead of periodic offline fine-tuning, production traces from agent runs could feed an OPSD-style loop that continuously improves the model's task performance without requiring environment infrastructure overhead.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-13-opsd-online-per-token-continual-learning` |
| Channel | aie |
| Video | [Scaling up Continual Learning — Ronak Malde, Trajectory](https://www.youtube.com/watch?v=zL1kLftVTlo) |
| Published | 2026-08-13 |
| Ingested upstream | 2026-08-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

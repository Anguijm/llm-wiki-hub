# Apply pipeline RL with off-policy tolerance to reduce GPU idle time in long-horizon rollouts

> Back to [[experiments-index]]

Source: **[Scaling to Long Horizons — Ross Taylor & Chengxi Taylor, General Reasoning](https://www.youtube.com/watch?v=2bvtay8wGYI)** · aie · 2026-07-31

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we use pipeline RL (starting model weight updates before all rollout sequences finish) with an off-policy tolerance of up to ~8 steps, then GPU utilization will improve during long-horizon RL training without meaningfully degrading policy quality.

## What they did

General Reasoning described the GPU idle time problem in long-horizon RL: standard approaches wait for all inference to finish before training, but long rollouts can take days/weeks. Pipeline RL starts training on completed sequences while others are still generating, accepting some off-policy drift. They found up to ~8 steps of off-policy is acceptable in practice. As an alternative, they described bootstrapping with a value model to generate expected returns mid-episode, though this introduces value model bias.

## Relevance to YOLO loop

Relevant if we run RL training on long agentic tasks. The 8-step off-policy rule-of-thumb is a useful guard rail when configuring pipeline RL in our training infrastructure.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-31 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-31-pipeline-rl-long-horizon` |
| Channel | aie |
| Video | [Scaling to Long Horizons — Ross Taylor & Chengxi Taylor, General Reasoning](https://www.youtube.com/watch?v=2bvtay8wGYI) |
| Published | 2026-07-31 |
| Ingested upstream | 2026-07-31 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Benchmark agents on open-ended real-world tasks (e.g., sports betting) to expose long-horizon weaknesses

> Back to [[experiments-index]]

Source: **[Scaling to Long Horizons — Ross Taylor & Chengxi Taylor, General Reasoning](https://www.youtube.com/watch?v=2bvtay8wGYI)** · aie · 2026-07-31

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we evaluate agents on open-ended, adversarial, real-world tasks with other players/uncertainty (rather than deterministic code tasks), then we will surface reliability failures that closed benchmarks miss, because real-world complexity includes multi-agent dynamics and uncertainty not captured in current evals.

## What they did

General Reasoning ran a sports betting experiment: gave frontier models $100K virtual capital and let them trade. All models lost money. They argued this kind of open-ended, adversarial, real-world benchmark better captures long-horizon agent weaknesses than procedure-following coding tasks, which tend to have one or two correct solutions and limit creativity.

## Relevance to YOLO loop

Designing at least one open-ended evaluation task in our dev loop—where the agent must operate under uncertainty and against other agents or changing conditions—would reveal failure modes that deterministic evals hide.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-31 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-31-open-ended-rl-benchmarks` |
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

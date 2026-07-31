# Run multi-sandbox post-training rollouts for tasks that exceed single-container complexity

> Back to [[experiments-index]]

Source: **[Emulated: The Data for Fully Autonomous Software Engineers and Companies — Joseph Wang](https://www.youtube.com/watch?v=zkX03APVj0M)** · aie · 2026-07-31

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we move from single-sandbox to multi-sandbox environments for post-training rollouts, then agents can learn to coordinate across distributed systems and company-scale workflows, because single-sandbox simulation hits complexity ceilings that require genuine multi-node orchestration to surpass.

## What they did

Emulated observed that single-node simulation gets you far but is not sufficient for truly autonomous software engineering. They are building multi-sandbox environments where each sandbox is a real node, enabling agents to operate across distributed clusters, manage secrets across services, and handle problems that only appear at real scale (e.g., sim-to-real gap, live customer traffic). They described the challenge of fitting long-spinning environments (e.g., spinning up AWS Lambda takes hours) into RL rollout budgets.

## Relevance to YOLO loop

For tasks in our loop that involve multi-service coordination, planning for multi-sandbox rollout infrastructure early—rather than retrofitting it—will reduce rework when single-container complexity is exceeded.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-31 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-31-multi-sandbox-parallel-rollouts` |
| Channel | aie |
| Video | [Emulated: The Data for Fully Autonomous Software Engineers and Companies — Joseph Wang](https://www.youtube.com/watch?v=zkX03APVj0M) |
| Published | 2026-07-31 |
| Ingested upstream | 2026-07-31 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

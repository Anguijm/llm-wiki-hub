# Implement Inner/Outer Training Loop Separation with Agent-Driven Eval Generation

> Back to [[experiments-index]]

Source: **[Recursive Model Improvement — Lee Robinson, Cursor, SpaceXAI](https://www.youtube.com/watch?v=q4Tr-DknG2M)** · aie · 2026-07-15

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we separate model improvement into an outer loop (user feedback, AB tests, metric collection feeding into eval design) and an inner loop (hard evals, difficult RL environments, reward shaping) and use the current best model to generate new evals and training problems for the next round, then training velocity will increase because the intelligence ceiling of the system rises with each model generation and the bottleneck shifts from human researchers to the model itself.

## What they did

Lee Robinson described Cursor's two-loop training architecture. The outer loop ingests thumbs-up/thumbs-down product feedback, online AB test metrics, and internal dogfooding reports to generate higher-quality evals and harder training problems. The inner loop climbs those evals rapidly using RL environments and reward shaping. Cursor trained Composer 2.5 by generating more RL environments, trying new learning methods, and creating more ambitious problem sets. Critically, they use derivative versions of the top-level model as reward models and judges within the inner loop — so when the top model improves, every sub-component improves. Researchers can trigger training runs and eval generation directly from Slack via an agent fleet, which pages them if infrastructure fails, removing human babysitting from the critical path.

## Relevance to YOLO loop

Our YOLO loop could adopt the inner/outer separation: outer loop = collect task outcomes and user corrections into structured eval cases; inner loop = run evals automatically on every prompt/system change. The Slack-triggered agent fleet pattern is directly applicable for automating our eval runs and alerting on regressions without human polling.

## Notes

Key recursive insight: smarter top-level model improves reward models and judge models which improves eval quality which improves next training run. Also notable: Cursor now derives majority of revenue from agent usage not tab-complete, so training data is predominantly agentic trajectories.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-15-recursive-model-improvement-loops` |
| Channel | aie |
| Video | [Recursive Model Improvement — Lee Robinson, Cursor, SpaceXAI](https://www.youtube.com/watch?v=q4Tr-DknG2M) |
| Published | 2026-07-15 |
| Ingested upstream | 2026-07-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

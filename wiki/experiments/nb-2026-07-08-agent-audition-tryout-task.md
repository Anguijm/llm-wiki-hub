# Run a structured audition task before including a new model in a swarm

> Back to [[experiments-index]]

Source: **[Claude Fable 5 Bossed 20 Cheap AI Agents. The Whole Site Cost $8.](https://www.youtube.com/watch?v=suY66oTDn0s)** · nb · 2026-07-08

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we give candidate models a small, constrained tryout task with auto-rejection criteria before adding them to a production swarm, then we can validate speed, instruction-following, and output quality cheaply because the rejection criteria are deterministic and the task is low-stakes.

## What they did

Before including two new models in the swarm, speaker ran an audition: each model had to produce exactly five tagline candidates for a book pre-order page, each 12 words or fewer, with a script that automatically rejected outputs containing predefined 'cheesy' words. One model completed the task in 29 seconds. Both models passed and joined the team.

## Relevance to YOLO loop

Provides a fast gate for evaluating whether a new model or agent config should be trusted with real tasks in the loop before full deployment.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-08-agent-audition-tryout-task` |
| Channel | nb |
| Video | [Claude Fable 5 Bossed 20 Cheap AI Agents. The Whole Site Cost $8.](https://www.youtube.com/watch?v=suY66oTDn0s) |
| Published | 2026-07-08 |
| Ingested upstream | 2026-07-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

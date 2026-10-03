# Build an Automated Model-Routing Harness That Selects the Cheapest Model Meeting Quality Bar Per Task

> Back to [[experiments-index]]

Source: **[Stop Rationing Tokens: Let the Harness Pick the Model — Kimchi by Cast AI](https://www.youtube.com/watch?v=48YUYDjwfYY)** · aie · 2026-10-03

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we route coding agent tasks through a harness that automatically selects the lowest-cost model that achieves the required quality for each task type (rather than always using the most capable model), then token spend will decrease while developer output increases because cost-per-task varies dramatically across models even for equivalent quality, and the harness can react to new model releases faster than human evaluation.

## What they did

Cast AI's Kimchi team built an open-source coding agent harness that autonomously selects the model for each task based on observed cost-per-task (not cost-per-token). Over three months with 300 developers, the harness achieved 2.5x cost savings while token usage grew 1.5x—meaning developers used AI more while spending less. The harness autonomously shifted its model preference from Kim 2.6 to Minimax 3 on June 12 when that model became more cost-effective, a transition no human team noticed or decided. They also demonstrated Teleport (cloud-based persistent agent sessions that survive laptop closure) and Kimchi Studio (team-level session sharing and review in a kanban-style UI).

## Relevance to YOLO loop

Directly addresses model cost governance in our dev loop. Even a simplified version—a routing layer that sends easy tasks (boilerplate, formatting, simple Q&A) to cheaper models and hard tasks (architecture, debugging, reasoning) to frontier models—could meaningfully reduce our token spend without sacrificing output quality.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-03-kimchi-model-routing-harness` |
| Channel | aie |
| Video | [Stop Rationing Tokens: Let the Harness Pick the Model — Kimchi by Cast AI](https://www.youtube.com/watch?v=48YUYDjwfYY) |
| Published | 2026-10-03 |
| Ingested upstream | 2026-10-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

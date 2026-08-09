# Separate Planning and Polish Phases in Agentic Workflows to Prevent Velocity Sickness

> Back to [[experiments-index]]

Source: **[Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](https://www.youtube.com/watch?v=Kz4QJmNrVXU)** · aie · 2026-08-09

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If engineers explicitly separate the planning phase (human-driven decision-making on what to build and key design choices) from the implementation/polish phase (agent-driven code generation), then teams will avoid 'velocity sickness'—high output with low impact—because critical decisions remain human-owned and aligned with team direction before agents run.

## What they did

Matt Dailey described 'velocity sickness' as the stress caused by sudden AI-driven output increases that produce output without impact—too many PRs, agents running in contradictory directions, 'agent bankruptcy' (context lost overnight), and agents making critical architectural decisions. His solution: treat the plan as a 'portal to the software system,' extract all key decisions into a durable shared document before agents implement, share the plan with teammates for alignment, and make agent state stateless so the doc is the ground truth. This keeps humans as the decision owners and makes parallel agents easier to manage.

## Relevance to YOLO loop

Directly maps to adding an explicit planning artifact step before the YOLO loop's generation step—requiring a decision doc to be written and reviewed before agents are unleashed on implementation, preventing divergent agent work and preserving human ownership of architecture.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-09-plan-before-implement` |
| Channel | aie |
| Video | [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](https://www.youtube.com/watch?v=Kz4QJmNrVXU) |
| Published | 2026-08-09 |
| Ingested upstream | 2026-08-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

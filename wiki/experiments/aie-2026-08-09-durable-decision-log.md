# Maintain a Durable Decision Log External to Agent Sessions to Prevent Agent Bankruptcy

> Back to [[experiments-index]]

Source: **[Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](https://www.youtube.com/watch?v=Kz4QJmNrVXU)** · aie · 2026-08-09

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If all key decisions made during agentic sessions are extracted into a persistent external document rather than left in-session, then engineers can resume work after context loss without redoing decisions or re-spending tokens on already-solved problems.

## What they did

Dailey observed that engineers regularly hit 'agent bankruptcy'—closing all sessions after a day of work and losing all context, then restarting the next morning. His fix: make agent output stateless by writing all decisions to an external plan/doc. This doc serves as the human re-entry point to resume any session, as input to parallel agents so they don't diverge, and as a team alignment artifact. He contrasted this with trying to have an LLM summarize session history after the fact, which risks losing the critical decisions.

## Relevance to YOLO loop

Augments the YOLO loop with a lightweight session persistence layer—a decisions.md or similar artifact written at the end of each agentic session that lets the next loop iteration start with full context rather than cold-starting from scratch.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-09-durable-decision-log` |
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

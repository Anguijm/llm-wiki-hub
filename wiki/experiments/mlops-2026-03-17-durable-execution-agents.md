# Evaluate durable execution for long-running agent workflows

> Back to [[experiments-index]]

Source: **[Durable Execution and Modern Distributed Systems](https://www.youtube.com/watch?v=umdiwQbkwlY)** · mlops · 2026-03-17

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `high`

---

## Hypothesis

If we structure long-running YOLO workflows (multi-project refinement, Phase 3 cull) as durable workflows with automatic state persistence, then we eliminate lost progress from crashes/disconnects because the system automatically resumes from the last checkpoint.

## What they did

Johann Schleier-Smith from Temporal described durable execution: Workflows (deterministic control flow) + Activities (side effects with retries). State saved automatically. If failure occurs, replay from last known state. Especially valuable for AI agents running over days/weeks.

## Actionable steps

- Evaluate whether cron-based refinement sessions lose state on failure
- Research Temporal or similar durable execution for the YOLO loop
- Prototype a single refinement cycle as a durable workflow
- Compare reliability vs current cron approach

## Success metric

Zero lost refinement progress due to session crashes or disconnects.

## Relevance to YOLO loop

The YOLO loop runs long sessions via cron that can fail mid-refinement. Durable execution would make the pipeline crash-proof.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

Implemented session_state.json + update_session_state.py. Not Temporal-style heavyweight durable execution — instead, lightweight file-based state persistence that any new session reads to recover full context. Tracks: tick-tock position, pending Deck fixes, Phase 4 queue state, portfolio counts, resume instructions. Script auto-generates state from yolo_log.json, experiments.json, phase4_queue.json, and deck_roadmap.md.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-03-29 | `done` | Evaluated: overkill for current YOLO loop scope |
| 2026-03-31 | `in_progress` | Reconsidered — session-level durable execution via session_state.json, not Temporal |
| 2026-03-31 | `done` | Implemented as lightweight session_state.json, not Temporal |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-03-17-durable-execution-agents` |
| Channel | mlops |
| Video | [Durable Execution and Modern Distributed Systems](https://www.youtube.com/watch?v=umdiwQbkwlY) |
| Published | 2026-03-17 |
| Ingested upstream | 2026-03-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

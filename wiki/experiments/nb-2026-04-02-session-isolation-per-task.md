# Use task-isolated fresh Claude sessions to prevent context bloat

> Back to [[experiments-index]]

Source: **[Your Claude Limit Burns In 90 Minutes Because Of One ChatGPT Habit.](https://www.youtube.com/watch?v=5ztI_dbj6ek)** · nb · 2026-04-02

**Status:** `done` · **Verdict:** `discard` · **Effort:** `low`

---

## Hypothesis

If we start a fresh Claude session for each discrete YOLO task (build, review, logging) instead of continuing a single long session, then we stay within token limits and reduce costs because each session loads only the context it actually needs.

## What they did

Nate identified that developers burn through Claude limits in ~90 minutes because they carry ChatGPT-style long-thread habits into Claude — accumulating context across unrelated tasks instead of treating each task as isolated. The fix is treating Claude as a task executor (fresh session per task) rather than a chatbot (single growing thread).

## Relevance to YOLO loop

The YOLO loop already uses fresh agent sessions for builds, but long Phase 2/3 sessions can accumulate context across multiple project reviews. Explicit session boundaries at task checkpoints would reduce token waste.

## Outcome

Parked — already solved. Cron fires fresh isolated sessions hourly. /compact at milestones handles within-session context.

## Notes

Parked, architecture already provides this.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `done` | Parked — already solved by cron architecture |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-04-02-session-isolation-per-task` |
| Channel | nb |
| Video | [Your Claude Limit Burns In 90 Minutes Because Of One ChatGPT Habit.](https://www.youtube.com/watch?v=5ztI_dbj6ek) |
| Published | 2026-04-02 |
| Ingested upstream | 2026-04-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

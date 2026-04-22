# Implement Claude Code Routines for Scheduled Autonomous Dev Tasks

> Back to [[experiments-index]]

Source: **[Claude Code Just Dropped Routines. 24/7 Agents.](https://www.youtube.com/watch?v=ehg4fhydTgs)** · NateHerk · 2026-04-16

**Status:** `deferred` · **Verdict:** `deferred` · **Effort:** `medium`

---

## Hypothesis

If we configure Claude Code Routines to run recurring autonomous tasks (e.g., nightly test runs, dependency update PRs, doc generation), then we will offload low-cognition maintenance work from synchronous dev sessions, because Routines provides a native cron-like scheduler that keeps the agent context warm between runs.

## What they did

Speaker demonstrates the newly released Claude Code Routines feature, which allows scheduling agent tasks at defined intervals without manual invocation. Shows setup of a 24/7 monitoring and maintenance agent that runs code checks, generates summaries, and opens PRs on a schedule. Walks through the Routines configuration syntax and how to scope permissions safely.

## Relevance to YOLO loop

High relevance — Routines could automate the maintenance and monitoring phases of the YOLO loop, freeing human attention for creative/architectural decisions while keeping the repo healthy around the clock.

## Notes

Duplicates what GitHub Actions already gives us for scheduling. Low differentiation.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-16 | `backlog` | Extracted from YouTube RSS |
| 2026-04-22 | `deferred` | Duplicates what GitHub Actions already gives us for scheduling. Low differentiation. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-04-16-claude-code-routines-scheduler` |
| Channel | NateHerk |
| Video | [Claude Code Just Dropped Routines. 24/7 Agents.](https://www.youtube.com/watch?v=ehg4fhydTgs) |
| Published | 2026-04-16 |
| Ingested upstream | 2026-04-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

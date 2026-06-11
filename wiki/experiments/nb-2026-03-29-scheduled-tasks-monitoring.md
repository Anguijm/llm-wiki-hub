# Use Claude Scheduled Tasks for automated recurring work

> Back to [[experiments-index]]

Source: **[Anthropic Just Gave You 3 Tools That Work While You're Gone](https://www.youtube.com/watch?v=3e7gmNPr5Vo)** · nb · 2026-03-29

**Status:** `done` · **Verdict:** `discard` · **Effort:** `low`

---

## Hypothesis

If we set up Claude Scheduled Tasks for recurring monitoring (e.g., daily test runs, dependency checks, competitor analysis), then we reduce manual overhead and catch issues earlier because the agent works asynchronously while we focus on building.

## What they did

Nate described Anthropic using Scheduled Tasks internally to keep Go and Python code libraries in sync silently. Non-dev use cases include morning AI news briefings and monitoring flight prices.

## Actionable steps

- Identify 2-3 recurring tasks in the YOLO loop (e.g., daily test suite runs, learnings review)
- Set up Claude Scheduled Tasks with repo + schedule + prompt
- Evaluate whether async results reduce manual overhead after 1 week

## Success metric

At least one recurring task fully automated with no manual intervention needed.

## Relevance to YOLO loop

The YOLO loop has recurring work (test runs, dashboard updates, learnings review) that could run autonomously on a schedule.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

The YOLO loop already uses cron for scheduled work (Phase 2 refinement ran on 30-min cron). Claude Scheduled Tasks would add a second scheduling layer without clear benefit. The cron approach is simpler and already proven. Discard in favor of existing cron infrastructure.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-03-29 | `done` | Evaluated: cron already serves this role. Scheduled Tasks would be redundant. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-03-29-scheduled-tasks-monitoring` |
| Channel | nb |
| Video | [Anthropic Just Gave You 3 Tools That Work While You're Gone](https://www.youtube.com/watch?v=3e7gmNPr5Vo) |
| Published | 2026-03-29 |
| Ingested upstream | 2026-03-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

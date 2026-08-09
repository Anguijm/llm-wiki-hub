# Run Schedule- and Trigger-Based Background Agents for Proactive Production Health Tasks

> Back to [[experiments-index]]

Source: **[Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](https://www.youtube.com/watch?v=vSx5IULvBns)** · aie · 2026-08-09

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If background agents run on schedules and event triggers to perform proactive production tasks (health summaries, runbook updates, dependency checks), then the long tail of operational toil that consumes 70% of engineering time will be reduced without requiring humans to initiate each task.

## What they did

Smith described background agents as covering the 'long tail' of operational work beyond incident response. These agents run on cron-like schedules or event triggers, are composable, and can be configured conversationally (e.g., 'set up a weekly health summary for my team'). The agent explores the environment, asks clarifying questions, sets itself up, and shares results via Slack. He cited a survey finding that 70% of engineer time is spent on production operations (maintenance, debugging, on-call, hot fixes, escalations) rather than writing new code, motivating the need for agents to absorb this work.

## Relevance to YOLO loop

Maps to adding proactive background monitoring tasks to the YOLO loop's operational layer—agents that continuously validate deployed code health, surface regressions, and update operational docs without requiring human-initiated queries.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-09-background-scheduled-agents` |
| Channel | aie |
| Video | [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](https://www.youtube.com/watch?v=vSx5IULvBns) |
| Published | 2026-08-09 |
| Ingested upstream | 2026-08-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

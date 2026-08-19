# Implement a chief-of-staff agent that delegates to specialist sub-agents instead of routing tasks manually

> Back to [[experiments-index]]

Source: **[A Week of Grok Bot Lessons in 10 Mins](https://www.youtube.com/watch?v=TMPUUyQC5aM)** · nh · 2026-08-19

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we designate one primary agent as a chief-of-staff with explicit awareness of all specialist sub-agents and a delegation-first instruction set, then a user only needs to interact with one interface to access the full capability of a multi-agent system, because the chief agent selects and routes to the correct specialist automatically based on task type, returning consolidated results.

## What they did

Nate Herk showed his Grokbot setup where a 'Klaus' chief-of-staff agent is the only agent he directly messages. Klaus has a description instructing it to check whether a specialist sub-agent owns the task before acting itself. Specialist agents (researcher, content strategist, motion graphics, morning planner, financial) each have clear single-purpose descriptions. Nate demonstrated conversation logs showing Klaus delegating to sub-agents and returning results. He also showed: a 'grill me' skill that interviews the user to capture business context; screen-recorded skill teaching via computer use; scheduled routines running in Grok's cloud; and saved browser profiles so agents can act in authenticated web sessions without credentials being shared in chat.

## Relevance to YOLO loop

The chief-of-staff pattern is directly applicable to our YOLO loop orchestration layer: rather than hardcoding task routing logic, a chief agent with good sub-agent descriptions can dynamically route steps to the right specialist, making the loop easier to extend with new capabilities.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-19-grokbot-chief-of-staff-pattern` |
| Channel | nh |
| Video | [A Week of Grok Bot Lessons in 10 Mins](https://www.youtube.com/watch?v=TMPUUyQC5aM) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

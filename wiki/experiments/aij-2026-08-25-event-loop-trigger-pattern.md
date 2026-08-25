# Replace human-triggered agent prompts with event-based or goal-based loop triggers

> Back to [[experiments-index]]

Source: **[I don't prompt agents anymore...](https://www.youtube.com/watch?v=_9OT25ZvrWs)** · aij · 2026-08-25

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we replace manual human prompting of agents with automated triggers (time-based, goal-based, or event-based), then we can sustain continuous agent work without human bottlenecks because the agent wakes up autonomously when conditions are met and only escalates to humans when explicitly necessary.

## What they did

Jason described the shift AI-native companies are making from 'human prompts agent for every task' to loop-based patterns where a trigger prompts the agent. He gave three trigger types: time-based (e.g., every day pull latest GitHub issues and fix them), goal-based (e.g., continuously optimize front-end until performance increases 200%), and event-based (e.g., every incoming email wakes the agent). The key design decision for each loop is explicitly defining what the agent can do autonomously versus what must involve a human. He also described an orchestrator pattern where a human talks to an orchestrator agent that then delegates to specialist sub-agents, rather than the human prompting each agent individually.

## Relevance to YOLO loop

The YOLO loop currently requires manual invocation; this experiment suggests wiring event triggers (e.g., new GitHub issue created, test suite failure, PR comment) to automatically invoke the appropriate loop, with a defined human-escalation policy.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-25 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aij-2026-08-25-event-loop-trigger-pattern` |
| Channel | aij |
| Video | [I don't prompt agents anymore...](https://www.youtube.com/watch?v=_9OT25ZvrWs) |
| Published | 2026-08-25 |
| Ingested upstream | 2026-08-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

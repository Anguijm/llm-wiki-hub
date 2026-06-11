# Design a multi-agent pipeline that minimizes human checkpoints

> Back to [[experiments-index]]

Source: **[Getting Humans Out of the Way: How to Work with Teams of Agents](https://www.youtube.com/watch?v=ie1M8p-SVfM)** · mlops · 2026-05-03

**Status:** `deferred` · **Effort:** `high`

---

## Hypothesis

If we restructure agent workflows to push human approval gates to the edges (start and end) rather than inline, then throughput will increase and task completion latency will drop because agents can resolve ambiguity among themselves without blocking on human input.

## What they did

Speaker outlined an architecture and coordination patterns for teams of agents designed to reduce human-in-the-loop intervention during execution, focusing on how agents can negotiate, delegate, and self-correct without escalating to humans.

## Relevance to YOLO loop

Directly addresses YOLO loop autonomy: if we can reduce mid-loop human interrupts in our own Claude Code pipelines, we increase the 'YOLO' factor and get longer unattended runs.

## Notes

[2026-05-06T19:43:19Z] DEFER: Thought-piece on agent autonomy. Needs a concrete metric (e.g., 'human interrupts per build') before it's actionable.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-03 | `backlog` | Extracted from YouTube RSS |
|  | `` | Triage 2026-05-05: Thought-piece on agent autonomy. Needs a concrete metric (e.g., 'human interrupts per build') before it's actionable. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-05-03-humans-out-of-way-agent-teams` |
| Channel | mlops |
| Video | [Getting Humans Out of the Way: How to Work with Teams of Agents](https://www.youtube.com/watch?v=ie1M8p-SVfM) |
| Published | 2026-05-03 |
| Ingested upstream | 2026-05-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

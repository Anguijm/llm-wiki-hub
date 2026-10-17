# Audit our Claude Code harness against the four harness primitives: file system, sub-agents, skills, and memory

> Back to [[experiments-index]]

Source: **[What is an Agent Harness?](https://www.youtube.com/watch?v=R0ckdFjUF5U)** · lc · 2026-10-16

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we audit our existing Claude Code setup against the four harness primitives (file system offload, sub-agent parallelisation, on-demand skills, and persistent memory), then we will identify which primitives are missing and causing context-window blowouts or task loss, because a harness missing any one of these forces the model to compensate by stuffing everything into context.

## What they did

LangChain's explainer defined an agent harness as the infrastructure layer that lets a model perceive, act, persist information, and enforce boundaries. The four named primitives: (1) file system to offload data out of context, (2) sub-agents for isolation and parallelisation, (3) skills loaded on demand, (4) enforced context boundaries. Absence of any primitive causes context-window overflow and task derailment.

## Relevance to YOLO loop

high: directly maps to our Claude Code harness design—running this four-primitive audit against our current setup is an immediate actionable task.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `lc-2026-10-16-agent-harness-explainer` |
| Channel | lc |
| Video | [What is an Agent Harness?](https://www.youtube.com/watch?v=R0ckdFjUF5U) |
| Published | 2026-10-16 |
| Ingested upstream | 2026-10-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

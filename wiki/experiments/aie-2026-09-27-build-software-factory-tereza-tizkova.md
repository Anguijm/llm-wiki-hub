# Implement a task-decomposition and agent-dispatch layer modeled on factory production planning

> Back to [[experiments-index]]

Source: **[What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory](https://www.youtube.com/watch?v=vGCJ7diEtrw)** · aie · 2026-09-27

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we build an explicit planning layer that decomposes software tasks into standardized work units before dispatching to coding agents, then we achieve more predictable and parallelizable output because factory-style production planning reduces variance in agent task scope.

## What they did

Tereza Tížková from Factory described the concrete infrastructure and organizational practices required to actually build a functioning software factory—task decomposition, agent dispatch, quality control, and iteration loops—based on their production experience.

## Relevance to YOLO loop

Directly relevant: describes the scaffolding around an agentic loop that makes it production-grade. The task decomposition and dispatch layer she describes is a more formal version of how we scope tasks before YOLO loop runs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-27-build-software-factory-tereza-tizkova` |
| Channel | aie |
| Video | [What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory](https://www.youtube.com/watch?v=vGCJ7diEtrw) |
| Published | 2026-09-27 |
| Ingested upstream | 2026-09-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

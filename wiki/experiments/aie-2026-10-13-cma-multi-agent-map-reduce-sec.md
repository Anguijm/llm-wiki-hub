# Implement a map-reduce agent pattern where a coordinator dispatches sub-agents per entity and aggregates results

> Back to [[experiments-index]]

Source: **[Build a Research Agent with Claude Managed Agents (Part 2 of 4) — Anthropic](https://www.youtube.com/watch?v=FGftGOzfohc)** · aie · 2026-10-13

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we build a coordinator agent that dispatches per-entity sub-agent sessions (e.g., one per stock ticker) and then aggregates their outputs, then we can parallelize long-running research tasks and keep the main session responsive, because Anthropic's workshop demo showed the main session remaining idle and interactable while sub-agents ran SEC filing analysis concurrently.

## What they did

Gabe Semach walked through building a financial research agent using Claude Managed Agents. The architecture progressed from a simple chat agent → multi-agent with sub-agents → async long-running tasks → map-reduce. In the map-reduce pattern, the main coordinator agent receives a query (e.g., 'analyze Google and Microsoft'), dispatches individual sessions per ticker with SEC-filing skills, each sub-session uses outcome definition for self-supervision and memory stores for cross-session learning, and results are aggregated. The main thread remains idle and reachable while sub-agents work. Deployments API enables scheduling this on a recurring cadence (e.g., first of month at 1pm).

## Relevance to YOLO loop

For our dev loop, parallelizing sub-tasks (e.g., running evals or code review on multiple PRs simultaneously) via a coordinator + sub-agent pattern would reduce wall-clock time on batch jobs.

## Notes

Key API: Deployments endpoint takes agent definition + schedule + initial messages + resources (memory stores, GitHub repos). Custom tools on sub-agents allow the coordinator to stay free; sub-agent threads handle tool-result blocking independently.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-13-cma-multi-agent-map-reduce-sec` |
| Channel | aie |
| Video | [Build a Research Agent with Claude Managed Agents (Part 2 of 4) — Anthropic](https://www.youtube.com/watch?v=FGftGOzfohc) |
| Published | 2026-10-13 |
| Ingested upstream | 2026-10-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Implement Progressive MCP Tool Discovery to Prevent Context Bloat From Large Tool Registries

> Back to [[experiments-index]]

Source: **[MCP Doesn't Suck. Your Agent Does. — Jan Čurn, Apify](https://www.youtube.com/watch?v=pAnLpiAG6Es)** · aie · 2026-10-03

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we configure our MCP-connected agents to use progressive tool discovery (exposing only a search-tool initially, then loading specific tools into context on demand) rather than registering all available tools at session start, then context consumption and cost will decrease substantially while task performance remains equivalent, because agents typically need only one or two tools per task and pre-loading all tools wastes up to a third of the context window before any work begins.

## What they did

Jan Čurn of Apify argued that MCP criticism (context bloat, high cost, poor accuracy) is a harness problem, not a protocol problem. He outlined three solutions: (1) sub-agent delegation to isolate tool results from main context, (2) progressive tool discovery where a meta search-tool finds and loads specific tools only when needed, and (3) code-mode where tools are navigated as code rather than registered functions. He then demonstrated MCPC, their open-source MCP client that persists sessions across agent invocations, supports progressive tool discovery via a grep command, enables asynchronous task execution (agent starts a task, detaches, returns for results later), and shares session state across Claude Code and Codex. Connector evals showed MCPC and CLI performing comparably on cost and time while raw MCP consumed significantly more tokens.

## Relevance to YOLO loop

Directly addresses MCP scaling in our dev loop. If we use more than five MCP servers, pre-loading all tools is likely already degrading our agent performance. Switching to a progressive discovery pattern—or adopting MCPC as our MCP client—is a concrete architectural change with measurable token savings.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-03-apify-mcpc-progressive-tool-discovery` |
| Channel | aie |
| Video | [MCP Doesn't Suck. Your Agent Does. — Jan Čurn, Apify](https://www.youtube.com/watch?v=pAnLpiAG6Es) |
| Published | 2026-10-03 |
| Ingested upstream | 2026-10-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

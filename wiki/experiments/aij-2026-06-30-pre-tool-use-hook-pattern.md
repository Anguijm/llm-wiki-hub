# Use pre-tool-use hooks to silently augment default agent tool calls with richer context

> Back to [[experiments-index]]

Source: **[I was giving my coding agent context the wrong way...](https://www.youtube.com/watch?v=iWRmtPdFbGw)** · aij · 2026-06-30

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we attach a pre-tool-use hook that intercepts native tool calls (e.g. ripgrep) and appends graph or semantic metadata to the result before the model sees it, then the agent will receive enriched context without requiring a deliberate MCP tool invocation, reducing the chance the agent skips the richer retrieval path.

## What they did

Jason highlighted that most MCP tools fail because agents forget to call them. The codebase-memory MCP solves this by registering a pre-tool-use hook in Claude Code: when the agent fires a standard grep, the hook intercepts the call, runs a parallel graph query, and merges the graph data into the grep result transparently. The agent always gets augmented output even when it never explicitly calls the MCP tools.

## Relevance to YOLO loop

Generalizable design pattern for any MCP or tool wrapper in the YOLO loop. Any enrichment layer (memory lookup, project-rules injection, test-coverage data) can be silently grafted onto existing tool calls via hooks rather than requiring prompt engineering to make the agent remember to call a separate tool.

## Notes

Hook API available in Claude Code and Codex. Pattern is transferable to any agent framework that exposes pre/post tool lifecycle events.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-30 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aij-2026-06-30-pre-tool-use-hook-pattern` |
| Channel | aij |
| Video | [I was giving my coding agent context the wrong way...](https://www.youtube.com/watch?v=iWRmtPdFbGw) |
| Published | 2026-06-30 |
| Ingested upstream | 2026-06-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

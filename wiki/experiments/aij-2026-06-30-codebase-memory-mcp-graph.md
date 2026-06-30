# Replace flat-file grep with codebase-memory MCP graph for agent context

> Back to [[experiments-index]]

Source: **[I was giving my coding agent context the wrong way...](https://www.youtube.com/watch?v=iWRmtPdFbGw)** · aij · 2026-06-30

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we index the codebase into a relationship graph via the codebase-memory MCP and let the agent use graph-traversal tools (search_graph, trace_path, get_architecture) instead of raw ripgrep, then token consumption will drop ~50% and the agent will identify more complete blast-radius impact because it follows typed edges rather than loading full file contents.

## What they did

Jason installed the codebase-memory MCP (written in C/C++ for speed, no LLM pipeline) into Claude Code. It indexed his repo in seconds, extracted functions/classes/methods into a relationship graph, and exposed tools like get_architecture, search_graph, trace_path, and detect_change. He also used the pre-tool-use hook so that even when the agent defaulted to ripgrep, the hook augmented the result with graph data automatically. He compared token usage on the same codebase-investigation task: ~11k tokens with MCP vs ~38k without for the first query, and ~33k vs ~64k for a follow-up trace query.

## Relevance to YOLO loop

Directly reduces context-window bloat during any agent-driven code-change task in the YOLO loop. The pre-tool-use hook pattern is a drop-in for Claude Code / Codex and would benefit PR review, dependency tracing, and refactor planning without changing the outer loop orchestration.

## Notes

GitHub: search 'AI builder club' or check video description. Install flag: --with-ui adds a graph visualisation web UI on a local port. Particularly valuable for mono-repo or multi-ripple projects.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-30 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aij-2026-06-30-codebase-memory-mcp-graph` |
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

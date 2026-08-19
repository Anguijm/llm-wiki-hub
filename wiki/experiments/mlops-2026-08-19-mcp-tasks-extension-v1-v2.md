# Migrate MCP tool servers from blocking calls to Tasks v2 async pattern

> Back to [[experiments-index]]

Source: **[The MCP Tasks Extension](https://www.youtube.com/watch?v=dSoXxTqHJv0)** · mlops · 2026-08-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we retrofit existing synchronous MCP tool servers to support the Tasks v2 async protocol (task creation returns immediately, client polls or receives push notifications, cancellation is explicit), then long-running tool calls will no longer block connections or time out, and clients without task support will automatically fall back to blocking behavior, because the v2 spec includes graceful degradation for non-task-capable clients.

## What they did

Vikram Wasani compared MCP Tasks v1 (8-step lifecycle, mixed blocking/polling, client-server capability negotiation at three levels) with the streamlined Tasks v2 spec. He live-demoed a server implementing v2: task creation returns a task ID immediately; the client polls for status; cancellation is available but not guaranteed; clients that don't advertise task capability receive a blocking call transparently; old v1 clients attempting task/result calls receive an explicit error. Key v2 improvements: genuinely stateless, strict read/write separation, task list endpoint removed (security improvement), no backward compatibility with v1.

## Relevance to YOLO loop

Any MCP server we build or depend on for agentic steps should be evaluated against this pattern; migrating to Tasks v2 prevents timeout failures in our loop when tool calls involve multi-step or human-in-the-loop operations.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-08-19-mcp-tasks-extension-v1-v2` |
| Channel | mlops |
| Video | [The MCP Tasks Extension](https://www.youtube.com/watch?v=dSoXxTqHJv0) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

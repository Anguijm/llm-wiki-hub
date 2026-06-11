# Return sandboxed interactive HTML iframes from MCP tool calls to replace text-only agent responses with rich UI

> Back to [[experiments-index]]

Source: **[Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub](https://www.youtube.com/watch?v=_xIwFcnHqp4)** · aie · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If an MCP server tool returns a resource reference pointing to a server-generated HTML app alongside its normal tool result, then VS Code (as MCP host) will render that HTML in a sandboxed iframe directly in the chat window, enabling interactive data exploration (charts, flame graphs, diagrams) without additional round-trips, because the MCP apps protocol allows hosts to fetch and render UI resources separate from the client/LLM layer.

## What they did

Marlene Mhangami and Liam Hampton from Microsoft/GitHub explained and demoed MCP apps, a VS Code extension of the MCP protocol. When a tool call result includes a UI resource reference (an HTML element stored server-side), VS Code fetches it and renders it in a sandboxed iframe inside the chat panel. The app can call back to the MCP server for fresh data, enabling live interaction. Liam demoed a Go profiler MCP server that bundles and profiles a Go app, returns JSON flame graph data, and the React-based MCP app renders an interactive flame graph in the chat—eliminating the need to copy/paste profiler output back to the LLM. The iframe sandbox prevents the app from accessing VS Code internals or external APIs.

## Relevance to YOLO loop

If we build internal MCP servers for our dev loop (e.g. eval dashboards, trace viewers, diff explorers), returning interactive HTML via MCP apps would let developers inspect results without leaving the chat context—tightening the feedback loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-11-mcp-apps-rich-ui-in-chat` |
| Channel | aie |
| Video | [Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub](https://www.youtube.com/watch?v=_xIwFcnHqp4) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

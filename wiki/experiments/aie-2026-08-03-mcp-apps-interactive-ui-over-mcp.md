# Embed Interactive MCP App UI into Agent Tool Responses

> Back to [[experiments-index]]

Source: **[MCP Apps: Extending the Frontier — Ido Salomon & Liad Yosef](https://www.youtube.com/watch?v=-jY2T2PiJBE)** · aie · 2026-08-03

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we return HTML-based interactive UI from an MCP tool response instead of plain text, then users will be able to act on structured data directly inside the chat interface, because MCP apps standardize a two-way communication protocol between the rendered UI and the host agent.

## What they did

Ido and Liad described MCPUI / MCP apps, an open protocol extension to MCP that lets servers return HTML (or declarative UI) as a resource, which the host renders as an interactive iframe-style application. They showed examples where clicking a button inside the rendered UI triggers a standardized message back to the host, which can then call another MCP tool (e.g., favoriting a Spotify track). They noted Claude, ChatGPT, Cursor, and GitHub Copilot already support it, and that ChatGPT apps are built on this spec. They also previewed 'view tools' where the host/chat can programmatically fill out forms inside the rendered app.

## Relevance to YOLO loop

In our dev loop, tool call responses are currently plain text or JSON printed into the context window. Upgrading any frequently-used tool (e.g., test results, diff views, search results) to return an MCP app HTML resource would let the operator interact with output directly rather than issuing follow-up text commands, tightening the feedback loop.

## Notes

Spec repo referenced as 'X apps repo' on MCP website. Protocol is officially backed by Anthropic and OpenAI. View-tools (host→app direction) imminent but not yet released at time of talk. Worth checking mcpapps spec for current stability before building.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-03-mcp-apps-interactive-ui-over-mcp` |
| Channel | aie |
| Video | [MCP Apps: Extending the Frontier — Ido Salomon & Liad Yosef](https://www.youtube.com/watch?v=-jY2T2PiJBE) |
| Published | 2026-08-03 |
| Ingested upstream | 2026-08-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

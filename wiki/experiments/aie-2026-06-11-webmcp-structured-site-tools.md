# Expose site capabilities as Web MCP tools to replace brittle DOM-scraping agent flows

> Back to [[experiments-index]]

Source: **[The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google](https://www.youtube.com/watch?v=ghJmWQCIHRM)** · aie · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we define structured MCP tools on a web interface instead of letting agents infer actions from the DOM, then agent task completion rate increases and token cost drops because the agent receives a deterministic action menu instead of parsing HTML, accessibility trees, and screenshots.

## What they did

Google Chrome DevRel demoed Web MCP, a proposed web standard that lets developers declare named tools (e.g. search_concerts, purchase_ticket) directly on a page. A Chrome extension inspector lists available tools per page. Gemini in Chrome calls these tools sequentially instead of scraping the DOM, completing multi-step flows (find concert → open page → buy tickets) with three clean tool calls and UI kept in sync. Setup requires Chrome Canary v146+, an experimental flag, and the MCP inspector extension.

## Relevance to YOLO loop

If our dev loop involves agents driving web UIs or internal dashboards, replacing screenshot/DOM scraping with declared MCP tools would make those steps faster, cheaper, and more reliable.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-11-webmcp-structured-site-tools` |
| Channel | aie |
| Video | [The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google](https://www.youtube.com/watch?v=ghJmWQCIHRM) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

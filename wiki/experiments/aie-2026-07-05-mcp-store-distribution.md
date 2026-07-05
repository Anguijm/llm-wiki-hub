# Publish an MCP app with UI widgets to Claude and ChatGPT stores for dynamic discovery

> Back to [[experiments-index]]

Source: **[MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc](https://www.youtube.com/watch?v=sAOBXCDiDOs)** · aie · 2026-07-05

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we package an existing MCP server as an MCP app (returning sandboxed iframe UI widgets alongside JSON) and submit it to the Claude and ChatGPT MCP stores, then the agent will surface our tool organically to high-intent users via dynamic registry discovery, because Claude already searches the MCP registry when it lacks a tool for an assigned task, meaning listed apps receive unprompted routing from active users without requiring explicit configuration.

## What they did

Pietro explained the MCP app primitive: an MCP server that returns sandboxed iframe UI components instead of (or alongside) JSON, with bidirectional communication between the iframe and the host application. He traced the timeline from MCP launch (2024) through MCP UI proposals, ChatGPT's App SDK, and the opening of Claude's Connectors store and Character AI's store to general submissions (previously gated to design partners). He described Manifold's cloud tooling: ship from GitHub repo, run automated submission checks matching what each client store requires, auto-generate screenshots and test cases, and get a one-click install URL. The critical discovery mechanism is that Claude performs dynamic MCP registry search when it lacks a tool for a task—meaning a listed connector can be routed to organically by Claude on behalf of users who never explicitly installed it. ChatGPT is expected to follow. Pietro reported that store listing drove significant traffic to Manifold.

## Relevance to YOLO loop

If the yolo-loop produces tools or capabilities worth exposing externally, packaging them as MCP apps and listing in stores creates a distribution channel where the model itself becomes the discovery mechanism. The bidirectional iframe pattern also suggests a way to surface loop status or approval UIs directly inside Claude/ChatGPT sessions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-05 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-05-mcp-store-distribution` |
| Channel | aie |
| Video | [MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc](https://www.youtube.com/watch?v=sAOBXCDiDOs) |
| Published | 2026-07-05 |
| Ingested upstream | 2026-07-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

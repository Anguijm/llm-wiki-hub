# Implement ACP (Agent Client Protocol) transport so any client can drive any harness

> Back to [[experiments-index]]

Source: **[The Universal Remote Control for AI — Alex Hancock, Block](https://www.youtube.com/watch?v=YkNulwcc5jk)** · aie · 2026-09-09

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we add ACP support to our agent harness, then any compliant client (editor, desktop app, mobile, headless script) can send tasks and receive streaming updates from that harness without bespoke integration because ACP provides a standard JSON-RPC message layer with both local stdio and remote HTTP/WebSocket transports.

## What they did

Alex Hancock (Block/Goose) described ACP — a protocol originally proposed by Zed and JetBrains editors so a single client implementation could control any agent harness. The Goose team extended it beyond editors, specifying an HTTP transport and WebSocket upgrade for remote deployments. He live-demonstrated two different clients (including one coded the night before) simultaneously connecting to the same Goose agent process, receiving identical tool-call notifications and streaming text responses. He framed the agentic stack as four movable components (client, harness, tools/MCP, model) and argued that ACP + MCP remote transports together allow each component to live on any machine.

## Relevance to YOLO loop

Directly addresses the client↔harness interface in our dev loop. Adopting ACP would let us swap or multiply front-end clients (CLI, IDE plugin, web UI) against the same running agent backend without rewriting integration code, and enables remote harness deployments behind an HTTP endpoint.

## Notes

ACP site linked in talk. Goose is donated to Linux Foundation. Rust SDK maintained by speaker. Custom methods convention: prefix with underscore, allowing ecosystem-driven protocol evolution. Worth pairing with MCP remote transport experiment.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-09-acp-universal-agent-client-protocol` |
| Channel | aie |
| Video | [The Universal Remote Control for AI — Alex Hancock, Block](https://www.youtube.com/watch?v=YkNulwcc5jk) |
| Published | 2026-09-09 |
| Ingested upstream | 2026-09-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Deploy MCP Servers Behind a Load Balancer Using Stateless Protocol + DB-Backed Session Tokens

> Back to [[experiments-index]]

Source: **[MCP Goes Stateless | ​John Dellenbaugh & Pankaj Kumar | MCP Release Party - Seattle](https://www.youtube.com/watch?v=banffxk7EqQ)** · mlops · 2026-08-18

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run multiple stateless MCP server instances behind a standard load balancer and store all session state in a shared database keyed by a token passed in each request, then any instance can handle any request without sticky routing, because the protocol no longer maintains in-process session memory.

## What they did

John Dellenbaugh and Pankaj Kumar demonstrated the new stateless MCP spec (released 2026-07-28) using a shopping-cart agent scenario. Under the old protocol, session state lived in each server instance's local memory, so requests routed to a different instance returned 'session not found' errors. Their demo ran two MCP server instances behind a load balancer with a shared Postgres database holding cart state. Each tool call included a token identifying the cart; any instance could look up the state from the DB. They showed the old protocol failing on scale-out and the new stateless approach succeeding with no sticky routing required.

## Relevance to YOLO loop

If our dev loop MCP servers need to scale beyond a single process or survive restarts, this pattern is the baseline architecture. Migrating to stateless transport + shared DB eliminates the single-process bottleneck and makes deployments restartable without losing agent context.

## Notes

The spec change removes protocol-level sessions entirely—no handshake, no session ID negotiation. Application-level state (like cart ID) still needs an explicit token passed by the client. New MCP Inspector now supports both legacy and modern protocol eras for testing.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-08-18-stateless-mcp-horizontal-scale` |
| Channel | mlops |
| Video | [MCP Goes Stateless | ​John Dellenbaugh & Pankaj Kumar | MCP Release Party - Seattle](https://www.youtube.com/watch?v=banffxk7EqQ) |
| Published | 2026-08-18 |
| Ingested upstream | 2026-08-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

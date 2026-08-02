# Implement durable MCP task handles for long-running tool calls using Temporal workflows

> Back to [[experiments-index]]

Source: **[MCP Tasks (async): Why Aren't Any Agents Supporting Them? — Cornelia Davis, Temporal](https://www.youtube.com/watch?v=s4r6nk5WsZw)** · aie · 2026-08-02

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we back MCP tool calls with Temporal workflows that return a task handle instead of a synchronous response, then agents can invoke long-running operations (invoice processing, human-in-the-loop approvals, multi-step ERP workflows) without blocking or losing state across network blips, crashes, or human delays, because Temporal's durable execution guarantees task survival through infrastructure failures.

## What they did

Cornelia Davis (Temporal) explained the MCP tasks specification — an experimental extension allowing MCP tools to be long-running and asynchronous. Instead of request-response, the client gets a handle and can poll or receive notifications. She demoed a purchase order workflow: receive PO → record goods → parallel back-office updates + invoice processing via MCP tool → human-in-the-loop approval → ERP reconciliation. The MCP server implementing invoice processing is backed by a Temporal workflow, which provides durability (tasks survive crashes, network blips, humans going on vacation). She covered V1 spec issues (FIFO limitation on concurrent input-required tasks, ugly client-server protocol) and previewed V2 (cleaner protocol, coming July). She noted the spec mandates task durability and client-side task ID persistence. Code and Docker environments available in her Git repo.

## Relevance to YOLO loop

YOLO loop agents currently fail silently on long-running tool calls. This pattern enables MCP tools that can span minutes-to-hours without the agent polling in a busy loop or losing context on restart — critical for real production agentic workflows.

## Notes

V2 MCP tasks spec releasing July 2026. V1 has FIFO limitation. Temporal workflow provides durability layer. Demo code available via QR/Git repo mentioned in talk. Fast-MCP integration planned within 1-2 months.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-02-mcp-tasks-async-durable` |
| Channel | aie |
| Video | [MCP Tasks (async): Why Aren't Any Agents Supporting Them? — Cornelia Davis, Temporal](https://www.youtube.com/watch?v=s4r6nk5WsZw) |
| Published | 2026-08-02 |
| Ingested upstream | 2026-08-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

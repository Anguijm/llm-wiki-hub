# Use Cloudflare Durable Objects as stateful, addressable compute units for long-running AI agents

> Back to [[experiments-index]]

Source: **[Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carey, Cloudflare](https://www.youtube.com/watch?v=SKDJo2CopRs)** · aie · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we back AI agents with Cloudflare Durable Objects (stateful serverless) instead of stateless functions plus an external database, then we will reduce latency, simplify resumability across sessions/tabs, and enable background scheduling natively, because each Durable Object instance maintains in-process state, a built-in SQLite store, and can hibernate between requests while preserving identity.

## What they did

Matt Carey and Sunil Pai from Cloudflare described their agents.cloudflare.com platform built on Durable Objects. They explained that a Durable Object is a class that spins up once per ID and receives all future requests and WebSocket connections for that ID, giving stateful serverless semantics (scales globally, hibernates, persists state). They argued this is the ideal compute unit for agents: addressable, long-running, background-schedulable, and persistent. They demonstrated the AI SDK backend integration, MCP server hosting via Durable Objects, and a 'code mode' that bundles and executes dynamic worker code with NPM dependency caching via Cloudflare's CDN.

## Relevance to YOLO loop

If we deploy agents that need to run background tasks, maintain per-session state, or support resumable multi-turn interactions, Durable Objects offer a simpler architecture than managing external state stores. Worth prototyping for our agent loop persistence layer.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-11-eval-as-compute-primitive` |
| Channel | aie |
| Video | [Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carey, Cloudflare](https://www.youtube.com/watch?v=SKDJo2CopRs) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

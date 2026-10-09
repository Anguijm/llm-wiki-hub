# Build an API context graph grounded in source code to give coding agents cross-service awareness

> Back to [[experiments-index]]

Source: **[We Mapped 115 Microservices for Our Coding Agents — Kamalakannan Nandagopal, Postman](https://www.youtube.com/watch?v=k2ClBT4aqAg)** · aie · 2026-10-09

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we construct a centralized context graph that maps every microservice endpoint down to its exact line of implementation, cross-service call chains, and data flows to databases/caches, then coding agents will produce correct cross-service changes and catch dependency issues that single-repo context misses because agents are only as good as the context they receive.

## What they did

Kamal (Postman staff engineer) described building an API context graph across 150+ microservices and thousands of REST endpoints. Every data point is grounded in a hard truth: a line of code or a verifiable artifact, not LLM-generated docs. Steps: catalog every microservice in production, identify every endpoint and its exact implementation line, map inter-service calls and endpoint-to-endpoint connections, track data flow to databases and caches, map frontend/CLI/API interactions to backend. All data indexed via LLM into a centralized context layer. Results: agents could now answer architecture-wide questions impossible from a single repo; a 21-page engineering report surfaced dependency cycles, risky long-running migrations, single points of failure, telemetry blind spots. 75% of PRs in top-10 repos had API surface effects, validating the graph's relevance. Future work: adding semantic business-domain reasoning and 'why does this API exist vs. others' rationale.

## Relevance to YOLO loop

High relevance: building a source-grounded context graph for our own service topology would let YOLO loop agents make cross-service changes safely and surface architectural debt automatically.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-09-api-context-graph-coding-agents` |
| Channel | aie |
| Video | [We Mapped 115 Microservices for Our Coding Agents — Kamalakannan Nandagopal, Postman](https://www.youtube.com/watch?v=k2ClBT4aqAg) |
| Published | 2026-10-09 |
| Ingested upstream | 2026-10-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

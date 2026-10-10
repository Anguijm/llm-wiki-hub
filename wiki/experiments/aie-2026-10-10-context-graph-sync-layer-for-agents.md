# Build a tiered context graph with live MCP lookups for simple queries and synced vector cache for semantic/analytical queries

> Back to [[experiments-index]]

Source: **[Why Your Company Needs a Context Graph (and How to Build It) — Gil Feig, Merge](https://www.youtube.com/watch?v=cSz7aL2nl2U)** · aie · 2026-10-10

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we separate agent data access into live MCP lookups (for simple, bounded queries like a specific Stripe customer) and a locally synced, vectorized cache (for semantic or cross-dataset analytical queries), then agent reliability and answer quality improve significantly, because live APIs don't support semantic search and will timeout on large dataset traversals, while synced copies enable efficient hybrid retrieval.

## What they did

Gil Feig argued that MCP alone is insufficient for production agent context because underlying SaaS APIs don't expose semantic endpoints and can't handle queries like 'which customers were upset in the last year' without timing out. He proposed a four-tier context graph: (1) live MCP lookups for simple/bounded queries, (2) synced/cached copies in a vector DB for semantic/analytical queries, (3) memories formed during agent sessions, and (4) skills (documented company processes). He also stressed traceability: always store where data came from, when it was fetched, under what permissions, whether it was transformed, and what should invalidate it. Example: answering 'give me a status update on Acme including renewal risk' requires combining CRM live lookup + cached ticketing data + derived summary stored back to cache.

## Relevance to YOLO loop

Our YOLO loop agents likely query external tools via MCP. If any query requires cross-dataset analysis (e.g., 'which PRs failed CI this quarter?'), we need a sync layer. This architecture clarifies when to add a vector cache vs. keep live lookups, preventing silent timeout failures in production agents.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-10-context-graph-sync-layer-for-agents` |
| Channel | aie |
| Video | [Why Your Company Needs a Context Graph (and How to Build It) — Gil Feig, Merge](https://www.youtube.com/watch?v=cSz7aL2nl2U) |
| Published | 2026-10-10 |
| Ingested upstream | 2026-10-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Use a Storage-First Vector DB (turbopuffer) for Long-Tail Cold Indexes to Cut Search Infrastructure Cost

> Back to [[experiments-index]]

Source: **[Connect AI to Billions of Legal Documents — Simon Eskildsen, turbopuffer & Jacob Lauritzen, Legora](https://www.youtube.com/watch?v=V-isu4eTHgw)** · aie · 2026-09-16

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use a storage-first vector database that keeps cold indexes on SSD rather than in DRAM (e.g., turbopuffer) for workloads with many infrequently-queried indexes, then infrastructure costs will be substantially lower than always-in-memory solutions while maintaining acceptable latency for cold queries, because most enterprise projects are queried rarely after completion.

## What they did

Jacob (Legora) and Simon (turbopuffer) described Legora's evolution of search infrastructure from single ElasticSearch → multi-region ElasticSearch → per-tenant Postgres+pgvector → turbopuffer. The key insight was that Legora has 70-200+ tenants, many of which are closed projects that are rarely queried (long-tail cold indexes). Postgres with pgvector was expensive and broke at scale. Turbopuffer stores vectors on SSD with a memory hierarchy where cluster centroids stay in DRAM and leaves are fetched from SSD with a single 1ms round trip. Simon explained the architecture as a B-tree over vector space, making it the cheapest possible storage topology for databases with many cold partitions. This allowed Legora to handle per-tenant physical isolation, customer-managed encryption keys, and data residency (EU/US/APAC) natively without managing separate database clusters.

## Relevance to YOLO loop

If our dev loop maintains many per-project or per-user code context indexes where most are queried infrequently, a storage-first vector DB reduces the cost of keeping all those indexes warm. Relevant for scaling a multi-tenant coding assistant or code search system.

## Notes

Turbopuffer uses SSD-first storage with DRAM for hot centroids; single 1ms SSD round trip for cold leaf nodes. Supports both vector and full-text (BM25) search natively. Key trade-off: slightly higher latency for cold queries vs always-in-memory solutions, but dramatically cheaper at scale with many cold indexes.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-16-turbopuffer-cold-index-cost` |
| Channel | aie |
| Video | [Connect AI to Billions of Legal Documents — Simon Eskildsen, turbopuffer & Jacob Lauritzen, Legora](https://www.youtube.com/watch?v=V-isu4eTHgw) |
| Published | 2026-09-16 |
| Ingested upstream | 2026-09-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

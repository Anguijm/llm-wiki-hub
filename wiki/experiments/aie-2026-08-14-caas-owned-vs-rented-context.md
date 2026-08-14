# Calculate the Cost Tipping Point Between Renting AI Search Context vs Owning a Custom Knowledge Graph

> Back to [[experiments-index]]

Source: **[The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data](https://www.youtube.com/watch?v=Ot4OPrPH4xY)** · aie · 2026-08-14

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we model the per-query cost of rented AI search (e.g., Exa, Tavily) against the amortized cost of building an owned, continuously-refreshed knowledge graph for a fixed entity set, then we will find a tipping point (likely well below 100k queries) beyond which owning is cheaper and compounds in value because rented context has no memory across queries while owned context is queried for free after setup.

## What they did

The speaker compared ad-hoc AI search (pay-per-query, always fresh, zero setup) against building a custom entity-structured knowledge graph (~1 week setup, ~$5k estimated cost). He showed that for a use case with ~15k entity queries, the owned approach already breaks even. For persistent, high-frequency, domain-specific retrieval needs the owned graph compounds: data decays but the graph is continuously refreshed, and repeated queries cost nothing marginal. He argued that frequency of retrieval is the key variable — if you ask the same question over and over, rented context will 'bite you in the ass.'

## Relevance to YOLO loop

The YOLO loop's retrieval stage currently likely uses ad-hoc search per query. If certain entity types (repos, PRs, docs, API schemas) are queried repeatedly, pre-building an owned indexed store (even a simple vector DB with scheduled refresh) would reduce per-loop latency and cost significantly.

## Notes

Speaker's data-decay chart showed that finance/news/retail data goes stale within 30 days, social media within hours. Refresh cadence for an owned graph must match the decay rate of the target domain.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-14-caas-owned-vs-rented-context` |
| Channel | aie |
| Video | [The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data](https://www.youtube.com/watch?v=Ot4OPrPH4xY) |
| Published | 2026-08-14 |
| Ingested upstream | 2026-08-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

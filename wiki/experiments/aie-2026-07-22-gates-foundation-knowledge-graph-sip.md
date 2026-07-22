# Build a Cross-System Semantic Knowledge Graph as the Agentic Retrieval Layer

> Back to [[experiments-index]]

Source: **[Your Moat Is Your Data Model — Mike Phipps, Gates Foundation](https://www.youtube.com/watch?v=jt1Pbr_n6oU)** · aie · 2026-07-22

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we model internal operational data as a semantic knowledge graph (rather than flat embeddings or siloed databases) and expose it to agents via MCP, then agents will return more precise, contextually grounded answers because graph traversal preserves entity relationships and domain rules that vector similarity search loses.

## What they did

Mike Phipps described the Gates Foundation's Strategic Intelligence Platform (SIP), rolled out to ~4,000 employees. They built a data lakehouse consolidating structured and unstructured data from siloed systems of record, added a semantic graph layer modeled around domain entities (grants, grantees, strategies, divisions, countries, disbursements), and exposed it to agents via Neo4j MCP servers (forked and modified to pass conversation IDs and message numbers back for state tracking). Evals were built per data-owner reporting standards, separated into complexity tiers, run against the live graph at runtime, with LLM-as-judge scoring pass@1 and stability. The eval feedback loop updated domain rules and schema descriptions to close ambiguity gaps. Key lesson: engage data owners early to capture tacit knowledge before modeling; the graph encoding of that tacit knowledge is the durable competitive moat regardless of which frontier model is current.

## Relevance to YOLO loop

Directly applicable to the YOLO loop's context/memory layer. Rather than embedding docs into a flat vector store, structuring the dev loop's knowledge (tasks, outcomes, dependencies, agent decisions) as a graph would enable agents to traverse causal chains and retrieve relevant prior experiment results with higher precision.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-22-gates-foundation-knowledge-graph-sip` |
| Channel | aie |
| Video | [Your Moat Is Your Data Model — Mike Phipps, Gates Foundation](https://www.youtube.com/watch?v=jt1Pbr_n6oU) |
| Published | 2026-07-22 |
| Ingested upstream | 2026-07-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

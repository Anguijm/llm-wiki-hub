# Implement a Three-Pillar Ontology Layer (Business + Technical + Execution Traces) to Enable Thin Cross-Agent Data Discovery

> Back to [[experiments-index]]

Source: **[Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j](https://www.youtube.com/watch?v=VGN22pPpb-8)** · aie · 2026-07-22

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we build a shared ontology layer with a business-facing concept graph, a technical metadata graph of all data sources, and a mapping between them augmented by agent execution traces, then individual agents can be thin (no hardcoded data wiring) and the system self-learns which data sources are reliable because execution traces score each data path's historical success rate.

## What they did

Emil Eifrem described a pattern validated across a Fortune 20 bank, a Bay Area tech platform, and a fintech company. Three pillars: (1) Business ontology — human-readable concepts and relationships (Customer has FirstName, not f_name) encoded in Neo4j; (2) Technical ontology — metadata of all enterprise data sources (Oracle DBs, Snowflake, S3, etc.) with schemas and locations; (3) A mapping layer connecting business concepts to technical data assets, plus agent execution traces (what was tried, was it successful, context, score). At runtime, agents query the ontology to discover relevant data sources rather than having them hardcoded in prompts/code. Execution traces feed back as Bayesian-style weights: if DMV lookup succeeds consistently in a given context, future agents in that context prefer it. This eliminates the DRY violation (a schema change cascades automatically) and enables cross-agent learning.

## Relevance to YOLO loop

Maps directly to the YOLO loop's need to scale from one agent to many without re-engineering data wiring each time. Encoding the loop's tool inventory (APIs, file paths, model endpoints) as a technical ontology and mapping it to task-type business concepts would let new sub-agents self-discover their tools and learn from prior agents' success/failure traces.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-22-thin-agents-ontology-semantic-layer` |
| Channel | aie |
| Video | [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j](https://www.youtube.com/watch?v=VGN22pPpb-8) |
| Published | 2026-07-22 |
| Ingested upstream | 2026-07-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

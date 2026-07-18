# Use schema-constrained structured outputs for graph extraction from unstructured text

> Back to [[experiments-index]]

Source: **[A Practitioner's Guide to Graphs - Tim Ainge, Good Collective](https://www.youtube.com/watch?v=3ySF0I5iE_0)** · aie · 2026-07-18

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we provide LLM extractors with an explicit typed schema (nodes, edge types, properties) rather than open-ended triple extraction, then the resulting knowledge graph will have consistent, queryable relationships because the model fills a well-defined structure instead of inventing arbitrary predicates.

## What they did

Tim Ainge demonstrated that naive subject-predicate-object triple extraction produces inconsistent graphs. By instead giving the agent a typed schema (e.g., Recipe → Ingredients → Quantity, Recipe → Steps → CookingTechnique) with ontology instructions (lowercase names, metric units), the output became immediately meaningful and queryable. He also showed embedding-based node deduplication for handling synonym variants at query time rather than requiring exhaustive pre-enumeration.

## Relevance to YOLO loop

Applicable when the YOLO loop needs to build or query a knowledge graph from code, docs, or logs; schema-first extraction would make graph context retrieval reliable rather than ad-hoc.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-18-schema-first-graph-extraction` |
| Channel | aie |
| Video | [A Practitioner's Guide to Graphs - Tim Ainge, Good Collective](https://www.youtube.com/watch?v=3ySF0I5iE_0) |
| Published | 2026-07-18 |
| Ingested upstream | 2026-07-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

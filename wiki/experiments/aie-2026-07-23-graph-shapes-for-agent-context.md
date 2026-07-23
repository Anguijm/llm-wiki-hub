# Model agent context as typed graph shapes (table-of-contents, connection, theme) rather than flat vector search

> Back to [[experiments-index]]

Source: **[AI on Your Lakehouse: Context Comes in Shapes, Not Queries — Zach Blumenfeld, Neo4j](https://www.youtube.com/watch?v=kRkcNOsRyYg)** · aie · 2026-07-23

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we pre-define named graph shapes that match the structure of questions our agents need to answer (hierarchical containment, cross-entity connection, pattern clustering), then agents will answer estate-level and relational questions more accurately because vector search can only find similar items while graph traversal can prove negatives, find patterns across all records, and correctly join lookalike schemas.

## What they did

Zach Blumenfeld presented a workshop on using Neo4j graph representations alongside structured data warehouses (BigQuery/Snowflake/Databricks) to give agents better context. He identified three query failure modes for large data estates: proving a negative (what documentation don't we have?), finding patterns across everything (what keeps failing?), and joining lookalike schemas correctly. His solution: define three concrete graph shapes before building the agent — a 'table of contents' tree for document containment, a 'connection' shape for structured data relationships, and a 'theme' shape for clustering patterns across records. Agents use these shapes as named traversal strategies rather than ad-hoc queries, making retrieval deterministic for the cases where semantic search is confidently wrong.

## Relevance to YOLO loop

Our yolo loop agents retrieve context via vector search or direct SQL. For tasks involving 'what's missing,' 'what pattern keeps repeating,' or 'how do these records relate,' graph shapes would dramatically improve answer quality. Even a lightweight graph representation of our codebase or task history using these three shapes could make agent planning more reliable.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-23-graph-shapes-for-agent-context` |
| Channel | aie |
| Video | [AI on Your Lakehouse: Context Comes in Shapes, Not Queries — Zach Blumenfeld, Neo4j](https://www.youtube.com/watch?v=kRkcNOsRyYg) |
| Published | 2026-07-23 |
| Ingested upstream | 2026-07-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

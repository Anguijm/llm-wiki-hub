# Build a persistent knowledge base of processed dataset results to prevent redundant expensive compute

> Back to [[experiments-index]]

Source: **[When Agents Meet Physical Data: The Other Physics of Agent Harnesses - Dmitry Petrov, DataChain](https://www.youtube.com/watch?v=bUJgirn4_yc)** · aie · 2026-07-20

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we store the outputs of expensive LLM/compute processing runs (schema, stats, source code, session context) as structured markdown knowledge base entries linked to source data, then agents and teammates can reuse prior results instead of recomputing, because the knowledge base provides the lineage and context needed to answer the same question without re-running the pipeline.

## What they did

Dmitry described building DataChain, an open-source data harness for unstructured physical data (video, sensor, robot telemetry). He demonstrated a coding agent (Claude Code) analyzing 91 dashcam video clips using a YOLO model in 24 minutes, then persisting results as a structured dataset. The knowledge base entry for each processed dataset contains: description, session context (why it was created), storage dependency path, data preview, schema, statistics, and crucially the source code used to produce it. He argued that without this memory layer, agents and humans repeat expensive compute jobs redundantly. The harness stack has: raw unstructured data in object storage → compute engine extracting metadata → dataset slices → knowledge base MD files → coding agents that consult the knowledge base before triggering new compute. He used Pydantic schemas as the unifying layer to avoid a SQL island in Python codebases.

## Relevance to YOLO loop

The YOLO loop repeatedly processes the same codebases and test suites. Persisting processed context (AST summaries, test result histories, dependency graphs) in a structured knowledge base that the agent checks before re-analyzing would eliminate redundant indexing work across sessions and enable incremental rather than full re-processing.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-20-physical-data-harness-knowledge-base` |
| Channel | aie |
| Video | [When Agents Meet Physical Data: The Other Physics of Agent Harnesses - Dmitry Petrov, DataChain](https://www.youtube.com/watch?v=bUJgirn4_yc) |
| Published | 2026-07-20 |
| Ingested upstream | 2026-07-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

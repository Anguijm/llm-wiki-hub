# Build a knowledge graph of organizational processes and train a retrieval agent to traverse it

> Back to [[experiments-index]]

Source: **[AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents](https://www.youtube.com/watch?v=l0FLhNqBOic)** · aie · 2026-07-28

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we extract business process knowledge into a structured knowledge graph and train an RL agent with custom tools to traverse it reliably, then agents can extract the right context for task execution, because frontier models fail at process understanding due to verbosity and inability to distinguish what clients actually care about from irrelevant detail.

## What they did

Varick Agents built an internal toolchain that (1) post-trains an open-source model (Kimi K2-6 mentioned) on normalized process flow writing to produce concise, client-relevant summaries rather than verbose frontier-model output, and (2) creates an RL environment with custom tools designed to traverse their knowledge graph — including tools to resolve person identity disambiguation (e.g., detecting that two 'Mikes' are the same person) and tools to detect redundancy cycles or DAG violations in the process graph.

## Relevance to YOLO loop

Directly relevant to context injection in our dev loop. When an agent needs to execute a task, it needs the right slice of organizational/codebase context. A traversal-trained retrieval agent would replace brittle RAG with structured graph navigation.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-28-varick-knowledge-graph-process-extraction` |
| Channel | aie |
| Video | [AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents](https://www.youtube.com/watch?v=l0FLhNqBOic) |
| Published | 2026-07-28 |
| Ingested upstream | 2026-07-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

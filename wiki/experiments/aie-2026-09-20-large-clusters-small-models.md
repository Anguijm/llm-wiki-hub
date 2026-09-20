# Scale embedding/small-model inference horizontally to unlock throughput gains

> Back to [[experiments-index]]

Source: **[Large clusters for small models — Daniel Svonava, Superlinked](https://www.youtube.com/watch?v=g4SsanB0gMc)** · aie · 2026-09-20

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we run small models (embeddings, rerankers, classifiers) on horizontally scaled clusters rather than single large instances, then we can achieve much higher throughput for vector search and routing tasks, because small models are compute-bound per token but embarrassingly parallel across requests.

## What they did

Daniel Svonava described Superlinked's approach of deploying large GPU clusters dedicated to small models — particularly embedding models — to achieve throughput at a scale that changes what retrieval and search architectures are feasible in production.

## Relevance to YOLO loop

If the YOLO loop uses retrieval-augmented generation or semantic routing, scaling the embedding layer independently could remove a retrieval bottleneck without changing the main LLM inference path.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-20-large-clusters-small-models` |
| Channel | aie |
| Video | [Large clusters for small models — Daniel Svonava, Superlinked](https://www.youtube.com/watch?v=g4SsanB0gMc) |
| Published | 2026-09-20 |
| Ingested upstream | 2026-09-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

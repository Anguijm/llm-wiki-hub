# Pre-tokenize model/artifact names at insert time into a denormalized read collection to keep search sub-100ms at scale

> Back to [[experiments-index]]

Source: **[Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub — Arek Borucki, Hugging Face](https://www.youtube.com/watch?v=lyL5QhgIOxc)** · aie · 2026-07-28

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we tokenize searchable identifiers (model names, file paths, artifact IDs) at write time and store them in a denormalized read-only collection separate from the source-of-truth collection, then search latency will remain consistently low as the catalog scales past millions of entries, because regex-based queries on the main collection do not scale and pre-tokenized arrays allow Apache Lucene-backed autocomplete indexes to operate efficiently.

## What they did

Arek Borucki described Hugging Face's migration from regex-based MongoDB queries on a main models collection (which broke at 3M models) to a two-collection architecture: a main repo collection for writes and a separate denormalized read collection where model names are pre-tokenized on insert (e.g., 'meta-llama/Llama-3.1-8B' becomes tokens ['meta', 'llama', '3', '1', '8b', etc.] stored in an array). Searches run against this read collection using MongoDB Atlas Search (Apache Lucene) with autocomplete. They also use replica sets to route complex aggregations, change streams, and ad hoc queries to secondaries, keeping the primary for strong-consistency writes only.

## Relevance to YOLO loop

Relevant if our dev loop includes any catalog search (model registry, tool library, artifact lookup). The pattern — denormalize at write time, search a read-optimized collection — is directly applicable to any agent that needs to search a growing catalog of artifacts or code patterns.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-28-huggingface-denormalized-read-collection-search` |
| Channel | aie |
| Video | [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub — Arek Borucki, Hugging Face](https://www.youtube.com/watch?v=lyL5QhgIOxc) |
| Published | 2026-07-28 |
| Ingested upstream | 2026-07-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Index Documents at Multiple Chunk Sizes and Fuse Results with RRF to Improve RAG Recall by 20-40%

> Back to [[experiments-index]]

Source: **[Stop Chunking Like It's 2022 — Yuval Belfer, AI21 Labs](https://www.youtube.com/watch?v=r9OwPx_HoV0)** · aie · 2026-09-16

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we index the same document corpus at multiple chunk sizes (e.g., 50, 100, 200, 500, 1000, 2000 tokens) and retrieve from all indexes in parallel, fusing results with Reciprocal Rank Fusion (RRF), then retrieval recall will improve by 20-40% over any single fixed chunk size because optimal chunk size is query-dependent and no single size dominates across query types.

## What they did

Yuval Belfer (AI21 Labs) presented research showing that chunking is lossy compression and no single chunk size is optimal across all queries. They duplicated a corpus six times with different chunk sizes, ran retrieval experiments on QMSum (meeting transcripts), NarrativeQA (novel Q&A), a Seinfeld trivia dataset, and FinanceBench, and showed that different queries within the same dataset prefer different chunk sizes. Their proposed method: index at all chunk sizes simultaneously, retrieve from each index per query, and aggregate using Reciprocal Rank Fusion (RRF) — a simple formula requiring no trained model. Results showed 20-40% recall improvement over the best single fixed chunk size across datasets, with no latency penalty (parallel retrieval) at the cost of 2-5x storage overhead.

## Relevance to YOLO loop

Our dev loop uses RAG for code context and documentation retrieval. Implementing multi-size indexing with RRF could substantially improve the quality of context retrieved for coding agents, especially for queries that span both fine-grained (function signatures) and coarse-grained (architectural decisions) content.

## Notes

RRF is a simple script, not a trained model. Storage overhead is 2-5x. Latency is not significantly affected because retrieval across indexes is parallelizable. Example code and Seinfeld dataset available on AI21 blog. Future work: determine optimal number and selection of chunk sizes rather than using arbitrary fixed set.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-16-multi-chunk-size-rrف` |
| Channel | aie |
| Video | [Stop Chunking Like It's 2022 — Yuval Belfer, AI21 Labs](https://www.youtube.com/watch?v=r9OwPx_HoV0) |
| Published | 2026-09-16 |
| Ingested upstream | 2026-09-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

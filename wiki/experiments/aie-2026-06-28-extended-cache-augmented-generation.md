# Distribute a rapidly-changing full-corpus across parallel CAG buckets with a supervisor model for global questions

> Back to [[experiments-index]]

Source: **[When All Context Matters: Extended Cache Augmented Generation - Luis Romero-Sevilla, Orbis](https://www.youtube.com/watch?v=XovaGv4f39A)** · aie · 2026-06-28

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we split a large, frequently-updated document collection across multiple parallel cache-augmented generation (CAG) buckets — each pre-loading a subset of documents into KV cache — and use a supervisor model to interrogate relevant buckets and synthesise answers, then we get better recall than simple RAG and faster recomputation than GraphRAG when data changes, because each bucket can be independently refreshed and queried in parallel rather than rebuilding a global knowledge graph.

## What they did

Luis described a scenario where all documents in a collection are relevant to answer global questions AND the collection changes frequently. He evaluated three approaches: (1) Simple RAG — fast to update but misses cross-document relationships; (2) GraphRAG — excellent at relationships but prohibitively expensive to recompute when data changes; (3) Extended CAG — split documents into balanced buckets (no domain ordering, to prevent the supervisor ignoring seemingly irrelevant buckets), pre-load each bucket into a model's KV cache, run buckets in parallel, and have a supervisor model progressively explore buckets and ask follow-up questions before synthesising a final answer. He noted KV cache cost can be managed by optimising cache lifetime. The approach sits between RAG and GraphRAG on the cost/accuracy tradeoff curve.

## Relevance to YOLO loop

Relevant if the YOLO loop needs to reason over a large project corpus where all documents are potentially relevant (e.g. full codebase + all design docs). The parallel bucket pattern with a supervisor is an architectural option for the loop's context retrieval stage when RAG recall is insufficient.

## Notes

No benchmark numbers provided. KV cache cost is a real concern — speaker acknowledges it but only gestures at lifecycle optimisation. Worth revisiting when Anthropic or other providers offer cheaper KV cache pricing.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-28-extended-cache-augmented-generation` |
| Channel | aie |
| Video | [When All Context Matters: Extended Cache Augmented Generation - Luis Romero-Sevilla, Orbis](https://www.youtube.com/watch?v=XovaGv4f39A) |
| Published | 2026-06-28 |
| Ingested upstream | 2026-06-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

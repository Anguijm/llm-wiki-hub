# Implement a Dedicated Document Context Layer Between Agents and Raw Documents

> Back to [[experiments-index]]

Source: **[Building the Document Context Layer for AI Agents — Jerry Liu, LlamaIndex](https://www.youtube.com/watch?v=RQi7x-navxU)** · aie · 2026-09-23

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we insert a dedicated document context layer (as described by LlamaIndex) between our agents and raw document sources, then agent reasoning quality will improve because agents receive pre-structured, semantically enriched context rather than raw text chunks that require the agent to do its own parsing.

## What they did

Jerry Liu from LlamaIndex presented the architecture for a document context layer — a middleware that handles parsing, structuring, indexing, and retrieval of documents specifically optimized for agent consumption, going beyond naive RAG.

## Relevance to YOLO loop

Directly applicable to our loop's context management — replacing ad-hoc RAG with a proper document context layer would make agent context more reliable and reduce hallucinations from poor retrieval.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-23-document-context-layer-agents-llamaindex` |
| Channel | aie |
| Video | [Building the Document Context Layer for AI Agents — Jerry Liu, LlamaIndex](https://www.youtube.com/watch?v=RQi7x-navxU) |
| Published | 2026-09-23 |
| Ingested upstream | 2026-09-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

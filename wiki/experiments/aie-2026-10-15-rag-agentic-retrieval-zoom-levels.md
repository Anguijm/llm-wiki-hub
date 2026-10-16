# Give a RAG agent multiple zoom levels (chunk → section → full document) via metadata-driven tool calls

> Back to [[experiments-index]]

Source: **[Your Fridge Is a Valid Payment Device — Eleonora Drykina & Nina Žižakić, In The Pocket](https://www.youtube.com/watch?v=gonAewBZxfU)** · aie · 2026-10-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we equip the RAG agent with tools to fetch at chunk, section, or full-document granularity using indexed metadata (chunk index, section path, rulebook ID), then answer quality will improve over single-call retrieval because the agent can gather more context when a narrow chunk is insufficient.

## What they did

Eleonora described switching from a single LLM call with retrieved chunks to an agentic retrieval loop. The agent could call a vector search tool for initial chunks, then use section-path metadata to fetch the entire section, or use rulebook ID to list all available rulebooks. Non-overlapping chunks were intentional so that reassembling a section from its chunk index produced the original text exactly. They observed meaningful eval score increases after this architectural change. Streaming was also highlighted as critical for perceived usability.

## Relevance to YOLO loop

Maps to any retrieval step in the YOLO loop where a single-shot vector search leaves the agent without enough context. Adding section-fetch and document-list tools to the agent's tool registry is a concrete upgrade path.

## Notes

Hybrid embeddings used: dense + BM25. Non-overlapping chunks are a prerequisite for clean section reassembly. Conversation history intentionally capped at last 20 messages to control context size.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-15-rag-agentic-retrieval-zoom-levels` |
| Channel | aie |
| Video | [Your Fridge Is a Valid Payment Device — Eleonora Drykina & Nina Žižakić, In The Pocket](https://www.youtube.com/watch?v=gonAewBZxfU) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

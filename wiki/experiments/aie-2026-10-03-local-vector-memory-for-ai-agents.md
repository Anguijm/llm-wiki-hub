# Add Local Qdrant Vector Memory to Agent Loop

> Back to [[experiments-index]]

Source: **[Stop Renting Your AI's Memory — Dylan Couzon, Qdrant](https://www.youtube.com/watch?v=apyrzaWj0Z4)** · aie · 2026-10-03

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we attach a locally-running Qdrant vector store to our agent loop with write, retrieve, and forget operations, then the agent will accumulate user-specific context across sessions because persistent vector retrieval compounds knowledge over time without relying on a third-party cloud memory service.

## What they did

Dylan Couzon argued that AI assistants reset to zero each session because their 'disk' (long-term memory) lives in someone else's data center. He demonstrated running Qdrant locally with no network attachment, using HNSW-based vector retrieval to store and query object observations from a drone/robot, showing the system could recall items (e.g., a coffee table and how many times it had been seen) entirely offline. He framed memory as three verbs — write, retrieve, forget — and showed that a locally-owned embedding folder paired with a consistent embedding model is portable across hardware swaps, enabling lifetime context accumulation owned entirely by the user.

## Relevance to YOLO loop

Our dev loop currently starts each run with no memory of prior sessions, preferences, or dead ends hit during development. Adding a local Qdrant instance as the persistent memory layer would let the loop accumulate project-specific context (e.g., failed approaches, coding preferences, recurring errors) across runs, making each iteration smarter without expanding the context window.

## Notes

Speaker specifically highlights that HNSW has been available since 2016 and local embeddings since 2019 — infrastructure is mature. Key implementation detail: keep the same embedding model across hardware changes to preserve portability of the memory folder. Cloud sync to Qdrant Cloud is optional and opt-in for multi-device or multi-agent hive-mind scenarios.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-03-local-vector-memory-for-ai-agents` |
| Channel | aie |
| Video | [Stop Renting Your AI's Memory — Dylan Couzon, Qdrant](https://www.youtube.com/watch?v=apyrzaWj0Z4) |
| Published | 2026-10-03 |
| Ingested upstream | 2026-10-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

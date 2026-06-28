# Swap the retrieval layer in agent vector search to TurboQuant 3-4 bit embedding compression for 5x memory reduction

> Back to [[experiments-index]]

Source: **[Turbocharge Your Agent's Retrieval with TurboQuant - Shashi Jagtap, Superagentic AI](https://www.youtube.com/watch?v=tB9RKTrU-Ig)** · aie · 2026-06-28

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we replace float32 vector storage in our agent's retrieval index with TurboQuant 3-4 bit compressed embeddings (using Polar Quant + QJL error correction), then we achieve ~5x reduction in index memory with retrieval quality preserved at ~90% recall, because search only needs to find the closest vector, not reconstruct it exactly, and TurboQuant's two-stage compression corrects quantisation errors sufficiently for ranking purposes.

## What they did

Shashi presented TurboQuant, a Google Research paper from ICLR 2026, as a practical tool for agent memory reduction. He explained the two-stage algorithm: (1) Polar Quant shuffles and scalar-quantises vectors into 3-4 bits; (2) QJL fixes remaining error with 1 bit. He demonstrated this via the open-source 'Turbo Agent' library which wraps existing agent frameworks and vector databases — only the retrieval/indexing layer is swapped. In a live demo using a 2B local Llama model and a 0.6B quantised embedding model (256 dimensions), the float32 index used 8KB vs TurboQuant's 1.6KB (5x smaller) with identical answers. He noted the library is already being adopted by llama.cpp, MLX, Ollama, and LM Studio. Recommended sweet spot is 3.5 bits; 4 bits is the practical safe choice.

## Relevance to YOLO loop

The YOLO loop's vector retrieval for code and docs can directly benefit from this swap — lower RAM usage means larger indexes fit on local machines, enabling bigger codebase coverage without GPU or cloud vector DB costs.

## Notes

Cold start limitation: pure semantic search until enough usage history accumulates for utility scoring. For new projects, plan for a warm-up period. GitHub repo: TurboAgent. Also supports LanceDB and SurrealDB as vector backends.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-28-turboquant-embedding-compression` |
| Channel | aie |
| Video | [Turbocharge Your Agent's Retrieval with TurboQuant - Shashi Jagtap, Superagentic AI](https://www.youtube.com/watch?v=tB9RKTrU-Ig) |
| Published | 2026-06-28 |
| Ingested upstream | 2026-06-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

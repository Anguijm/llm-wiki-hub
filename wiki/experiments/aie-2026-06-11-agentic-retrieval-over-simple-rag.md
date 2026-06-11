# Replace single-shot vector search with iterative agentic retrieval (search→read→assess→repeat) for agent context gathering

> Back to [[experiments-index]]

Source: **[RAG is dead, right?? — Kuba Rogut, Turbopuffer](https://www.youtube.com/watch?v=UM6sFg_jdlE)** · aie · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we replace a one-shot vector search retrieval step in our agent pipeline with an iterative agentic retrieval loop that combines semantic search, full-text search, grep, and regex as tools the agent selects based on intermediate findings, then retrieval accuracy will improve significantly (potentially 12–24% per Cursor's benchmarks) because agents can progressively narrow context to the right subset rather than relying on a single embedding similarity pass that conflates structural and semantic similarity.

## What they did

Kuba Rogut from Turbopuffer argued that 'RAG is dead' discourse conflates simple one-shot vector search with the broader concept of retrieval-augmented generation. He reframed RAG as any retrieval method (vector, BM25, grep, glob, regex, filters) feeding an LLM, and agentic search as giving agents a tool suite to iteratively retrieve and reason until a satisfactory context state is reached. He cited Cursor's case study: they use Turbopuffer for semantic search over chunked codebases, with Merkle-tree deduplication to avoid re-embedding unchanged files. Cursor found 12.5–13.5% average accuracy improvement and nearly 24% improvement on their Composer model from adding semantic search to the agent toolkit. He cited Jeff Dean's framing: even with trillion-token context windows, staged retrieval to get 'the right million' is necessary. He showed a token cost comparison: an agent without indexed retrieval spent ~6,000 tokens grep-reading to answer one sub-question; an agent with upfront indexed retrieval answered the same query with a lightweight lookup after a one-time indexing cost.

## Relevance to YOLO loop

If our YOLO loop agents currently use single-shot vector search to locate relevant code or docs, upgrading to an iterative retrieval tool set (search→read→reassess) could meaningfully improve task completion rates. The Merkle-tree incremental indexing pattern is also relevant for keeping codebase indexes fresh without full re-embedding on every run.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-11-agentic-retrieval-over-simple-rag` |
| Channel | aie |
| Video | [RAG is dead, right?? — Kuba Rogut, Turbopuffer](https://www.youtube.com/watch?v=UM6sFg_jdlE) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

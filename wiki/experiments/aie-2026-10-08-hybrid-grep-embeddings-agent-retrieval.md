# Add Hybrid Grep + Vector Search Toolset to Document-Heavy Agents to Replace Full-File Downloads

> Back to [[experiments-index]]

Source: **[Grep or Embeddings? Agentic Search Over Company Documents — George He, LlamaIndex](https://www.youtube.com/watch?v=X4w2Pkz5tDY)** · aie · 2026-10-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we give document-retrieval agents a toolset combining semantic vector search (for broad discovery) and regex grep (for precise in-file targeting) against a remote index, then agents can answer questions over large heterogeneous document corpora without downloading full files or burning tokens on irrelevant content, because the two tools complement each other — embeddings find relevant chunks, grep pinpoints exact offsets within those chunks.

## What they did

George He from LlamaIndex argued that code-style local file grep (as used by Claude Code) does not scale to enterprise document sets (PDFs, PowerPoints, images, mixed formats) because: (1) company data is not syntactically structured like code, (2) security/access control is more complex, (3) scale prohibits local storage. His approach: pre-index documents with hybrid retrieval (keyword + semantic, tunable balance), return chunks with page screenshots for grounding, then expose a grep tool for regex search within specific files at a given offset/length. Demonstrated an agent answering 'give me cash flow as a table from 2021-2025' by issuing search commands, reviewing screenshots, re-scoping queries, and reading specific file offsets — producing a grounded multi-file answer. Threshold guidance: local file grep is fine for 100-1000 files; pre-indexed vector retrieval is necessary at thousands to millions.

## Relevance to YOLO loop

When our YOLO loop agents need to reason over large document sets (specs, runbooks, historical PRs), this hybrid toolset pattern avoids context stuffing and provides grounded, auditable retrieval rather than bulk file ingestion.

## Notes

LlamaIndex is Series A, focuses on document parsing + orchestration + knowledge management. Key tool pair: (1) semantic search returning chunks + page screenshots, (2) grep with offset + max_length params for precise extraction. The page screenshot alongside the chunk gives the agent visual grounding to verify relevance before committing to a chunk.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-08-hybrid-grep-embeddings-agent-retrieval` |
| Channel | aie |
| Video | [Grep or Embeddings? Agentic Search Over Company Documents — George He, LlamaIndex](https://www.youtube.com/watch?v=X4w2Pkz5tDY) |
| Published | 2026-10-08 |
| Ingested upstream | 2026-10-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

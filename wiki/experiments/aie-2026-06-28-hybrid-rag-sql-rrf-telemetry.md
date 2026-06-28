# Pre-process documents into PostgreSQL with hybrid RRF search before LLM queries to avoid multimodal upload token tax

> Back to [[experiments-index]]

Source: **[Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry - Abed Matini, Ogilvy](https://www.youtube.com/watch?v=Akm1sqvWG4A)** · aie · 2026-06-28

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we convert documents to markdown via Docling at ingest time, chunk and embed them into PostgreSQL, and retrieve at query time using Reciprocal Rank Fusion over both keyword and semantic search, then we avoid spending tokens on document upload at query time and improve retrieval relevance, because pre-indexing separates the one-time parsing cost from the repeated inference cost and RRF surfaces better-ranked results than either search method alone.

## What they did

Abed built a framework-free FAQ chatbot (FastAPI + React + PostgreSQL + Ollama + LangFuse) for an HR employee handbook use case. Documents (PDF, PPTX, DOCX, images) are converted to markdown by Docling at ingest, chunked with multiple strategies selectable via admin UI, and embedded into PostgreSQL's vector extension. At query time, hybrid search combines keyword and semantic retrieval using SQL-based Reciprocal Rank Fusion (RRF). LangFuse provides observability over all LLM calls, latency, and tool use. Prompt injection and risky queries are filtered in Python before reaching the LLM using rule-based checks (rigid, fully testable, no reliance on LLM for safety). He ran the full stack locally on CPU only (no GPU) using a quantised Qwen 0.5B chat model and a BGE embedding model — the smallest models sufficient once data is pre-vetted.

## Relevance to YOLO loop

The ingest-once, retrieve-many pattern maps directly to providing the YOLO loop with project documentation context. Pre-indexing codebases and docs means each loop iteration pays retrieval cost rather than re-ingestion cost.

## Notes

Key finding: with well-vetted pre-processed data, the smallest quantised models produce accurate, low-hallucination answers. Rule-based safety filtering in Python before LLM is more reliable than prompting the LLM to police itself.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-28-hybrid-rag-sql-rrf-telemetry` |
| Channel | aie |
| Video | [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry - Abed Matini, Ogilvy](https://www.youtube.com/watch?v=Akm1sqvWG4A) |
| Published | 2026-06-28 |
| Ingested upstream | 2026-06-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

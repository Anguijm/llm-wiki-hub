# Use Docling for local, GPU-free conversion of PDFs and mixed documents to structured markdown before RAG ingestion

> Back to [[experiments-index]]

Source: **[Structuring the Unstructured - Cedric Clyburn, Red Hat](https://www.youtube.com/watch?v=-x5GEVnkuRw)** · aie · 2026-06-28

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we process all enterprise documents (PDFs, PPTX, DOCX, scanned images) through Docling's local OCR+layout-analysis pipeline to produce clean markdown or JSON before embedding, then RAG retrieval accuracy improves and hallucination risk decreases compared to naive PDF parsers or frontier-model extraction, because Docling correctly preserves table structure, image captions, and column boundaries that simple parsers merge or truncate and that LLMs non-deterministically misinterpret.

## What they did

Cedric demonstrated Docling (Linux Foundation open-source project) as a local document processing tool that runs on CPU without GPU. It uses a combination of OCR and layout analysis to parse PDFs and other formats into a Pydantic DoclingDocument object exportable to markdown or JSON. Key capabilities shown: table extraction preserving row/column structure, image content extraction (via annotation models), caption and heading detection. He demonstrated the contrast between a naive PDF parser (truncated/merged text, unusable table, no image content) vs frontier model extraction (good quality but expensive and non-deterministic at scale) vs Docling (deterministic, fast, cheap, local). He also showed docling-serve (run as a microservice/container) for scaling to thousands of documents, and the Docling MCP server for agentic document processing — allowing agents like Claude Code or Cursor to trigger Docling conversions via MCP tool calls. The hybrid chunker was highlighted for RAG-optimised chunking.

## Relevance to YOLO loop

Any YOLO loop that ingests project documentation, design docs, or external references as context should pre-process them through Docling rather than passing raw PDFs to the LLM. One-time setup, then all future document ingestion is deterministic and cheap.

## Notes

The viral tweet about 20 scientific papers containing a hallucinated term (from AI misreading a scanned two-column PDF) is a compelling case for why deterministic document parsing matters. Docling MCP server enables agentic document workflows without custom glue code.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-28-docling-unstructured-document-processing` |
| Channel | aie |
| Video | [Structuring the Unstructured - Cedric Clyburn, Red Hat](https://www.youtube.com/watch?v=-x5GEVnkuRw) |
| Published | 2026-06-28 |
| Ingested upstream | 2026-06-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

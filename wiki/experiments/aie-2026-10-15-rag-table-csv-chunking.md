# Convert PDF tables to CSV chunks with preserved row/column context for RAG

> Back to [[experiments-index]]

Source: **[Your Fridge Is a Valid Payment Device — Eleonora Drykina & Nina Žižakić, In The Pocket](https://www.youtube.com/watch?v=gonAewBZxfU)** · aie · 2026-10-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we detect tables in PDFs and convert them to CSV format (rather than extracting raw text) before chunking, then the RAG agent will retrieve correct cell values—especially for merged-cell tables—because structured CSV preserves row-column relationships that plain-text extraction destroys.

## What they did

Nina and Eleonora built a RAG system over ~270 PDF rulebooks (~6,000 pages, ~3,000 tables) for a Belgian fintech. Their initial pipeline extracted plain text from PDFs, which mangled merged-cell tables and caused the agent to return wrong fee or rule values. They switched to detecting tables and converting them to CSV format, storing each as a separate chunk with metadata (rulebook name, page number, section path, chunk index). Section paths were extracted via regex on heading patterns, enabling the agent to fetch entire sections when more context was needed. They also generated LLM-produced summaries per rulebook at index time, attached to every chunk, so the agent could identify which document a chunk came from. Evaluation used ~86 Promptfoo tests including citation correctness checks.

## Relevance to YOLO loop

Directly applicable when the YOLO loop indexes structured documents (specs, changelogs, financial docs). The table-to-CSV conversion step and section-path metadata pattern can be dropped into any PDF ingestion pipeline to improve retrieval precision.

## Notes

They also noted that LLM-based evaluation has significant noise—5 of 12 observed changes did not reproduce on re-run. Recommend running evals multiple times before trusting any delta. Promptfoo used for test harness.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-15-rag-table-csv-chunking` |
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

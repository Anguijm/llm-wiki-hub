# Use a Purpose-Built VLM for Table Extraction from Documents Instead of Generic OCR

> Back to [[experiments-index]]

Source: **[Your Agreements Are a Database You Can't Query — Hiral Shah, Docusign & Sean Sodha, NVIDIA](https://www.youtube.com/watch?v=_gvamfT8H-w)** · aie · 2026-09-16

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use a layout-aware vision-language model specifically trained for table extraction (e.g., NVIDIA Neatron Parse) rather than generic OCR or line-by-line text extraction, then structured data in tables (pricing tiers, SLAs, rate cards) will be extracted accurately from PDFs and images because generic models read line-by-line and break table structure.

## What they did

Hiral (DocuSign) and Sean (NVIDIA) described the challenge of extracting structured data from enterprise agreements at scale (1M agreements/day, 1.9M customers). Generic LLMs and OCR tools fail on tables because they process text line-by-line, destroying the relational structure of cells. DocuSign partnered with NVIDIA to use Neatron Parse, a purpose-built model from the Neatron Retriever portfolio that understands document layout and extracts tables as structured data. They run a hybrid pipeline: Neatron Parse for tables, standard OCR for free-text fields and metadata. The model currently runs on FP16 with paths to FP8/FP4 quantization. They use batch preprocessing (not runtime) for pabyte-scale document corpora to separate high-throughput offline extraction from low-latency online Q&A.

## Relevance to YOLO loop

Relevant if our dev loop needs to ingest structured data from PDFs (e.g., API specs, pricing docs, data sheets). Swapping generic PDF parsing for a layout-aware table extraction model improves the quality of RAG context for structured queries.

## Notes

Neatron Parse is available from NVIDIA. Two latency modes discussed: batch preprocessing for large corpora vs. reactive single-document extraction for low-latency Q&A. DocuSign blog post on their full pipeline architecture is available publicly.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-16-neatron-table-extraction` |
| Channel | aie |
| Video | [Your Agreements Are a Database You Can't Query — Hiral Shah, Docusign & Sean Sodha, NVIDIA](https://www.youtube.com/watch?v=_gvamfT8H-w) |
| Published | 2026-09-16 |
| Ingested upstream | 2026-09-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

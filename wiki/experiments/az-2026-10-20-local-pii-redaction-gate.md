# Prototype a local PII redaction gate before cloud model calls

> Back to [[experiments-index]]

Source: **[It Begins... Local AI and the Cloud Start Sharing](https://www.youtube.com/watch?v=8FEm8mMzeLE)** · az · 2026-10-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run the open-source PII Tracer model and a local open-weights model on the Strix Halo box to detect and redact personal data before any prompt goes to a cloud LLM, then sensitive content will stay on-device while cloud research still works because only the non-sensitive query parts are sent.

## What they did

Alex Ziskind tested Perplexity Computer's Privacy Gate on three Macs. The PII Tracer model on Hugging Face scans documents, images and folders for personal data. A local model (Gemma 4 E4B, Qwen 3.6 35B or Perplexity's 19GB model) analyzes the sensitive records on-device. The redacted query is then dispatched to cloud models, and OCR runs locally. A sample audit of 6 months of ISP bills flagged an $88 overcharge. He warns that dragging photos into the main chat uploads them to the cloud, and that PII classification may need user confirmation when boundaries are ambiguous.

## Relevance to YOLO loop

high: A redaction hook in front of cloud model calls is a concrete Claude Code hook and verification pattern.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-20 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `az-2026-10-20-local-pii-redaction-gate` |
| Channel | az |
| Video | [It Begins... Local AI and the Cloud Start Sharing](https://www.youtube.com/watch?v=8FEm8mMzeLE) |
| Published | 2026-10-20 |
| Ingested upstream | 2026-10-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

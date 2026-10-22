# Benchmark MXFP4 large-model serving on Strix Halo

> Back to [[experiments-index]]

Source: **[Stop paying for AI, run everything locally (here’s how)](https://www.youtube.com/watch?v=DwoWIf8f2yQ)** · do · 2026-10-20

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we serve a large MXFP4-quantized open-weights model on the 128 GB Strix Halo box with a split unified-memory allocation and run coding agents in an air-gapped sandbox, then we will get usable local decode speed for Push to Talk and agent work because unified memory and 4-bit quantization fit large models while sandboxing limits supply-chain risk.

## What they did

David Ondrej and Ahmed demonstrated ODS (Open Deployment System, Apache 2.0, single-command install) on an Asus ProArt laptop with 128 GB unified memory split 32 GB system and 96 GB GPU. They reported 72 tokens per second on Qwen 3.8 Flash Next in MXFP4 and an 180B model loaded using 88 GB VRAM with disk-cached SSD embeddings, and generated a web page offline. They claimed dual RTX Sparks beat an M5 Ultra Mac Studio despite lower memory bandwidth. They also warned that fine-tuned open-weights models can carry credential-stealing backdoors and recommended air-gapped sandboxes, and noted local models fail at hardware tasks without search and documentation access.

## Relevance to YOLO loop

medium: Sandboxing local coding agents and untrusted weights is relevant to agent workflow safety, but the focus is local inference.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-21 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-10-20-local-inference-sandboxing-strix-halo` |
| Channel | do |
| Video | [Stop paying for AI, run everything locally (here’s how)](https://www.youtube.com/watch?v=DwoWIf8f2yQ) |
| Published | 2026-10-20 |
| Ingested upstream | 2026-10-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

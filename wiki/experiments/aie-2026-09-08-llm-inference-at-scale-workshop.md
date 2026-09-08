# Build a structured decision framework for selecting LLM serving engines based on use-case constraints

> Back to [[experiments-index]]

Source: **[Deep dive on LLM Inference at Scale — Harshul Jain, Audible & Tanmay Sah, Independent AI Researcher](https://www.youtube.com/watch?v=y2W4FNAuPEA)** · aie · 2026-09-08

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we apply a first-principles inference optimization checklist (model sizing → quantization → serving engine selection → KV cache tuning) before deploying any LLM endpoint, then we will reduce per-token serving cost and improve throughput predictably, because most production inference bottlenecks stem from mismatches between hardware memory budgets and model/serving-engine defaults rather than model capability gaps.

## What they did

Harshul Jain (Audible) and Tanmay Sah ran a two-hour workshop covering LLM inference from first principles. They demonstrated GPU memory profiling on a Mistral-7B model loaded onto an RTX 6000 (102GB VRAM), showing baseline 15GB model weight footprint and the additional KV cache growth with sequence length. They walked through model-level optimizations (quantization to reduce memory), serving-level optimizations (batching strategies, attention mechanism choices), and a benchmark-driven engine selection guide comparing vLLM, SGLang, TensorRT-LLM, Nvidia Dynamo, and HuggingFace's no-server option. They provided Jupyter notebooks via Modal (Google Colab alternative with free RTX 6000 GPU) and a public GitHub repo with slides and a benchmark report. They also outlined a decision chart: pick model → quantize to fit target GPU → select serving engine by throughput/latency SLA → apply KV cache eviction strategy for long-context workloads.

## Relevance to YOLO loop

Relevant to our infrastructure layer: as we scale Codex/Astra API usage costs, self-hosting open-weight models for lower-stakes tasks becomes attractive. This workshop provides the evaluation framework and hands-on notebooks to benchmark candidate engines (vLLM vs SGLang vs TensorRT) against our specific throughput and latency requirements before committing to a serving stack.

## Notes

Repo is public on GitHub ('LLM inference at scale'). Modal provides free RTX 6000 GPU for notebook experiments. Key takeaway: KV cache engineering is becoming its own sub-discipline (eviction strategies, compression, hybrid memory) — worth monitoring. Workshop pitched as beginner/intermediate; advanced distributed inference session proposed for AI Engineer New York.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-08-llm-inference-at-scale-workshop` |
| Channel | aie |
| Video | [Deep dive on LLM Inference at Scale — Harshul Jain, Audible & Tanmay Sah, Independent AI Researcher](https://www.youtube.com/watch?v=y2W4FNAuPEA) |
| Published | 2026-09-08 |
| Ingested upstream | 2026-09-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

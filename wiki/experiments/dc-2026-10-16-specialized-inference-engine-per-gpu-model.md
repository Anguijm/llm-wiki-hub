# Benchmark GPU-specialised inference engines (GGZ14/DFlash-2, R9V, Rob Smith vLLM) against baseline llama.cpp on our Strix Halo box for Qwen 3.8 family models

> Back to [[experiments-index]]

Source: **[Qwen3.8 27B and Flash Next on Single/Dual AMD Radeon 9700: Engine Benchmarks and Setup](https://www.youtube.com/watch?v=FIoTh48iRBU)** · dc · 2026-10-16

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we test GPU-architecture-specific inference engine forks (GGZ14 with DFlash-2, R9V vLLM fork) against baseline llama.cpp with ROCm/Vulkan on our AMD Radeon 8060S hardware, then we will find 2–3× generation speed improvements at long contexts, because specialised kernels exploit the exact memory and compute layout of the target GPU in ways a general engine cannot.

## What they did

Donato benchmarked Qwen 3.8 27B and Flash Next on a dual AMD Radeon AI Pro 9700 (32 GB VRAM each) using several specialised inference engines: GGZ14 with DFlash-2 achieved 50+ tokens/s on one GPU and ~100 on two at 64K context; Rob Smith's customised vLLM build with MTP and mixed quantisation (MXFP4 experts, FP8 attention, 6-bit embeddings) hit 107 tokens/s on two GPUs for Flash Next vs. 30 tokens/s with baseline llama.cpp Vulkan. He used a real-world agent-simulation benchmark (growing conversation via OpenAI-compatible endpoint with context reuse measurement) rather than raw library benchmarks.

## Relevance to YOLO loop

high: directly applicable to our Strix Halo box (Radeon 8060S)—identifying the fastest inference engine for Qwen 3.8 family models would directly improve Push to Talk response latency and any local agentic coding workflows.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `dc-2026-10-16-specialized-inference-engine-per-gpu-model` |
| Channel | dc |
| Video | [Qwen3.8 27B and Flash Next on Single/Dual AMD Radeon 9700: Engine Benchmarks and Setup](https://www.youtube.com/watch?v=FIoTh48iRBU) |
| Published | 2026-10-16 |
| Ingested upstream | 2026-10-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

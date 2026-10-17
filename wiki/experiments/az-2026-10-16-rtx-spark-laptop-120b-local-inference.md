# Compare vLLM multi-user throughput vs. llama.cpp single-user latency on unified-memory ARM hardware for agent workloads

> Back to [[experiments-index]]

Source: **[NVIDIA Put a DGX Spark in a Laptop… Almost](https://www.youtube.com/watch?v=iZ88PPiAsl8)** · az · 2026-10-16

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run vLLM vs. llama.cpp on unified-memory hardware with simulated multi-agent concurrency, then vLLM will win on total throughput at 4+ concurrent agents while llama.cpp will win on single-user latency, because vLLM's batching overhead is amortised across concurrent requests in the same way a bus outperforms a car only when full.

## What they did

AZisk benchmarked the MSI Prestige N16 (RTX Spark, 128 GB unified memory, ARM-based N1X chip) running 120–125B parameter models. He found llama.cpp delivered 65 tokens/s single-user vs. vLLM's 35 tokens/s, but vLLM scaled to 127.5 tokens/s total with 8 concurrent users while llama.cpp barely improved. He also confirmed no thermal throttling over 20 minutes at full GPU+CPU load, and tested Qwen 3.8 Flash Next (125B) at 33.7 tokens/s on the thin laptop. He demonstrated adjustable GPU memory allocation (up to 96 GB dedicated) via the Nvidia app.

## Relevance to YOLO loop

medium: informs our serving strategy for local models when running multiple Claude Code sub-agents concurrently—vLLM for multi-agent, llama.cpp for interactive single-session use.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `az-2026-10-16-rtx-spark-laptop-120b-local-inference` |
| Channel | az |
| Video | [NVIDIA Put a DGX Spark in a Laptop… Almost](https://www.youtube.com/watch?v=iZ88PPiAsl8) |
| Published | 2026-10-16 |
| Ingested upstream | 2026-10-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Profile and reduce KV cache memory pressure in long-context agent runs by tuning batching strategy

> Back to [[experiments-index]]

Source: **[How Inference Keeps Up with Our Insatiable Need for Tokens — Cerebras & Gimlet Labs](https://www.youtube.com/watch?v=_cRgl3maiT8)** · aie · 2026-10-13

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we measure KV cache growth during long-context YOLO loop runs and apply continuous batching with paged KV cache, then we can serve more parallel agent threads at the same memory budget because paged KV cache eliminates fragmentation and continuous batching fills idle compute slots that would otherwise waste the weight-read cost.

## What they did

Daniel (Cerebras) and Michelle (Gimlet Labs) gave a deep technical walkthrough of inference optimization history and roadmap. Key points: (1) LLM autoregressive generation is memory-bandwidth-bound — compute sits idle up to 90% of the time waiting on weight reads; (2) tensor parallelism across GPUs helps speed but incurs all-reduce communication overhead, yielding diminishing returns; (3) continuous batching slots new requests into idle compute windows within a single weight read; (4) KV cache is the dominant memory consumer — a 70B model needs ~1 GB KV cache per 3,000 tokens per request, ballooning to 42 GB for a single 128K-context coding agent session; (5) paged KV cache (inspired by OS virtual memory) reduces fragmentation; (6) Gimlet's KForge agent autonomously generates and tunes GPU kernels for specific hardware/model/workload combinations, achieving 33% end-to-end speedup on GPT-MoE 12B on AMD hardware within one week of agent runtime.

## Relevance to YOLO loop

The YOLO loop runs long-context coding agents that accumulate large KV caches. Understanding the ~1 GB per 3K tokens rule helps right-size inference infrastructure and choose between speed (more tensor parallelism) and throughput (larger batches). The KForge kernel-generation agent pattern is also directly applicable: we could run a similar agent to auto-tune our local inference stack for our specific model and workload shape.

## Notes

The KForge agent-generates-kernels pattern (brute-force search over hardware/workload profiles) is a low-overhead experiment to try on local vLLM/SGLang deployments. Start by profiling actual KV cache usage per agent run before investing in paged KV cache infrastructure.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-13-kv-cache-inference-optimization` |
| Channel | aie |
| Video | [How Inference Keeps Up with Our Insatiable Need for Tokens — Cerebras & Gimlet Labs](https://www.youtube.com/watch?v=_cRgl3maiT8) |
| Published | 2026-10-13 |
| Ingested upstream | 2026-10-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Implement KV Cache Offload from GPU to CPU Memory to Sustain 5-10x Inference Speedups Without Cache Eviction

> Back to [[experiments-index]]

Source: **[What Makes Open Models Fast in Production — Sujee Maniyam, Nebius](https://www.youtube.com/watch?v=TRe1u7dHYiA)** · aie · 2026-10-04

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we offload KV cache from GPU memory to CPU/regular memory automatically rather than evicting it when GPU memory is under pressure, then we will sustain 5-10x inference speedups from caching even under large context windows, because the cache is preserved across requests instead of being rebuilt from scratch.

## What they did

Nebius Token Factory described three stacked inference optimizations: (1) KV caching (5-10x speedup by reusing cached context tokens instead of regenerating), (2) automatic offload of the KV cache from GPU VRAM to CPU memory when GPU memory is scarce — bringing it back on demand — so the cache is never thrown away, (3) prefill/decode disaggregation: separate GPU sets handle the compute-intensive prefill phase and the memory-intensive decode phase, then transfer the KV cache between them, improving overall utilization.

## Relevance to YOLO loop

Maps to the inference infrastructure layer of the YOLO loop: for any self-hosted or managed model powering an agent loop, these optimizations directly reduce latency and cost per agent turn, making rapid iteration cheaper.

## Notes

High effort for self-hosted setups; low effort if using Nebius Token Factory or similar managed inference with these features built in. Worth evaluating managed inference vs self-host cost/latency tradeoff first.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-04-kv-cache-offload-gpu-memory` |
| Channel | aie |
| Video | [What Makes Open Models Fast in Production — Sujee Maniyam, Nebius](https://www.youtube.com/watch?v=TRe1u7dHYiA) |
| Published | 2026-10-04 |
| Ingested upstream | 2026-10-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

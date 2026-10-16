# Enable LM Cache (external KV cache server) for multi-agent vLLM workloads that exceed GPU memory

> Back to [[experiments-index]]

Source: **[I Made My AI Agents Faster Without a GPU Upgrade](https://www.youtube.com/watch?v=bYpdCFz7VtA)** · az · 2026-10-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we add LM Cache as an external KV cache layer on top of vLLM for multi-agent sessions that grow beyond GPU memory, then per-agent throughput will increase up to 7.5x and cache survives vLLM restarts, because LM Cache stores KV state in RAM and NVMe outside the GPU process so it persists across restarts and spills beyond GPU memory limits.

## What they did

AZisk benchmarked four caching setups for long agent sessions on local GPU hardware (DGX Station GB300 and RTX Pro 6000): no cache, vLLM prefix cache (GPU only), vLLM CPU offload (RAM), and LM Cache (external server, RAM + NVMe). With 8 concurrent agents on RTX Pro 6000 running Qwen3 8.27B, no-cache gave ~1 turn/min per agent; with either cache ~7 turns/min (7.5x). LM Cache uniquely survived a vLLM restart, reusing ~60K tokens vs. cold rebuild. Tradeoff: LM Cache adds config complexity and slower restarts.

## Relevance to YOLO loop

high: directly applicable to running multi-agent Claude Code workflows on local hardware—shows when vLLM prefix cache is sufficient vs. when LM Cache is needed for sessions that exceed GPU memory or need restart resilience.

## Notes

Decision rule from video: if everything fits in GPU memory, vLLM prefix cache (on by default) is sufficient. If it spills beyond GPU but fits in RAM, vLLM CPU offload matches LM Cache. Only add LM Cache if: cache outgrows RAM, server restarts are frequent, or cross-session persistence matters. LM Cache requires more config and slower restarts. ROCm/Vulkan compatibility for AMD Strix Halo not tested in video.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `az-2026-10-15-kv-cache-agents-lmcache` |
| Channel | az |
| Video | [I Made My AI Agents Faster Without a GPU Upgrade](https://www.youtube.com/watch?v=bYpdCFz7VtA) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

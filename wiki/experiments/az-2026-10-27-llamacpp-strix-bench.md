# Benchmark Qwen3 4B/8B Q4 on Strix Halo Vulkan vs ROCm

> Back to [[experiments-index]]

Source: **[I Tested Two $699 Laptops for Coding… It Got Weird](https://www.youtube.com/watch?v=vbHCaeH9LZ0)** · az · 2026-10-27

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run the same llama.cpp prompt-processing and token-generation benchmarks (Qwen 3 4B and 8B at 4-bit) on the Strix Halo box under Vulkan and ROCm, then we will get a baseline for Push to Talk model choice because memory fit and backend strongly determine tokens per second.

## What they did

The speaker built llama.cpp from source on both laptops and ran Qwen 3 4B and 8B at 4-bit, recording prompt processing and generation tokens per second. On the 4B model the Dell reached 156 t/s prompt processing and 15.7 t/s generation versus 142 and 17.9 on the MacBook Neo. When the 8B model spilled out of GPU allocation, the Dell collapsed to 0.23 t/s and the Neo held 7.1 t/s. He also measured wall power with a power meter and ran repeated runs to check throttling.

## Relevance to YOLO loop

none: This is hardware benchmarking and does not involve agent workflows.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-27 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `az-2026-10-27-llamacpp-strix-bench` |
| Channel | az |
| Video | [I Tested Two $699 Laptops for Coding… It Got Weird](https://www.youtube.com/watch?v=vbHCaeH9LZ0) |
| Published | 2026-10-27 |
| Ingested upstream | 2026-10-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Benchmark a tuned quantized open coding model on Strix Halo

> Back to [[experiments-index]]

Source: **[How Revolut Cut AI Coding Costs 90% With Self-Hosted Open Models - David Abitbol, Revolut](https://www.youtube.com/watch?v=Ok6QdZHCcI8)** · aie · 2026-10-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we serve a 4-bit quantized open coding model on the Strix Halo box with a capped context window, KV cache reuse and speculative decoding, then time-to-first-token and throughput will reach interactive levels at zero marginal token cost because Revolut got a 3x-plus latency improvement from the same tuning levers on fixed hardware.

## What they did

Revolut self-hosted GLM on 56 Nvidia B200 GPUs for 2,000 engineers using FP4 quantization, a 256K context cap, TP8 tensor parallelism, cache hit rates above 90%, speculative decoding and paged attention. Tuning raised throughput from 3 to 7 requests per second and cut time-to-first-token from 10s to 1.6s. Blended cost fell to $0.30 per million tokens, a 90% reduction versus cloud APIs. A local routing layer sent image queries to other models because GLM is text-only.

## Relevance to YOLO loop

medium: A flat-cost local coding model could handle cheap, high-volume agent subtasks inside the loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-29 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-29-strix-halo-quantized-coding-model` |
| Channel | aie |
| Video | [How Revolut Cut AI Coding Costs 90% With Self-Hosted Open Models - David Abitbol, Revolut](https://www.youtube.com/watch?v=Ok6QdZHCcI8) |
| Published | 2026-10-29 |
| Ingested upstream | 2026-10-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

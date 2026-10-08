# Profile Speculative Decoding Acceptance Rate by Task Type to Decide Whether to Enable It

> Back to [[experiments-index]]

Source: **[Is Speculative Decoding Worth It? Profiling vLLM on NVIDIA Blackwell — Akamai](https://www.youtube.com/watch?v=XTpyNrEgJQ4)** · aie · 2026-10-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we measure draft-model token acceptance rate separately for structured-output tasks (code, JSON, SQL) versus creative tasks (open-ended generation, high temperature), then we will find that speculative decoding yields meaningful throughput gains only for structured tasks because the draft model can predict deterministic token patterns far more accurately than creative ones, making it net-positive only when acceptance rate is high enough to offset the overhead of hosting a second model.

## What they did

Akamai's developer advocate set up vLLM with speculative decoding on a single NVIDIA Blackwell GPU, pairing a large target model (16 GB weights) with a small draft model (2.5 GB weights) from the same model family with the same tokenizer. She ran side-by-side comparisons of baseline vs. speculative-decoding-enabled inference for structured outputs (JSON/SQL) and creative outputs (high-temperature prompts), measuring token acceptance rate and tokens-per-second throughput. Structured tasks showed high acceptance rate and significantly improved throughput; creative tasks showed low acceptance rate with minimal benefit. She identified the key decision criteria: available VRAM headroom, workload concurrency level, task structure, and context-length ratio (input-heavy RAG workloads benefit less because speculative decoding accelerates the decode phase, not prefill).

## Relevance to YOLO loop

If our dev loop runs inference-heavy agents against structured outputs (code generation, JSON tool calls, SQL queries), enabling speculative decoding in our vLLM serving layer could reduce latency per agent step. The acceptance-rate profiling methodology gives us a concrete, low-risk way to evaluate this before committing to the architectural change.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-08-speculative-decoding-vllm-blackwell` |
| Channel | aie |
| Video | [Is Speculative Decoding Worth It? Profiling vLLM on NVIDIA Blackwell — Akamai](https://www.youtube.com/watch?v=XTpyNrEgJQ4) |
| Published | 2026-10-08 |
| Ingested upstream | 2026-10-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

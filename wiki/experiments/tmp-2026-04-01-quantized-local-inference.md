# Prototype a YOLO project using local quantized LLM inference via Ollama

> Back to [[experiments-index]]

Source: **[Google's New AI Just Broke My Brain (TurboQuant)](https://www.youtube.com/watch?v=7YVrb3-ABYE)** · @TwoMinutePapers · 2026-04-01

**Status:** `done` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we build one YOLO project that runs LLM inference locally using a quantized model (4-bit via Ollama), then we validate whether quantized local inference is production-viable for YOLO builds, because TurboQuant-style compression shows 6-8x memory reduction is achievable at 3-4 bit with no quality-loss fine-tuning required.

## What they did

Károly Zsolnai-Fehér covered Google's TurboQuant paper — a KV-cache vector quantization algorithm that achieves 6x memory reduction (8x throughput on H100) at 3-4 bit precision with no training or fine-tuning. The broader implication: compressed inference is becoming a viable alternative to full-precision cloud APIs for cost-sensitive or privacy-sensitive applications.

## Actionable steps

- Pick a YOLO project idea that requires repeated LLM calls (e.g., a text processing or code analysis tool)
- Implement it twice: once hitting Claude API, once using Ollama with a quantized model (e.g., qwen2.5-coder:7b-instruct-q4)
- Compare output quality, latency, cost, and dev complexity side by side
- Document which quantization tier (7B, 14B, 70B) meets the 'good enough' bar for YOLO-style builds

## Success metric

Local quantized model produces output that passes Gemini review at the same quality tier as Claude API, at materially lower per-call cost.

## Relevance to YOLO loop

YOLO projects currently use Claude API exclusively. Knowing when a local quantized model is 'good enough' would reduce API costs for projects with many LLM calls and opens up offline-capable or privacy-preserving builds.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

Parked — John wants to run this on different hardware. Revisit when target hardware is available.

## Notes

Parked. Interesting but needs different hardware than RTX 3070 Mobile.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `done` | Parked — shifting to different hardware |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `tmp-2026-04-01-quantized-local-inference` |
| Channel | @TwoMinutePapers |
| Video | [Google's New AI Just Broke My Brain (TurboQuant)](https://www.youtube.com/watch?v=7YVrb3-ABYE) |
| Published | 2026-04-01 |
| Ingested upstream | 2026-04-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Audit agent LLM calls and replace routine classification/summarization calls with on-device SLMs

> Back to [[experiments-index]]

Source: **[Frontier results, on device - RL Nabors, Arize](https://www.youtube.com/watch?v=fWXJM-J0ZB8)** · aie · 2026-06-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we identify which agent tool calls involve bounded, well-defined tasks (e.g. sentiment classification, chat summarization, urgency detection) and replace those specific calls with a locally-run small language model, then we will reduce per-call latency below 4 seconds, eliminate PII exposure to third-party servers, cut inference costs, and maintain quality parity with the frontier model on those subtasks, because SLMs with post-processing and prompt engineering can match LLM accuracy on narrow, repetitive tasks.

## What they did

Rachel Lee Nabors (Arize) demonstrated a workflow where she profiled an agentic system using Phoenix (Arize open-source observability), identified calls exceeding 4-second latency thresholds, then replaced a chat-thread summarization LLM call with a quantized SLM running locally. She added post-processing for length and structural validation, ran LLM-as-judge evals for factual consistency, and iterated prompt engineering to close the quality gap. Final results: P50 latency ~1s, P95 under 3.5s, 100% JSON and structural validity, ~$1/day inference savings. She recommended: prototype with a frontier model, then convert features to SLMs for production using prove→define→test→select workflow.

## Relevance to YOLO loop

Our dev loop likely makes many repeated, narrow LLM calls (status checks, summarization, classification) that could be served locally. Converting even one high-frequency call to a SLM reduces cost, latency, and data exposure — and the eval harness built during conversion becomes a regression test for future model changes.

## Notes

Key tooling: Arize Phoenix for latency profiling; Chrome Prompt API (Gemini Nano) for browser-native inference; quantized models (4-bit/8-bit) for device constraints. Critical: run evals across repeated seeds, not just one favorable run. Keep regression evals running CI-style to prevent prompt or model upgrades from silently degrading output.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-29-slm-replace-llm-calls` |
| Channel | aie |
| Video | [Frontier results, on device - RL Nabors, Arize](https://www.youtube.com/watch?v=fWXJM-J0ZB8) |
| Published | 2026-06-29 |
| Ingested upstream | 2026-06-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

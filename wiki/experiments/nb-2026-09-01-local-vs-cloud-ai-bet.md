# Build a local-vs-cloud task router for AI workloads

> Back to [[experiments-index]]

Source: **[Apple's New Mac Line is Built Around Local AI. The Bet Is You'd Rather Own Than Rent.](https://www.youtube.com/watch?v=1lO8aNSLPJc)** · nb · 2026-09-01

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we implement a routing layer that classifies tasks by complexity and sends them to local models by default and frontier APIs only when needed, then we can reduce token costs by 50-80% because 80-90% of routine AI work does not require frontier-level intelligence.

## What they did

Nate argued that the missing infrastructure piece in the local-AI ecosystem is a router that intelligently decides when a task can be handled by a local model on Apple Silicon and when it should be escalated to a frontier lab API. He pointed to OpenRouter token data trending toward open-source models as evidence that most workloads are locally satisfiable, and identified this routing problem as the main unsolved challenge for prosumer AI setups.

## Relevance to YOLO loop

Directly applicable to the YOLO loop's agent orchestration layer — a cost and latency optimizer that could front every LLM call, defaulting to a local Ollama/llama.cpp model and falling back to Claude or GPT only on low-confidence or high-complexity classifications.

## Notes

Nate explicitly calls this the 'routing problem' and says it is unsolved and worth building. OpenRouter open-source token share trend is a useful leading indicator to monitor.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-01 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-09-01-local-vs-cloud-ai-bet` |
| Channel | nb |
| Video | [Apple's New Mac Line is Built Around Local AI. The Bet Is You'd Rather Own Than Rent.](https://www.youtube.com/watch?v=1lO8aNSLPJc) |
| Published | 2026-09-01 |
| Ingested upstream | 2026-09-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

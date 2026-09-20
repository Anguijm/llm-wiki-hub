# Evaluate agent-optimized inference endpoints vs. generic LLM APIs for loop latency

> Back to [[experiments-index]]

Source: **[The Frontier AI Inference Cloud for Agents — Byung-Gon (Gon) Chun, FriendliAI](https://www.youtube.com/watch?v=Hvb2LfMH58c)** · aie · 2026-09-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we route YOLO loop LLM calls through an inference backend purpose-built for agentic workloads (e.g., FriendliAI), then we will see lower inter-step latency and better throughput under concurrent agent calls, because agent traffic patterns (many short, sequential calls with shared context) differ fundamentally from batch or chat workloads.

## What they did

Gon Chun described FriendliAI's inference cloud architecture designed specifically for agent use cases, covering how it handles high-frequency sequential requests, prefix caching for shared context across agent steps, and latency optimizations relevant to multi-step reasoning loops.

## Relevance to YOLO loop

The YOLO loop is an agentic system making many sequential LLM calls; an inference backend tuned for this pattern could reduce per-step latency and overall wall-clock time.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-20-friendli-agent-inference` |
| Channel | aie |
| Video | [The Frontier AI Inference Cloud for Agents — Byung-Gon (Gon) Chun, FriendliAI](https://www.youtube.com/watch?v=Hvb2LfMH58c) |
| Published | 2026-09-20 |
| Ingested upstream | 2026-09-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Run continuous Promptfoo evals across multiple LLM providers to select the fastest model that meets accuracy thresholds for latency-sensitive agentic tasks

> Back to [[experiments-index]]

Source: **[Agentic Sites: Building Hyper Personalized Websites — Carlos Sanchez, Adobe](https://www.youtube.com/watch?v=jebp4V0vh30)** · aie · 2026-08-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we continuously evaluate prompts for a specific use case across multiple LLM providers using an automated eval framework (Promptfoo), prioritizing both accuracy and latency, then we will find provider/model combinations that meet accuracy thresholds at dramatically lower latency (e.g., 1.1s vs 4.6s page generation), because the best model for a given task is highly site- and task-specific and cannot be determined by benchmark alone.

## What they did

Carlos built Adobe's 'Agentic Sites' system that personalizes web pages in real time based on user intent, using a RAG corpus built from the full site. For the backend, they run 15 prompt evaluations across multiple providers using Promptfoo, scoring on accuracy and latency. They found Cerebras running Gemma 4 achieved 1.1s average page generation at 2,300 tokens/second vs. 4.6s+ for the next-best provider—a 4x difference. They also built an OfOneLabs tool that auto-generates an agentic demo site for any URL in under an hour. The system personalizes blocks (not the whole page) to respect brand guidelines, grounding generation in the existing site corpus.

## Relevance to YOLO loop

The continuous provider-eval pattern applies directly to the YOLO loop's model-selection step: rather than hardcoding a provider, instrument evals that run on every model update and automatically route to the fastest accurate option for each task class.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-29-agentic-site-model-eval-latency` |
| Channel | aie |
| Video | [Agentic Sites: Building Hyper Personalized Websites — Carlos Sanchez, Adobe](https://www.youtube.com/watch?v=jebp4V0vh30) |
| Published | 2026-08-29 |
| Ingested upstream | 2026-08-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Benchmark Model Routing by Task Class Across GPT-5.5, Claude, and Gemini

> Back to [[experiments-index]]

Source: **[GPT-5.5 vs Claude vs Gemini: The Real Difference Nobody's Talking About](https://www.youtube.com/watch?v=9aIYhjeYxzM)** · NateBJones · 2026-04-28

**Status:** `in_progress` · **Effort:** `medium`

---

## Hypothesis

If we route different task classes (reasoning, code, long-context retrieval) to the model with the strongest empirical advantage for that class, then overall pipeline quality will improve over using a single model, because each frontier model has distinct capability profiles that are not captured by aggregate benchmarks.

## What they did

Speaker ran comparative tests across GPT-5.5, Claude, and Gemini on a set of real-world tasks and identified qualitative and quantitative differences in where each model excels that are underreported in standard benchmark coverage.

## Relevance to YOLO loop

Directly informs model selection at each node in the YOLO loop; a routing layer could swap the backbone model based on the task type detected at runtime.

## Notes

[2026-04-29T08:05:00Z] Implemented at experiments/model-routing-bench/. Adapters degrade to deterministic stubs without API keys, so the scaffold is runnable end-to-end. Promotion to tick queue is the next step.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-28 | `backlog` | Extracted from YouTube RSS |
|  | `` | Implemented as research-spike scaffold at experiments/model-routing-bench/. See README.md for design and usage. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-04-28-gpt55-vs-claude-vs-gemini-real-difference` |
| Channel | NateBJones |
| Video | [GPT-5.5 vs Claude vs Gemini: The Real Difference Nobody's Talking About](https://www.youtube.com/watch?v=9aIYhjeYxzM) |
| Published | 2026-04-28 |
| Ingested upstream | 2026-04-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

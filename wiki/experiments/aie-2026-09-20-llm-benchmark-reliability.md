# Replace reliance on public LLM benchmarks with task-specific internal evals for model selection

> Back to [[experiments-index]]

Source: **[Are LLM Performance Benchmarks Reliable? — Ashok Chandrasekar & Jason Kramberger, Google](https://www.youtube.com/watch?v=l1-D89bAuOA)** · aie · 2026-09-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we evaluate model candidates on our own task distribution rather than trusting public benchmark rankings, then we will make better model selection decisions, because public benchmarks are often contaminated, unrepresentative, or optimized against by model developers.

## What they did

Ashok Chandrasekar and Jason Kramberger from Google analyzed the reliability of LLM performance benchmarks, examining issues like benchmark contamination, variance in results, metric validity, and whether leaderboard rankings translate to real-world task performance.

## Relevance to YOLO loop

Model selection for the YOLO loop is currently likely influenced by public benchmarks; building even a small internal eval suite on actual loop tasks would yield more reliable model choices.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-20-llm-benchmark-reliability` |
| Channel | aie |
| Video | [Are LLM Performance Benchmarks Reliable? — Ashok Chandrasekar & Jason Kramberger, Google](https://www.youtube.com/watch?v=l1-D89bAuOA) |
| Published | 2026-09-20 |
| Ingested upstream | 2026-09-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Fine-tune a small model on tool-use discipline with RL to match large-model performance on structured tasks

> Back to [[experiments-index]]

Source: **[Stop Making Models Bigger, Make Them Behave — Kobie Crawdord, Snorkel](https://www.youtube.com/watch?v=TNwJ1LMiENk)** · aie · 2026-06-11

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `high`

---

## Hypothesis

If we apply RL training (GRPO) with high-quality single-step tool-use data to a 4B parameter model targeting a specific tool-call failure mode, then it will outperform a 235B parameter model on that task because the core performance gap is tool-use discipline rather than reasoning capacity, and fixing the specific failure mode generalizes to harder variants of the same task.

## What they did

Kobie Crawford from Snorkel presented research done in partnership with UC Berkeley's RLLM lab. The goal was to make a 4B model outperform a 235B model on a financial analysis tool-use benchmark (FinQA). They diagnosed that the failure mode was not reasoning but tool-call discipline — the small model was making incorrect or malformed tool invocations. They generated high-quality single-step tool-use training data, applied GRPO (a variant of RL), and trained exclusively on single-table questions. Results: the 4B model improved from ~14% to ~27% on single-table FinQA questions and from ~14% to ~27% on harder multi-table questions despite never training on multi-table data. They also tested curriculum learning (single-table first, then mixed) but found single-table-only training was best. The key insight: identifying the specific behavioral failure via rubric-based evals (breaking correctness into multiple sub-questions rather than binary pass/fail) pointed them to tool use as the root cause, not reasoning.

## Relevance to YOLO loop

Informs model selection strategy in the YOLO loop: before upgrading to a larger model when an agent fails at a structured task, diagnose whether the failure is tool-use discipline. If so, a fine-tuned smaller model may be cheaper and faster. The rubric-based eval approach is immediately adoptable for diagnosing loop failures.

## Notes

Backlog triage 2026-06-24 (owner-preference model). RL fine-tuning of a small model — GPU-heavy, off-focus, wrong hardware.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-11-small-model-tool-use-rl-training` |
| Channel | aie |
| Video | [Stop Making Models Bigger, Make Them Behave — Kobie Crawdord, Snorkel](https://www.youtube.com/watch?v=TNwJ1LMiENk) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Wire sub-agents into the LLM post-training pipeline for automated data curation and eval

> Back to [[experiments-index]]

Source: **[Production Sub-agents for LLM Post Training](https://www.youtube.com/watch?v=kPC4YOkIxVo)** · MLOps · 2026-04-10

**Status:** `discarded` · **Verdict:** `discarded` · **Effort:** `high`

---

## Hypothesis

If we deploy specialized sub-agents to handle discrete steps in the post-training pipeline such as data filtering, reward labeling, or evaluation, then we will reduce manual intervention and accelerate iteration cycles because sub-agents can parallelize and specialize work that is currently bottlenecked on human review.

## What they did

Speaker described a production architecture where LLM sub-agents are embedded in the post-training workflow, handling tasks like synthetic data generation, quality filtering, or automated evaluation scoring at scale.

## Relevance to YOLO loop

Core to YOLO Loop evolution; demonstrates how the loop itself can be partially automated using the agents it produces, creating a self-improving pipeline.

## Notes

Discarded 2026-04-12: YOLO loop does not do LLM fine-tuning or post-training. No infrastructure to apply this to.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-10 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-04-10-production-subagents-llm-posttraining` |
| Channel | MLOps |
| Video | [Production Sub-agents for LLM Post Training](https://www.youtube.com/watch?v=kPC4YOkIxVo) |
| Published | 2026-04-10 |
| Ingested upstream | 2026-04-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

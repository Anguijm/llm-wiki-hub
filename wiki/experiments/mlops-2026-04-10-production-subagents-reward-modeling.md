# Use a judge sub-agent to automate reward signal generation during RLHF or DPO runs

> Back to [[experiments-index]]

Source: **[Production Sub-agents for LLM Post Training](https://www.youtube.com/watch?v=kPC4YOkIxVo)** · mlops · 2026-04-10

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we replace or augment human preference labeling with a calibrated LLM judge sub-agent during post-training, then we can scale preference data collection by 10x at lower cost because LLM judges have shown strong correlation with human ratings on well-defined rubrics.

## What they did

Speaker likely covered reward modeling automation as part of the sub-agent post-training architecture, showing how LLM-as-judge patterns are operationalized in a production RLHF or DPO pipeline.

## Relevance to YOLO loop

Directly accelerates the feedback and evaluation phase of the YOLO Loop; reduces dependency on slow human-in-the-loop labeling steps.

## Notes

Discarded 2026-04-12: RLHF/DPO reward signal generation is out of scope. No fine-tuning pipeline exists.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-10 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-04-10-production-subagents-reward-modeling` |
| Channel | mlops |
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

# Replace fine-tuned intent classification with context-rich skills and system prompts on a frontier model

> Back to [[experiments-index]]

Source: **[Your Fine-Tuned Model Is Tech Debt: A 50x ROI House of Cards — Dan Bjornn, Lease End](https://www.youtube.com/watch?v=4loPnxvWWhg)** · aie · 2026-08-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we replace a fine-tuned classification model with a frontier model given structured skills, tools, and rich contextual resources (rather than fine-tuning), then accuracy will improve, fix cycle time will drop from days to under an hour, and total cost will decrease despite higher per-call API costs, because the bottleneck is context quality not model specialization.

## What they did

Dan Bjornn (senior data scientist, Lease End) built an LLM-based SMS customer communication system that classified user intent into 6 categories. Initial approach: RAG over a vector DB of classified messages, then fine-tuned smaller models for lower cost/latency. The fine-tuned model achieved 50x ROI ($12M revenue) but accumulated tech debt: fixing one regression caused others (whack-a-mole), fix cycles took ~1 week per iteration (data gathering → synthesis → validation → fine-tune → eval → regression check). After observing Claude Code's context-driven approach, they rebuilt using skills, tools, and markdown resources loaded as context into a frontier model — deployed by uploading MD files to S3. Results: accuracy went up, fix cycle dropped to under 1 hour, total cost went down (less maintenance time despite higher per-message API cost), and the system became model-agnostic. His final rule: 'Fine-tune only when you literally cannot call a frontier model, and even then your decision still has to beat the tax.'

## Relevance to YOLO loop

Directly applicable: before fine-tuning any model in our loop, test whether better context (skills files, structured prompts, resource loading) achieves the same accuracy. The S3-based MD file deployment pattern for updating agent behavior is immediately actionable.

## Notes

Fine-tuning justified only if: (1) privacy/data control prevents frontier model calls, or (2) offline requirement. All other common reasons (better accuracy, lower cost at volume, narrow structured task, vendor independence) were invalidated by their rebuild. The 'confused confirmer' and 'overeager puppy' failure modes illustrate how fine-tuned models fail on edge cases that context-rich prompts handle gracefully.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-20-fine-tuning-vs-context-engineering-lease-end` |
| Channel | aie |
| Video | [Your Fine-Tuned Model Is Tech Debt: A 50x ROI House of Cards — Dan Bjornn, Lease End](https://www.youtube.com/watch?v=4loPnxvWWhg) |
| Published | 2026-08-20 |
| Ingested upstream | 2026-08-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

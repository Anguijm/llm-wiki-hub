# Classify training and eval data as Type 1 (real workflow capture) vs Type 2 (contrived) and prefer Type 1 for fine-tuning

> Back to [[experiments-index]]

Source: **[State of Data — Sean Cai, Independent / State of Data](https://www.youtube.com/watch?v=ZyIoTOAbRfs)** · aie · 2026-07-27

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we source fine-tuning and eval data from real captured work trajectories (Type 1) rather than expert-manufactured examples (Type 2), then model performance on production tasks improves more efficiently because Type 1 data inherits realism from actual work structure, whereas Type 2 data biases the model toward idealized scenarios that diverge from messy real inputs.

## What they did

Sean Cai distinguished Type 1 data (pure capture of real workflows like GitHub commits or session replays, minimally shaped by non-experts) from Type 2 data (contrived examples manufactured by hired experts in artificial settings). He argued Type 2 is appropriate for bootstrapping low-capability models but Type 1 is required to push from 20% to 80% on domain tasks. He noted the industry dirty secret is that most vendors sell Type 2 while billing it as Type 1.

## Relevance to YOLO loop

When we build evals or fine-tuning sets for our agent loop, we should capture real session traces (inputs, tool calls, reasoning steps, outputs) from actual usage rather than constructing synthetic ideal examples — the loop itself is a Type 1 data source we are currently not harvesting.

## Notes

Sean's Antikythera mechanism concept — bespoke systems that translate messy business context into evals — is the infrastructure piece needed to make Type 1 data usable. The durable supply of Type 1 data is a live business process, not a static dataset.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-27-type1-vs-type2-data-pipeline-audit` |
| Channel | aie |
| Video | [State of Data — Sean Cai, Independent / State of Data](https://www.youtube.com/watch?v=ZyIoTOAbRfs) |
| Published | 2026-07-27 |
| Ingested upstream | 2026-07-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

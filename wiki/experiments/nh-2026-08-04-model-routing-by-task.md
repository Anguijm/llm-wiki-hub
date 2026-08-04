# Implement Model Routing to Match Task Complexity to Model Cost

> Back to [[experiments-index]]

Source: **[5000 Hours of Building AI in Just 17 Minutes](https://www.youtube.com/watch?v=7WZ6XldxX0U)** · nh · 2026-08-04

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we classify each step in our agent pipeline by cognitive complexity and route it to the cheapest model capable of handling that step, then we will reduce token costs by up to 10x without degrading output quality because grunt-work steps like summarization or extraction do not require frontier reasoning capacity.

## What they did

Nate described 'model routing' as a deliberate architectural pattern: every task in a pipeline is evaluated for how much reasoning it actually requires, then assigned to the cheapest model that meets that bar. He gave the example of using a fast cheap model like Haiku for bulk summarization of hundreds of thousands of words, while reserving an expensive frontier model only for the final strategic reasoning step that applies the summary to a business decision. He noted this approach can cut costs by 10x or more and will become increasingly powerful as local models improve.

## Relevance to YOLO loop

The YOLO loop makes many LLM calls across planning, execution, validation, and summarization steps. Mapping each loop phase to an appropriate model tier — cheap fast models for parsing logs and formatting outputs, expensive models for planning and error diagnosis — is a direct cost optimization that also speeds up the cheaper steps.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-04-model-routing-by-task` |
| Channel | nh |
| Video | [5000 Hours of Building AI in Just 17 Minutes](https://www.youtube.com/watch?v=7WZ6XldxX0U) |
| Published | 2026-08-04 |
| Ingested upstream | 2026-08-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Use structured XML tags in SFT data to reduce hallucination of specific values

> Back to [[experiments-index]]

Source: **[Data and Environment Curation for Post-Training LLMs — Mahesh Sathiamoorthy, Bespoke Labs](https://www.youtube.com/watch?v=ewtOo0scUh0)** · aie · 2026-07-31

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we add structured tags to prompt-response pairs in fine-tuning data (rather than plain-language Q&A), then the model will focus on form/pattern rather than memorizing specific numbers, reducing hallucination of factual values like rates or prices.

## What they did

When post-training a model for a financial use case (credit card recommendations), Bespoke Labs found the dataset had imbalanced coverage of specific numeric values (e.g., 0% APR), causing the fine-tuned model to hallucinate those numbers. They added structured tags to the training data so the model learned the response structure rather than specific numbers, which improved compliance metrics, latency, and throughput.

## Relevance to YOLO loop

Directly applicable when curating SFT data for any domain with factual values (prices, dates, IDs). Adding structural tags to training examples before fine-tuning could reduce hallucinations in our agent outputs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-31 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-31-curator-synthetic-data-pipeline` |
| Channel | aie |
| Video | [Data and Environment Curation for Post-Training LLMs — Mahesh Sathiamoorthy, Bespoke Labs](https://www.youtube.com/watch?v=ewtOo0scUh0) |
| Published | 2026-07-31 |
| Ingested upstream | 2026-07-31 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

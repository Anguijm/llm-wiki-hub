# Apply mid-training on curated domain-specific data to make post-training 2-3x more effective

> Back to [[experiments-index]]

Source: **[Data Quality Is the Compute Multiplier — Ari Morcos, DatologyAI](https://www.youtube.com/watch?v=_PdK6x7PQNM)** · aie · 2026-08-02

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we insert a mid-training phase on high-quality, domain-curated data between pre-training and post-training, then post-training gains will be 2-3x larger than post-training on the base model alone, because the model's policy starts from a much more accurate domain-specific prior, enabling better inference and reward signal utilization during RLHF/RLVR.

## What they did

Ari Morcos (CEO, DatologyAI) presented data quality as a compute multiplier: better data steepens the learning curve, achieving equivalent performance for 10x less compute. He described Datology's four-step data pipeline: Clean (heuristic filters, benchmark decontamination), Curate (quality classifiers, redundancy reduction, upsampling/downsampling by quality and relevance), Create (synthetic data generation), and Compose (mixing optimization across sources). Key finding: applying mid-training (domain-specific data fine-tuning) before post-training nearly tripled the gains from post-training compared to post-training the base instruction-tuned model directly. He cited the RCI model as a case study: competitive with open frontier models (matches GLM5 and Kimi, outperforms Claude on some tasks), trained on 17T curated public tokens for under $20M total including all iterations — by a team that had never trained a model before mid-2024.

## Relevance to YOLO loop

For teams fine-tuning models for specific YOLO loop tasks (code review, domain-specific generation), inserting a mid-training phase on curated domain data before RLHF/RLVR post-training could dramatically improve final model quality without increasing post-training compute budget.

## Notes

RCI benchmark: 17T tokens, <$20M total cost, competitive with open frontier. Mid-training 2-3x post-training multiplier finding is the key actionable result. Datology's principle: maximize marginal information gain per data point, not maximize token count.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-02-data-quality-compute-multiplier` |
| Channel | aie |
| Video | [Data Quality Is the Compute Multiplier — Ari Morcos, DatologyAI](https://www.youtube.com/watch?v=_PdK6x7PQNM) |
| Published | 2026-08-02 |
| Ingested upstream | 2026-08-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

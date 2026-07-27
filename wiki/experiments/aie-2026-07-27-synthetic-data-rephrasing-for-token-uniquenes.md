# Apply synthetic rephrasing to high-quality repeated data to prevent early saturation in fine-tuning

> Back to [[experiments-index]]

Source: **[The Messy Reality of Scale: Synthetic Data and Pre-Training — Marah Abdin & Robert McHardy, poolside](https://www.youtube.com/watch?v=KhYifX22yhE)** · aie · 2026-07-27

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we rephrase repeated high-quality seed examples into semantically equivalent variants before including them in a fine-tuning corpus, then model saturation on those examples is delayed and downstream eval performance improves because the model sees diverse surface forms of the same underlying knowledge rather than memorizing a fixed token sequence.

## What they did

Marah Abdin described poolside's finding that when scaling their Laguna models, high-quality data subsets hit repetition limits that caused the model to saturate too early. They implemented a rephrasing pipeline (multi-mode rephrasing plus specialized pipelines for STEM and code-to-text conversions) to replace repeated tokens with rephrasings, showing consistent eval improvement over the repeated-seed baseline in ablations. Synthetic data comprised 13% of their pre-training mix for Laguna XS point two.

## Relevance to YOLO loop

If we fine-tune or do continued pre-training on domain-specific examples (e.g., our agent's successful task traces), we should apply rephrasing augmentation to high-frequency patterns before training to avoid overfitting to surface form while preserving the underlying behavioral signal.

## Notes

Poolside frames all synthetic pipelines as composed of six components: seeds, primary inputs, metadata, secondary inputs, a generator function, and supplementary filters/validators. Using this modular framing helps scope pipeline complexity to the value of the target data type.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-27-synthetic-data-rephrasing-for-token-uniqueness` |
| Channel | aie |
| Video | [The Messy Reality of Scale: Synthetic Data and Pre-Training — Marah Abdin & Robert McHardy, poolside](https://www.youtube.com/watch?v=KhYifX22yhE) |
| Published | 2026-07-27 |
| Ingested upstream | 2026-07-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

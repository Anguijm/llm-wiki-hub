# Audit training data curation pipeline for unintentional stylistic diversity loss

> Back to [[experiments-index]]

Source: **[Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai](https://www.youtube.com/watch?v=-tviRdpmHvs)** · aie · 2026-08-18

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we audit and adjust data filtering steps to avoid unintentionally removing stylistically diverse samples, then output diversity across generated images will improve because mode collapse in generative models is often caused by overcleaning data toward a narrow aesthetic rather than model architecture choices.

## What they did

Sangwu Lee described how Krea prioritized stylistic diversity when training Krea 2, noting that a major risk during data curation is inadvertently filtering out stylistically diverse data. He emphasized that after locking in architecture, the vast majority of impactful work is in data curation, and that data is 'quite everything' — more durable and impactful than code or hyperparameter changes. He contrasted Krea's approach against production models like ChatGPT image gen and Ideogram which trade diversity for reliability, leading to mode-collapsed outputs (e.g., always rendering a 'boring average person centered in frame').

## Relevance to YOLO loop

Directly relevant if we are fine-tuning or training any generative model in the loop. Applies as a checkpoint: review what our data filtering removes and whether it biases outputs toward a narrow style, especially if we care about creative or diverse generation outputs.

## Notes

Speaker also noted that data quality/curation is more eternal and valuable than code, since code is easy to change but good curated datasets retain value across training paradigms.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-18-stylistic-diversity-data-curation` |
| Channel | aie |
| Video | [Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai](https://www.youtube.com/watch?v=-tviRdpmHvs) |
| Published | 2026-08-18 |
| Ingested upstream | 2026-08-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

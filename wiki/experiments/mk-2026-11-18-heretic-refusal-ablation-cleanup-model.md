# Run Heretic on the Push to Talk cleanup model against an untouched control

> Back to [[experiments-index]]

Source: **[This Skill Lets You Uncensor Any AI Model](https://www.youtube.com/watch?v=jfC6_biJ4Q8)** · mk · 2026-11-18

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run the open-source Heretic toolkit on the local cleanup model, giving it examples of dictation the model refuses or lectures about, then unwanted refusals and commentary will drop while cleanup quality stays level, because Heretic dampens the weights responsible for refusal.

## What they did

Mark kept an unmodified copy of a local Qwen model as a control, gave Heretic example prompts the model refused or answered in an unwanted style, and let it find and reduce the weights responsible. He then compared the modified model with the control on benchmark prompts to check for quality degradation, noting that touching too many weights harms quality.

## Relevance to YOLO loop

medium: Weight-level behavior steering is a new technique, but it only matters where the operator hosts the model.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-21 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-11-18-heretic-refusal-ablation-cleanup-model` |
| Channel | mk |
| Video | [This Skill Lets You Uncensor Any AI Model](https://www.youtube.com/watch?v=jfC6_biJ4Q8) |
| Published | 2026-11-18 |
| Ingested upstream | 2026-11-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

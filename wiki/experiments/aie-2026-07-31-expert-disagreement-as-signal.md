# Distinguish meaningful expert disagreement from data noise during human QA of preference data

> Back to [[experiments-index]]

Source: **[Ending AI Slop — Thais Castello Branco, Taste Labs](https://www.youtube.com/watch?v=lCBf9slCanI)** · aie · 2026-07-31

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we classify expert disagreements in preference labeling as either noise (disagreement on objective criteria like alignment) or signal (disagreement on stylistic preference), then we can preserve diverse taste signal in our training data rather than filtering it out, producing models that better handle plurality of subjective preferences.

## What they did

Taste Labs described running human QA on preference data for subjective domains. They found that when two experts disagree, the nature of the disagreement matters: disagreement on objective properties (e.g., visual alignment) indicates bad data and should be filtered; disagreement on style or aesthetics is valid signal showing genuine taste diversity and should be preserved. They use specificity of expert language as a proxy for data quality, and tie expert commentary to specific code components to reduce noise.

## Relevance to YOLO loop

When building preference datasets for our loop, adding a disagreement classification step to human QA—labeling whether disagreements are objective errors or subjective taste differences—will prevent over-filtering and improve the diversity of the reward model.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-31 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-31-expert-disagreement-as-signal` |
| Channel | aie |
| Video | [Ending AI Slop — Thais Castello Branco, Taste Labs](https://www.youtube.com/watch?v=lCBf9slCanI) |
| Published | 2026-07-31 |
| Ingested upstream | 2026-07-31 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

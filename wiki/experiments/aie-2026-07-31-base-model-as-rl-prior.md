# Design pre-training data mix to build atomic skills for RL rather than broad web knowledge

> Back to [[experiments-index]]

Source: **[The Base Model Is Dead — Varun Singh, Arcee AI](https://www.youtube.com/watch?v=xbPriQWXtWM)** · aie · 2026-07-31

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we shift pre-training (or mid-training) data away from general web text and toward code, STEM, and reasoning traces, then RL post-training will be more sample-efficient and reach higher performance, because the base model needs exposure to atomic skills it will compose during RL exploration.

## What they did

Arcee AI's pre-training lead described how the role of base models has shifted: web text has dropped from ~85% of training mix (GPT-3) to ~15% (some recent models), replaced by code, STEM, and synthetic SFT data. He cited research showing base models need prior exposure to atomic skills for RL to extrapolate effectively. He also described mid-training as a stage that exposes the model to the RL distribution (longer context, agentic traces) before full RL begins. Some labs (e.g., Cohere) now allocate equal or greater compute to RL than supervised learning.

## Relevance to YOLO loop

When selecting or fine-tuning a base model for our loop, auditing whether its pre-training mix includes sufficient code and reasoning trace coverage—and supplementing with mid-training if not—could significantly improve downstream RL results.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-31 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-31-base-model-as-rl-prior` |
| Channel | aie |
| Video | [The Base Model Is Dead — Varun Singh, Arcee AI](https://www.youtube.com/watch?v=xbPriQWXtWM) |
| Published | 2026-07-31 |
| Ingested upstream | 2026-07-31 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

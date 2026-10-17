# Characterise our fine-tuning use cases on the narrow-task vs. general-agent spectrum before choosing SFT or RL

> Back to [[experiments-index]]

Source: **[Why Nobody Has Solved Continual Learning](https://www.youtube.com/watch?v=whnDiwcL4HE)** · lc · 2026-10-16

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we explicitly place each fine-tuning objective on the narrow-task (stationary distribution, SFT-friendly) to general-agent (shifting distribution, RL-required) spectrum before starting a training run, then we will avoid wasting compute on the wrong method and reduce catastrophic forgetting incidents, because the SFT vs. RL tradeoff is determined almost entirely by task distribution stationarity.

## What they did

The LangChain speaker gave a detailed breakdown of why neither continual SFT nor continual RL alone is sufficient. SFT provides dense off-policy signal but fails when the model makes one misstep it was never trained to recover from (DAgger problem). RL is on-policy and avoids this but cannot teach behaviours outside the model's current support. The practical heuristic: narrow, stationary tasks (clinical notes, voice extraction) → SFT on gold traces; general agentic tasks → RL environments, possibly with mid-training SFT to bootstrap; most real cases sit in the middle and need a calibrated ratio of both.

## Relevance to YOLO loop

medium: informs decisions if we ever fine-tune a local model for Push to Talk or any other project where we want the model to improve from usage traces.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `lc-2026-10-16-continual-learning-sft-rl-tradeoff` |
| Channel | lc |
| Video | [Why Nobody Has Solved Continual Learning](https://www.youtube.com/watch?v=whnDiwcL4HE) |
| Published | 2026-10-16 |
| Ingested upstream | 2026-10-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

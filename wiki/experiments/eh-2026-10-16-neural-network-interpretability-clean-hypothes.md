# Apply the 'describe without nouns' interpretability heuristic when debugging unexpected agent behaviour

> Back to [[experiments-index]]

Source: **[AI's insides may not be a tangled mess after all (a new hypothesis, explained)](https://www.youtube.com/watch?v=z-cb8eem2HE)** · eh · 2026-10-16

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we describe unexpected agent outputs or intermediate reasoning steps in terms of abstract patterns rather than surface-level categories, then we will find simpler unifying explanations for apparently random behaviour because the underlying model representations tend to encode geometric or structural features that cross-cut human category labels.

## What they did

Nick Camarada at Goodfire proposed the working hypothesis that neural network neurons are far more readable than previously assumed, and that the apparent mess came from bad microscopes and old model designs rather than fundamental superposition. His practical heuristic: when a neuron (or agent behaviour) looks like a random mix, describe the stimulus without nouns—ask what shape or abstract property they share. Applied this to the famous cats-and-cars neuron and immediately found it was a V-shape detector.

## Relevance to YOLO loop

medium: useful when debugging why a Claude Code agent produces unexpected outputs—applying the 'what abstract property links these cases' heuristic before assuming the model is broken.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `eh-2026-10-16-neural-network-interpretability-clean-hypothesis` |
| Channel | eh |
| Video | [AI's insides may not be a tangled mess after all (a new hypothesis, explained)](https://www.youtube.com/watch?v=z-cb8eem2HE) |
| Published | 2026-10-16 |
| Ingested upstream | 2026-10-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

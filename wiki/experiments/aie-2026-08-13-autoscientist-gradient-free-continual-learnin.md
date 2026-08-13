# Evaluate Auto-Scientist for Automated Model Training Pipeline Optimization

> Back to [[experiments-index]]

Source: **[Adaption Labs: Gradient-Free Continual Learning — Sara Hooker, Adaption](https://www.youtube.com/watch?v=XEd_SRVHBgU)** · aie · 2026-08-13

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use an AutoScientist-style system that co-optimizes the full training loop (data selection, alignment, architecture search) without requiring manual researcher intervention, then model training quality on domain-specific tasks will match or exceed expert-tuned baselines because the system searches across architectures and data types simultaneously rather than relying on researcher heuristics.

## What they did

Sara Hooker described Adaption Labs' AutoScientist system, which automates the training of models by co-optimizing the entire loop from data to alignment, self-evolving based on domain and data type. She reported it outperforms research staff across multiple model architectures (dense and MoE, varying sizes) because staff expertise is narrowly specialized. The system is available in beta with free GPU access.

## Relevance to YOLO loop

Could replace or augment manual fine-tuning steps in the YOLO loop: instead of hand-selecting training data and hyperparameters for task-specific model adaptation, AutoScientist could run the search automatically when a new domain or task is introduced.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-13-autoscientist-gradient-free-continual-learning` |
| Channel | aie |
| Video | [Adaption Labs: Gradient-Free Continual Learning — Sara Hooker, Adaption](https://www.youtube.com/watch?v=XEd_SRVHBgU) |
| Published | 2026-08-13 |
| Ingested upstream | 2026-08-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

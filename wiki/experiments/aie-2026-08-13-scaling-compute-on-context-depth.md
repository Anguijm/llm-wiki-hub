# Apply Iterative Self-Improving Synthetic Training to Encode Private Domain Depth

> Back to [[experiments-index]]

Source: **[Scaling Compute on Context — Jack Morris, Engram](https://www.youtube.com/watch?v=WiqDvX6isc4)** · aie · 2026-08-13

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we iteratively generate synthetic training data from a private domain corpus, train the model on it, use the improved model to generate harder/better synthetic data, and repeat, then the model will develop progressively deeper knowledge of that private domain without hitting the saturation plateau of single-pass synthetic data generation, because self-improvement creates a curriculum that scales with model capability.

## What they did

Jack Morris framed the core problem as models only scaling on public data, lacking depth in private or long-tail domains. He surveyed approaches (continued pre-training, attention matching, self-study distillation, unsupervised RL) and noted all hit a saturation ceiling because the synthetic dataset is fixed. He argued the missing component is self-improvement: the model generates training data, gets better, then generates harder data recursively — analogous to AlphaGo's self-play. Ngram is pursuing curves that avoid plateau by making training progressively harder.

## Relevance to YOLO loop

Directly relevant to YOLO loop model specialization: after initial fine-tuning on a codebase or domain, a self-improving synthetic data loop could continue to deepen the model's understanding of project-specific patterns without requiring new human-labeled data.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-13-scaling-compute-on-context-depth` |
| Channel | aie |
| Video | [Scaling Compute on Context — Jack Morris, Engram](https://www.youtube.com/watch?v=WiqDvX6isc4) |
| Published | 2026-08-13 |
| Ingested upstream | 2026-08-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

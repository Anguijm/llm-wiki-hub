# Apply Item Response Theory to internal evals to get per-model theta scores and detect item noise

> Back to [[experiments-index]]

Source: **[Stop Evaluating Models Like It's the 50s - Alejandro Vidal, Mindmakers](https://www.youtube.com/watch?v=EfcfUB2uprc)** · aie · 2026-07-12

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we apply IRT (Item Response Theory) psychometric modeling to our internal eval suite—estimating per-item difficulty (B) and discrimination (A) and per-model latent ability (theta)—then we will identify noisy or negatively discriminating eval items, get a stable model ranking that is robust to benchmark saturation, and detect when two models with identical accuracy scores have meaningfully different capability profiles, because IRT preserves the full answer-pattern matrix rather than collapsing it to a single accuracy number.

## What they did

Alejandro Vidal (Mindmakers) argued that standard benchmark accuracy (sum of correct answers, equal-weighted) is a weak estimator because it assumes all items are equally informative and ignores item-level patterns. He presented IRT (2-parameter logistic model) applied to LLM benchmarks: (1) estimate B (difficulty) and A (discrimination slope) for each item; (2) estimate theta (latent ability on the same scale as B) for each model via maximum likelihood over its full answer vector, with a confidence interval for free; (3) use discrimination A to audit items—flat curves are noise, inverted curves are harmful, steep curves are informative; (4) use residual vectors (model answers minus IRT prediction) as fingerprints to detect distillation relationships and model families. He showed two models with identical benchmark scores but one standard deviation apart in theta, and identified model-family clusters in residual correlation matrices.

## Relevance to YOLO loop

We run evals to decide which model to use for each agent task. Replacing raw accuracy with IRT-derived theta would let us (a) prune our eval suite of noisy items, (b) detect when a new model is genuinely better vs just hitting easy items we already weight, and (c) build a more stable model-selection signal for our routing layer.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-12-irt-llm-benchmark-evaluation` |
| Channel | aie |
| Video | [Stop Evaluating Models Like It's the 50s - Alejandro Vidal, Mindmakers](https://www.youtube.com/watch?v=EfcfUB2uprc) |
| Published | 2026-07-12 |
| Ingested upstream | 2026-07-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

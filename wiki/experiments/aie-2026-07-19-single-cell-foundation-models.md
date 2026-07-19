# Benchmark flow-matching models against autoencoder-based models for single-cell RNA-seq generation

> Back to [[experiments-index]]

Source: **[From Tokens to Cells: Foundation Models for Single-Cell Biology - Akram Baharlouei, Altos Labs](https://www.youtube.com/watch?v=-561cZmir5Q)** · aie · 2026-07-19

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we apply flow-matching generative models (e.g. PrimeFlow) to single-cell RNA-seq data instead of transformer autoencoder-based foundation models, then distribution prediction quality will improve as measured by MMD score, because flow matching learns to match the full data distribution rather than compressing to a latent vector that loses information and regresses to the mean.

## What they did

Speaker from Altos Labs reviewed the current state of single-cell foundation models, noting that despite expensive training, transformer-based autoencoder models often underperform simple linear baselines on benchmarks (validated by two NeurIPS 2024 papers). He then presented PrimeFlow, a flow-matching model that predicts the distribution of single-cell data starting from Gaussian noise, and showed it better matches ground-truth cell distributions (green dots) compared to CPA/autoencoder models that collapse to predicting the mean. Results measured via MMD score. Context: single-cell RNA-seq data has ~20,000 gene dimensions per cell.

## Relevance to YOLO loop

Peripheral — relevant if the YOLO loop incorporates bioinformatics or scientific ML pipelines. The core lesson (distribution-matching models outperform compression-based models on sparse high-dimensional biological data) could inform architecture choices for any high-dimensional sparse embedding task in the loop.

## Notes

Primary domain is computational biology / drug discovery, not AI dev tooling. Actionable only for teams building scientific ML pipelines. Papers referenced: SCGENE/SCOPE, perturbation benchmarking (NeurIPS), PrimeFlow (arXiv).

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-19-single-cell-foundation-models` |
| Channel | aie |
| Video | [From Tokens to Cells: Foundation Models for Single-Cell Biology - Akram Baharlouei, Altos Labs](https://www.youtube.com/watch?v=-561cZmir5Q) |
| Published | 2026-07-19 |
| Ingested upstream | 2026-07-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

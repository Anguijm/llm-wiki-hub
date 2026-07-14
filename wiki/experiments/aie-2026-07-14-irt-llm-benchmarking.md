# Apply Item Response Theory to Internal Agent Evals to Get Calibrated Model Intelligence Scores

> Back to [[experiments-index]]

Source: **[Stop Evaluating Models Like It's the 50s - Alejandro Vidal, Mindmakers](https://www.youtube.com/watch?v=O3FEoMYvUf8)** · aie · 2026-07-14

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we apply Item Response Theory (IRT) to our agent eval benchmark instead of raw accuracy averaging, then we will get calibrated per-question difficulty scores and model intelligence estimates with confidence intervals, because IRT accounts for question difficulty and discrimination rather than treating all questions as equally weighted.

## What they did

Alejandro Vidal (Mindmakers) demonstrated applying IRT — standard in psychometrics for IQ tests — to LLM benchmarking using real epoch.ai data. Each benchmark question gets a B parameter (difficulty, normally distributed) and an A parameter (discrimination — how well it differentiates model ability). Each model gets a theta (estimated intelligence level). This enables: confidence intervals on model ability estimates, detection of mislabeled or negatively-discriminating questions, differential item functioning to detect benchmark bias between open/closed-weight models, and model fingerprinting via residual correlation matrices to detect distillations or model family relationships. He released datasets, code, and benchmarks for public use.

## Relevance to YOLO loop

If we run internal evals to choose which model to use in our loop, replacing accuracy averages with IRT-calibrated scores would give us more reliable model selection, especially for detecting regressions or choosing between closely-scored models. High effort but high rigour.

## Notes

Speaker released all materials publicly; links in video description. Meta-Benchmark paper recommended as companion reading.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-14-irt-llm-benchmarking` |
| Channel | aie |
| Video | [Stop Evaluating Models Like It's the 50s - Alejandro Vidal, Mindmakers](https://www.youtube.com/watch?v=O3FEoMYvUf8) |
| Published | 2026-07-14 |
| Ingested upstream | 2026-07-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

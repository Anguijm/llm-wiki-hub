# Generate Synthetic Training Data by Reversing the Inference Workflow

> Back to [[experiments-index]]

Source: **[Don't be data poor — Anuj Iravane, Anterior](https://www.youtube.com/watch?v=XAsb7MIAzm8)** · aie · 2026-08-19

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we reverse our forward inference pipeline by first sampling a label and reasoning trace then generating the input data backwards, then we can produce diverse, realistic synthetic examples without needing to retain real sensitive data, because conditioning generation on diverse sampled labels circumvents the mode-collapse problem LLMs exhibit when asked to generate inputs directly.

## What they did

Anterior needed eval datasets for healthcare workflows (prior auth, HEDIS, payment integrity) but could not retain PHI. They built a synthetic data pipeline that inverts the forward task: instead of (document → policy → reasoning → label), they sample a random outcome label, derive a plausible reasoning trace for it, then generate synthetic medical record documents backwards from that trace. They modeled the pipeline as a skills-based workflow on their internal agent harness so clinicians — not engineers — own and extend each stage (patient journey generation, document generation, enrichment, evals). In blind review, clinicians distinguished synthetic from real only 60% of the time. Roughly 90% of their eval datasets are now synthetic, enabling just-in-time dataset creation before customer go-lives.

## Relevance to YOLO loop

Directly applicable to any situation where we lack labeled examples for a new task or cannot retain sensitive user data. The reverse-inference pattern can bootstrap eval sets for new agent capabilities before real production data accumulates.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-19-reverse-inference-synthetic-data` |
| Channel | aie |
| Video | [Don't be data poor — Anuj Iravane, Anterior](https://www.youtube.com/watch?v=XAsb7MIAzm8) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

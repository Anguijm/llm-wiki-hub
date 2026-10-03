# Use High-Quality Document Rephrasing to Generate Synthetic Fine-Tuning Data Instead of Free-Form Generation

> Back to [[experiments-index]]

Source: **[Lessons from Generating 12 Trillion Synthetic Tokens — Bogdan Gaza, DatologyAI](https://www.youtube.com/watch?v=FQwTqUmcbRg)** · aie · 2026-10-03

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we generate synthetic training data by identifying the highest-quality documents in our corpus and rephrasing/restructuring them rather than prompting a model to generate from scratch, then the synthetic data will more accurately reflect the target distribution and require fewer tokens to reach equivalent model performance because seeding with real high-quality examples avoids learning only the mode of the generator model's distribution.

## What they did

Bogdan Gaza of DatologyAI described their 'Beyond Web' synthetic data recipe. Rather than prompting a model with 'give me a synthetic data point,' they identify the highest-quality documents in a customer's dataset, then rephrase or restructure those documents through their pipeline. Results showed training to equivalent benchmark accuracy with 2.7x–5.3x fewer tokens than Neotron Synth and Cosmopedia baselines, and a 3B parameter model matching 8B performance when trained on their synthetic data. They completed a 12-trillion-token run (web + math + code) using this approach.

## Relevance to YOLO loop

Relevant if we do any fine-tuning or mid-training. The rephrasing-over-generation principle also applies to smaller-scale data augmentation for RAG corpora or few-shot example sets—seeding with our best real examples and rephrasing them likely beats generating examples from scratch.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-03-datology-synthetic-data-rephrase` |
| Channel | aie |
| Video | [Lessons from Generating 12 Trillion Synthetic Tokens — Bogdan Gaza, DatologyAI](https://www.youtube.com/watch?v=FQwTqUmcbRg) |
| Published | 2026-10-03 |
| Ingested upstream | 2026-10-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

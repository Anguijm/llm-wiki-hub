# Curate high-quality reasoning traces using Curator for open-source SFT datasets

> Back to [[experiments-index]]

Source: **[Data and Environment Curation for Post-Training LLMs — Mahesh Sathiamoorthy, Bespoke Labs](https://www.youtube.com/watch?v=ewtOo0scUh0)** · aie · 2026-07-31

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use a structured data curation pipeline (like Bespoke Curator) to generate and filter reasoning traces from prompts, then the resulting SFT dataset will produce stronger reasoning models than training on raw or unfiltered data because quality filtering at curation time compounds with training.

## What they did

Bespoke Labs built the Curator tool to take prompt sets (from HuggingFace or internal logs) and generate responses via inference providers (Fireworks, Together, etc.), then used it to curate the Open Thoughts reasoning dataset after DeepSeek R1 was released. The dataset and paper were released open-source and formed the basis for community reasoning model efforts.

## Relevance to YOLO loop

If we want to fine-tune a smaller model for a specific reasoning task in our loop, using Curator to systematically generate and filter SFT traces is a concrete starting point.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-31 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-31-open-thoughts-reasoning-data` |
| Channel | aie |
| Video | [Data and Environment Curation for Post-Training LLMs — Mahesh Sathiamoorthy, Bespoke Labs](https://www.youtube.com/watch?v=ewtOo0scUh0) |
| Published | 2026-07-31 |
| Ingested upstream | 2026-07-31 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

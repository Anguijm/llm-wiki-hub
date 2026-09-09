# Benchmark our skills files against IFScale to find the real instruction-following ceiling for our chosen model

> Back to [[experiments-index]]

Source: **[How long can your skills be before your agent forgets what you told it? — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=XzJD1bvXKjs)** · aie · 2026-09-09

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run our production skills files through an IFScale-style keyword-inclusion benchmark across our candidate models, then we will discover the practical instruction count at which compliance degrades, allowing us to right-size skills files and catch silent failures before they reach production, because frontier models went from ~200 to ~2,000 followable instructions in one year but compliance is still sensitive to instruction ordering.

## What they did

Laurie Voss (Arize AI, ex-npm) investigated the claim that agents can follow ~200 instructions before forgetting. He replicated the IFScale benchmark (ask the model to write a report containing N exact keywords; measure what fraction appear) on the three models from the original paper still available via API: GPT-4.1, Claude Sonnet 4, and Gemini 2.5 Pro. Results confirmed the original finding for year-old models. He then ran the same benchmark on newer models and found the ceiling had moved by roughly 10x — current frontier models can track ~2,000 discrete instructions. However, a subsequent paper ('Revisiting the Reliability of Language Models in Instruction Following', 46 models) showed that models can ace the benchmark yet fail badly when the same instructions are reworded or reordered, meaning capacity is up but reliability is still fragile. Total cost for 2,300 API calls across 7 models: $29.

## Relevance to YOLO loop

Directly informs how large we can make our system prompts and skills files without silent degradation. The ordering-sensitivity finding suggests we should also test prompt variants, not just prompt length, as part of our eval suite.

## Notes

Code and data published to GitHub (QR in talk). Related benchmarks: IFScale, Firebench, CCRBench, GuideBench. Key takeaway: the compression problem (fitting instructions) is largely solved; the new problem is verification (did it actually follow them?), which requires output evals, not just prompt engineering.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-09-ifscale-instruction-following-ceiling` |
| Channel | aie |
| Video | [How long can your skills be before your agent forgets what you told it? — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=XzJD1bvXKjs) |
| Published | 2026-09-09 |
| Ingested upstream | 2026-09-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

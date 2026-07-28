# Build a staged pipeline from raw request to shipped feature with agents at each step and evals between stages

> Back to [[experiments-index]]

Source: **[How Forward Deployed Engineering is done at Ramp — Leo Mehr](https://www.youtube.com/watch?v=ITMXwI6QL6A)** · aie · 2026-07-28

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we decompose the intake-to-ship workflow into discrete agentic stages (scoping → spec generation → implementation → validation) with quality evals and rubrics between each stage, then we can scale engineering throughput without proportional headcount growth, because frontier models can already one-shot medium-sized features from a well-formed spec and the bottleneck is spec quality.

## What they did

Leo described Ramp's vision of a full agentic pipeline: stage 1 is the multi-turn scoping agent (already built), stage 3 is frontier-model code generation from a well-shaped spec (already working), and stage 2 — transforming a rough request into a well-shaped spec — is the hard unsolved middle. He described investing in evals, rubrics, and human feedback to validate output quality at each stage, and mentioned that agent context (product knowledge, historical data, PM institutional knowledge from Notion docs) is the key unresolved challenge for the middle stage.

## Relevance to YOLO loop

This is a blueprint for the full YOLO loop as a factory. The insight that the spec-shaping middle stage is the hardest is directly actionable — we should invest eval infrastructure there first.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-28-ramp-agentic-spec-pipeline` |
| Channel | aie |
| Video | [How Forward Deployed Engineering is done at Ramp — Leo Mehr](https://www.youtube.com/watch?v=ITMXwI6QL6A) |
| Published | 2026-07-28 |
| Ingested upstream | 2026-07-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

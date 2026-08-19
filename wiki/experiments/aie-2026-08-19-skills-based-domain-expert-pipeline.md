# Model Data Pipelines as Skill Files on an Agent Harness So Domain Experts Own Them

> Back to [[experiments-index]]

Source: **[Don't be data poor — Anuj Iravane, Anterior](https://www.youtube.com/watch?v=XAsb7MIAzm8)** · aie · 2026-08-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we represent each stage of a data or eval pipeline as a discrete skill file executed by a generic agent harness, then domain experts can add, modify, or replace pipeline stages without engineering involvement, because the interface between AI logic and domain knowledge becomes a declarative skill definition rather than embedded code.

## What they did

Anterior modeled their entire synthetic data generation pipeline — patient journey generation, document generation, enrichment, and evals — as individual skills running on an internal agent harness. A clinician who wanted to add support for a new document type (e.g., intake forms for a new customer) could create a new skill file and attach it to the pipeline without any engineering changes. This pattern also appears in their production workflows. They argue skills are the ideal interface between AI engineers and domain experts in vertical AI.

## Relevance to YOLO loop

Relevant to making our eval and data pipelines extensible by non-engineers. Adopting a skill-file abstraction over our agent harness would let us iterate faster on domain-specific steps without engineering bottlenecks.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-19-skills-based-domain-expert-pipeline` |
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

# Decompose subjective quality criteria into context-specific verifiable components for reward design

> Back to [[experiments-index]]

Source: **[Ending AI Slop — Thais Castello Branco, Taste Labs](https://www.youtube.com/watch?v=lCBf9slCanI)** · aie · 2026-07-31

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we decompose fuzzy subjective quality goals (e.g., 'great design') into explicit, context-specific, verifiable components (brand colors, typography rules, spacing constraints), then we can build reliable reward signals and preference data for subjective domains, because measurability is the bottleneck for capability in these areas.

## What they did

Taste Labs argued that AI capability closely follows measurability, and that subjective domains (design, writing, personality) lag because they lack decomposable verification. Their approach: take a brand guide and decompose it into codified components (color palette, typography, motion, texture), then verify generated outputs against each component. This converts 'is this on-brand?' from a fuzzy question into a set of checkable conditions. They also described tying expert commentary to specific code components (rather than free-form paragraphs) to produce cleaner preference data.

## Relevance to YOLO loop

Anywhere our loop produces outputs judged subjectively (UX copy, design artifacts, tone of voice), decomposing the rubric into explicit verifiable sub-criteria before collecting preference data will yield cleaner reward signals for RLHF or evals.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-31 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-31-subjective-domain-measurability` |
| Channel | aie |
| Video | [Ending AI Slop — Thais Castello Branco, Taste Labs](https://www.youtube.com/watch?v=lCBf9slCanI) |
| Published | 2026-07-31 |
| Ingested upstream | 2026-07-31 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

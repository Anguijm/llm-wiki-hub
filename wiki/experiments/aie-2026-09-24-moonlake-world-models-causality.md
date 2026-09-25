# Add Causal Structure to Agent World Model Representations

> Back to [[experiments-index]]

Source: **[World Models Need Causality, Not Pretty Pixels — Christopher Manning, Moonlake AI](https://www.youtube.com/watch?v=4Gqg0HVe-AY)** · aie · 2026-09-24

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we represent world state in our agent's context using causal graphs rather than flat descriptions or pixel-level observations, then downstream planning and action selection will be more robust because causal representations generalize better under distribution shift.

## What they did

Christopher Manning argued that current world models focus on perceptual fidelity (pretty pixels) but lack causal structure, and described Moonlake AI's approach to building world models with explicit causal relationships that support better reasoning and generalization.

## Relevance to YOLO loop

Our agents currently represent world state as flat text or embeddings; this suggests an experiment where we restructure context as a causal graph and test whether planning quality improves on multi-step tasks.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-24-moonlake-world-models-causality` |
| Channel | aie |
| Video | [World Models Need Causality, Not Pretty Pixels — Christopher Manning, Moonlake AI](https://www.youtube.com/watch?v=4Gqg0HVe-AY) |
| Published | 2026-09-24 |
| Ingested upstream | 2026-09-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

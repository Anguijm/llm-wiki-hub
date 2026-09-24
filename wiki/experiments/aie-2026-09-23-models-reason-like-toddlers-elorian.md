# Audit Frontier Model Reasoning Failures Using Toddler-Style Edge Cases

> Back to [[experiments-index]]

Source: **[The Best Models Still Reason Like Toddlers — Andrew Dai, Elorian](https://www.youtube.com/watch?v=A_I8mw8yfns)** · aie · 2026-09-23

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we probe frontier models with reasoning tasks that expose developmental-stage failures (analogical, causal, counterfactual reasoning), then we can systematically identify where even SOTA models break down because current training regimes produce surface-level reasoning mimicry rather than genuine causal understanding.

## What they did

Andrew Dai from Elorian presented evidence that top frontier models still fail at reasoning tasks trivial for adult humans, characterizing the failure modes and suggesting evaluation frameworks to expose them.

## Relevance to YOLO loop

Directly useful for designing our evaluation harness — adding toddler-style reasoning probes to our model selection benchmarks will catch brittle reasoning before we deploy a model in a critical loop step.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-23-models-reason-like-toddlers-elorian` |
| Channel | aie |
| Video | [The Best Models Still Reason Like Toddlers — Andrew Dai, Elorian](https://www.youtube.com/watch?v=A_I8mw8yfns) |
| Published | 2026-09-23 |
| Ingested upstream | 2026-09-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

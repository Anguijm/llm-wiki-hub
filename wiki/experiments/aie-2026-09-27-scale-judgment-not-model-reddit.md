# Build a lightweight judgment layer that evaluates and routes agent outputs rather than scaling model size

> Back to [[experiments-index]]

Source: **[Scale the Judgment, Not the Model — Andrew Orobator, Reddit](https://www.youtube.com/watch?v=6MudaeKdBSk)** · aie · 2026-09-27

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we invest in a structured judgment layer that evaluates agent outputs against explicit criteria before acceptance, then output quality scales without requiring larger or more expensive models because good judgment about outputs is separable from the capability to produce them.

## What they did

Andrew Orobator from Reddit argued that the leverage point in AI systems is not the model itself but the judgment infrastructure around it—routing, evaluation, and decision logic—and showed how Reddit scales AI impact by scaling judgment rather than model size.

## Relevance to YOLO loop

High relevance: the YOLO loop currently relies on tests as the judgment layer. This suggests investing more explicitly in a richer judgment/evaluation step that can catch subtler failures before they propagate.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-27-scale-judgment-not-model-reddit` |
| Channel | aie |
| Video | [Scale the Judgment, Not the Model — Andrew Orobator, Reddit](https://www.youtube.com/watch?v=6MudaeKdBSk) |
| Published | 2026-09-27 |
| Ingested upstream | 2026-09-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

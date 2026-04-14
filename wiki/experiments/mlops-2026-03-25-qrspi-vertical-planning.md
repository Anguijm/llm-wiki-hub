# Adopt vertical planning with structure outlines before coding

> Back to [[experiments-index]]

Source: **[Everything We Got Wrong About Research-Plan-Implement - Dexter Horthy](https://www.youtube.com/watch?v=YwZR6tc7qYg)** · @MLOps · 2026-03-25

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we add a structure outline phase (define signatures, types, interfaces before implementation) and plan vertically (small testable slices from data to UI), then we reduce rework because mistakes are caught at the design level before code is written.

## What they did

Dexter Horthy found RPI (Research-Plan-Implement) fails at scale due to horizontal planning and mega-prompts exceeding instruction budgets (~150-200 max). QRSPI adds objective research (hide the task from researcher), design docs (~200 lines for alignment), structure outlines (signatures/types first), and vertical slicing.

## Actionable steps

- Before the next YOLO build, write a 10-line structure outline (key functions, their signatures, data flow)
- Plan vertically: build one thin slice end-to-end before expanding
- Keep individual prompts under 150 instructions
- Review code not plans — skip lengthy plan review, read the actual output

## Success metric

Next 3 builds have zero structural rework (no rewriting core architecture after initial implementation).

## Relevance to YOLO loop

The YOLO builder currently goes from idea straight to code. Adding a lightweight structure outline could prevent the architectural bugs that Gemini catches in review.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

Built env-diff with structure outline first (types, signatures, DOM IDs). Zero rework, 7/7 tests on first try, 52 second build. Compare to shader-forge (same session, no outline): 3 rounds of fixes needed. Outline prevents mid-build data model discovery.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-02 | `done` | env-diff built with outline-first method. Zero rework vs 3 fix rounds without outline. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-03-25-qrspi-vertical-planning` |
| Channel | @MLOps |
| Video | [Everything We Got Wrong About Research-Plan-Implement - Dexter Horthy](https://www.youtube.com/watch?v=YwZR6tc7qYg) |
| Published | 2026-03-25 |
| Ingested upstream | 2026-03-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

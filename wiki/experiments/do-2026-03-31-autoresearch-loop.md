# Implement autoresearch loop for YOLO project optimization

> Back to [[experiments-index]]

Source: **[The only AutoResearch tutorial you will ever need](https://www.youtube.com/watch?v=uBWuKh1nZ2Y)** · do · 2026-03-31

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we structure the YOLO build loop as a Karpathy-style autoresearch loop (single file to edit, single metric to optimize, automated eval, git commit on success / reset on failure), then project quality improves autonomously because the agent iterates hundreds of times without human intervention.

## What they did

Karpathy's AutoResearch uses a 3-file architecture: program.md (goals/constraints), train.py (editable file), prepare.py (read-only metric). The loop: hypothesize → modify → train → evaluate → keep/discard → repeat. Applied to ML training, website optimization (50ms→25ms load time), trading strategies, prompt engineering.

## Actionable steps

- Identify a YOLO project with a measurable metric (e.g., load time, Lighthouse score, code size)
- Structure it as: program.md (rules), index.html (editable), test_project.py (metric)
- Let the agent loop: modify → test → keep if better, reset if worse
- Track how many iterations it takes to plateau

## Success metric

Agent autonomously improves a measurable metric over 10+ iterations without human guidance.

## Relevance to YOLO loop

The YOLO loop already has program.md and test_project.py. Adding a metric-driven feedback loop would be a natural evolution — especially for the refinement phase.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

color-mix built with autoresearch loop: metric=Gemini bug count, target=0. Iteration 1: 4 bugs found. Iteration 2: 0 bugs (all fixed). Loop converged in 2 iterations, 216 seconds total. Combined with vertical planning outline, the full loop (outline→build→eval→fix→re-eval) produced a clean build faster than ad-hoc approach.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-02 | `done` | Autoresearch loop converged in 2 iterations. 4 bugs→0. Adopted as standard loop. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-03-31-autoresearch-loop` |
| Channel | do |
| Video | [The only AutoResearch tutorial you will ever need](https://www.youtube.com/watch?v=uBWuKh1nZ2Y) |
| Published | 2026-03-31 |
| Ingested upstream | 2026-03-31 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

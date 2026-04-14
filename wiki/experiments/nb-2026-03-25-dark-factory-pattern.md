# Adopt the Dark Factory pattern for autonomous builds

> Back to [[experiments-index]]

Source: **[Tobi Lutke Made a 20-Year-Old Codebase 53% Faster Overnight](https://www.youtube.com/watch?v=YpPcDHc3e9U)** · @NateBJones · 2026-03-25

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we restructure the YOLO build loop as a Dark Factory (spec in → autonomous processing → eval out with retry loops), then build quality increases because the agent iterates against automated tests until passing, removing the human bottleneck from the middle.

## What they did

Nate described 'Dark Factories' as fully autonomous build pipelines: specification goes in, agent builds and tests iteratively, evaluation comes out. If tests fail, the agent loops back and tries again.

## Actionable steps

- Define clear spec format for each build (what working looks like, acceptance criteria)
- Wire test_project.py as the automated eval gate
- Let the agent loop: build → test → fix → retest until all pass
- Measure how many iterations it takes vs current single-pass approach

## Success metric

Agent autonomously fixes its own test failures in at least 3 out of 5 builds.

## Relevance to YOLO loop

The YOLO loop already has spec → build → test → fix. Formalizing it as a Dark Factory with explicit retry loops would reduce human intervention.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

Added Dark Factory Retry Loop section to program.md: test→fix→retest cycle with max 3 retries, mandatory retest after Gemini audit fixes, explicit gate requiring both test suite AND audit to pass before shipping. The YOLO loop already practiced this informally; now it is codified as protocol.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-03-29 | `in_progress` | Updating program.md with explicit retry loop pattern |
| 2026-03-29 | `done` | Formalized retry loop in program.md Testing Protocol |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-03-25-dark-factory-pattern` |
| Channel | @NateBJones |
| Video | [Tobi Lutke Made a 20-Year-Old Codebase 53% Faster Overnight](https://www.youtube.com/watch?v=YpPcDHc3e9U) |
| Published | 2026-03-25 |
| Ingested upstream | 2026-03-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

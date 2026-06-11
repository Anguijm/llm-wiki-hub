# Build an Agent Readiness checklist for the YOLO codebase

> Back to [[experiments-index]]

Source: **[Nvidia Just Open-Sourced What OpenAI Wants You to Pay Consultants For](https://www.youtube.com/watch?v=7AO4w4Y_L24)** · nb · 2026-03-24

**Status:** `done` · **Verdict:** `discard` · **Effort:** `high`

---

## Hypothesis

If we evaluate the YOLO codebase against an 'Agent Readiness Framework' (code quality, documentation, test coverage, clear file structure), then agent productivity improves because failures are usually caused by broken environments, not broken agents.

## What they did

Factory.ai evaluates codebases against 8 technical pillars before letting agents work on them. Their finding: when agents fail, it's usually the environment (codebase/data) that's broken, not the agent. Fixing the environment yields compounding gains.

## Actionable steps

- Define 5-8 readiness pillars for YOLO projects (README quality, test coverage, clear entry point, consistent structure)
- Score all 112 survivors against the checklist
- Fix the lowest-scoring projects first
- Track whether agent refinement success rate correlates with readiness score

## Success metric

Projects scoring 7+/8 on readiness have measurably fewer Gemini-reported bugs during refinement.

## Relevance to YOLO loop

The YOLO loop has 112 projects of varying quality. A readiness framework would prioritize which to refine and predict where agents will struggle.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

Phase 2 systematically evaluated every project via Gemini code review (the readiness check) and Phase 3 evaluated usefulness (the value check). The 70 survivors are the projects that passed both checks. Building a separate checklist would duplicate what was already done. The test_project.py + Gemini review pipeline IS the readiness framework.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-03-29 | `done` | Phase 2 refinement + Phase 3 cull already accomplished this goal |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-03-24-agent-readiness-checklist` |
| Channel | nb |
| Video | [Nvidia Just Open-Sourced What OpenAI Wants You to Pay Consultants For](https://www.youtube.com/watch?v=7AO4w4Y_L24) |
| Published | 2026-03-24 |
| Ingested upstream | 2026-03-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

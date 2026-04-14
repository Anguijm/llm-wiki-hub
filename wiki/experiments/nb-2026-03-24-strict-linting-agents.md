# Apply strict linting to all agent-generated code

> Back to [[experiments-index]]

Source: **[Nvidia Just Open-Sourced What OpenAI Wants You to Pay Consultants For](https://www.youtube.com/watch?v=7AO4w4Y_L24)** · @NateBJones · 2026-03-24

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we add automated static analysis (ESLint, HTMLHint) to the test pipeline, then bug rates drop because agents are 'lazy developers' who take shortcuts unless forced to comply with standards.

## What they did

Nate cited Factory.ai's finding that strict automated linting is required to force agents to adhere to clean code standards. Agents produce working-but-sloppy code without enforcement.

## Actionable steps

- Add ESLint with strict rules to test_project.py pipeline
- Run against all 112 survivors to establish baseline violation count
- Fix top violation categories
- Require zero lint errors before marking a project refined

## Success metric

All new and refined projects pass strict lint with zero errors.

## Relevance to YOLO loop

Current test_project.py checks syntax and ID consistency but not code quality. Linting would catch style issues, unused vars, and potential bugs the current tests miss.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

Created .eslintrc.json with 14 rules. Baseline scan: 68/70 survivors pass clean (0 errors, 0 warnings). Phase 2 Gemini reviews already caught most lint-level issues. Config committed for future use in test pipeline.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-03-29 | `in_progress` | Evaluating ESLint integration into test pipeline |
| 2026-03-29 | `done` | Baseline scan shows 68/70 clean. ESLint config created. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-03-24-strict-linting-agents` |
| Channel | @NateBJones |
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

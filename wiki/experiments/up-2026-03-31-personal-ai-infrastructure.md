# Build a Council skill for multi-perspective task review

> Back to [[experiments-index]]

Source: **[Anatomy of an Agentic Personal AI Infrastructure](https://www.youtube.com/watch?v=l9CPmPk2R-M)** · up · 2026-03-31

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we spin up multiple specialized agents to debate a task from different perspectives (security, performance, UX, architecture) before committing code, then build quality improves because blind spots from any single perspective are caught before shipping.

## What they did

Daniel Miessler's PAI system includes a Council feature that spins up a group of specialized agents to debate a task from multiple perspectives before providing a final recommendation. Also includes IterativeDepth (same question from multiple angles) and TheAlgorithm (reverse-engineer ambiguous goals into testable criteria).

## Actionable steps

- For the next 3 YOLO builds, after Gemini code review, add a second review pass from a different angle (security, then performance, then UX)
- Compare bug rates with single-review vs multi-perspective review
- If effective, formalize as a Council skill in the build loop

## Success metric

Multi-perspective review catches bugs that single Gemini review missed in at least 2 of 3 test builds.

## Relevance to YOLO loop

Currently the YOLO loop uses one Gemini review pass focused on bugs. Adding perspective-specific passes (security, perf, UX) could catch more issues.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

3/3 builds complete: ssl-check (2 angles, pilot), shader-forge (6 angles, manual), penrose+ (6 angles, automated via cron). Multi-perspective review consistently catches bugs single review misses. Guide review caught missing onboarding on shader-forge (4/10). Security review caught XSS on ssl-check. Expanded from 2 to 6 angles mid-experiment. Now adopted as standard for all builds including cron.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-02 | `in_progress` | Pilot: next Tick build gets standard bug review + second pass (security/perf/UX rotating) |
| 2026-04-02 | `in_progress` | shader-forge: 2/3 builds done. Expanded to 6 review angles (bugs, security, UI, guide, usefulness, cool). Guide review (4/10) caught missing onboarding. All angles surfaced unique findings. |
| 2026-04-03 | `done` | 3/3 builds done. Council adopted as standard. Cron prompt updated with all 6 angles. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `up-2026-03-31-personal-ai-infrastructure` |
| Channel | up |
| Video | [Anatomy of an Agentic Personal AI Infrastructure](https://www.youtube.com/watch?v=l9CPmPk2R-M) |
| Published | 2026-03-31 |
| Ingested upstream | 2026-03-31 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

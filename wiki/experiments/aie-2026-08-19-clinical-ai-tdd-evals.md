# Write Hundreds of Evals TDD-Style Before Prompting, with Zero Tolerance for Safety-Critical Failures

> Back to [[experiments-index]]

Source: **[AI is the World's largest Relationship Therapist — Clay Cockrell & Tony Fabrikant, CoupleWork AI](https://www.youtube.com/watch?v=yoONZwV2smc)** · aie · 2026-08-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we write eval cases in a test-driven style before finalizing prompts — running the agent through them tens of thousands of times and treating any single safety-critical failure as a blocker — then the eval suite becomes our primary development tool and prevents dangerous outputs from reaching users, because defining 'good' formally upfront makes the optimization target concrete and exposes edge cases early.

## What they did

CoupleWork co-founder Tony Fabrikant described their development process: start with the clinician (Clay Cockrell) to encode what good responses look like, then write hundreds of evals TDD-style. Run the agent through them thousands to tens of thousands of times. Watch for outliers — when safety is on the line, even one failing test is not acceptable. Complement automated evals with the developer's own subjective gut-check by using the product personally in real relationship contexts. Supplement with background safety screening on every message for escalating-control patterns, fear-based language, and risk indicators, with hard-coded protocol responses when those trigger.

## Relevance to YOLO loop

The TDD-for-evals framing is directly applicable to our agent development loop. Writing eval cases before writing prompts forces us to specify desired behavior formally, and zero-tolerance thresholds for safety-critical cases maps to any domain where certain failures are unacceptable.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-19-clinical-ai-tdd-evals` |
| Channel | aie |
| Video | [AI is the World's largest Relationship Therapist — Clay Cockrell & Tony Fabrikant, CoupleWork AI](https://www.youtube.com/watch?v=yoONZwV2smc) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

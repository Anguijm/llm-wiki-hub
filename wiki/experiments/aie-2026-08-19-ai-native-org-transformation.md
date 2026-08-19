# Run Per-Test-Case Multiple Trials with Minimum Pass Rate for Non-Deterministic AI Features

> Back to [[experiments-index]]

Source: **[How to build an AI-Native Health Company — Dan Feng, Maven Clinic](https://www.youtube.com/watch?v=WJRdLNhrsLQ)** · aie · 2026-08-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run each integration test case many times and require a sustained minimum pass rate (e.g. 90%) rather than a single pass, then we get statistically meaningful confidence in non-deterministic LLM behavior before release, because a single passing run does not bound the variance of a probabilistic model.

## What they did

Maven Clinic built hundreds of integration tests covering all known use cases for their AI features. For each test case they run it multiple times and require a consistently high pass rate (e.g. 90%) rather than accepting a single pass. After launch they run an auto-eval system that scores every conversation against predefined rubrics, and a dedicated human review team spot-checks conversations continuously — scaling up to 20% review on new feature launches. For safety-critical flows like reimbursement claims they run the same receipt through multiple models and only proceed if results agree.

## Relevance to YOLO loop

Directly applicable to our CI/eval loop. Switching from single-run pass/fail to repeated-trial pass-rate thresholds would surface flaky LLM behavior that currently slips through and reduce false confidence in agent reliability.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-19-ai-native-org-transformation` |
| Channel | aie |
| Video | [How to build an AI-Native Health Company — Dan Feng, Maven Clinic](https://www.youtube.com/watch?v=WJRdLNhrsLQ) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

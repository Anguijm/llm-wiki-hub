# Make Agent Evals Stochastic and Hierarchically Sampled to Prevent Replay-Agent Gaming

> Back to [[experiments-index]]

Source: **[Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](https://www.youtube.com/watch?v=CTLa_p6iOiY)** · aie · 2026-08-14

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we randomize initial state, data profiles, and appearance across eval runs instead of using a fixed benchmark, then agent scores will reflect genuine generalization rather than deterministic replay because a replay agent that memorizes the static task sequence can no longer trivially match frontier model performance.

## What they did

The researcher showed that a 'replay agent' — a sub-megabyte script that blindly re-executes recorded successful action sequences — matches or beats frontier models on standard static computer-use benchmarks (OSWorld, MobileWorld). The root cause is benchmark determinism. Their solution was the PRISM design principles for eval environments: multifactorial variation (randomize data, appearance, initial state), verified valid configurations, sandboxed execution, privileged verifiers, and realistic reproduction. They built DGWorld (15 Android apps, 387 scenarios, 3.2M verified configurations). They also showed that standard confidence intervals are overconfident due to ignoring benchmark hierarchy structure, and that correcting for this (using hierarchical sampling) changes model-selection decisions — a 4% real performance mismatch with $20/mistake at 1M tasks costs hundreds of thousands of dollars per month if you use the wrong model based on overconfident evals.

## Relevance to YOLO loop

If the YOLO loop uses any fixed eval suite to decide whether an agent change is an improvement, that suite is likely gameable by the same replay-agent phenomenon. Adding parameter randomization (vary the input data, file names, repo state) to eval runs and reporting hierarchically-corrected confidence intervals would make improvement signals more trustworthy.

## Notes

Practical minimum viable version: before running a regression eval, shuffle at least one input variable (file content, task parameters) so the same script cannot trivially replay. Full PRISM compliance is a multi-week effort. Paper available — check Programma Labs / Meta Superintelligence Labs publications.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-14-cu-benchmark-stochastic-envs` |
| Channel | aie |
| Video | [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](https://www.youtube.com/watch?v=CTLa_p6iOiY) |
| Published | 2026-08-14 |
| Ingested upstream | 2026-08-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

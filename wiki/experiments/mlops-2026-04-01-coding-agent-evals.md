# Build a golden dataset of past bugs as an eval suite

> Back to [[experiments-index]]

Source: **[Stop Shipping on Vibes — How to Build Real Evals for Coding Agents](https://www.youtube.com/watch?v=VbX24V_JFQI)** · mlops · 2026-03-31

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we extract 20-30 past Gemini-caught bugs from learnings.md as test cases (input: buggy code, expected: the fix), then we can measure whether future agent builds avoid those same bug patterns — turning learnings into a regression test.

## What they did

Conference talk on building evals for coding agents. Key insight: mine your own past bugs as a proprietary eval suite. Also: execution-based evals (run the code, not string comparison), trajectory evaluation (track tool calls), and tiered eval systems (unit → tool → end-to-end).

## Actionable steps

- Parse learnings.md for all FIX entries with clear before/after patterns
- Create a test file with 20 representative bug patterns
- Before each new build, run the agent output against the bug pattern checker
- Track: does the agent avoid known antipatterns?

## Success metric

New builds trigger zero matches against the known-bug pattern suite.

## Relevance to YOLO loop

learnings.md has 350+ bug fixes documented. Mining them into an automated regression check would compound the value of all that accumulated knowledge.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

Built eval_bugs.json (26 patterns) + eval_bugs.py runner. Mined from 2700+ lines of learnings.md. Patterns cover: URL double-slash, clipboard fallback, hot path perf, GPU leaks, grammar, emoji, prototype pollution, etc. Runner supports --all and --json. Integrated into cron prompt (step C). 2048 matches across full portfolio — some false positives but catches real bugs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `done` | 26 patterns extracted, runner built, integrated into cron |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-04-01-coding-agent-evals` |
| Channel | mlops |
| Video | [Stop Shipping on Vibes — How to Build Real Evals for Coding Agents](https://www.youtube.com/watch?v=VbX24V_JFQI) |
| Published | 2026-03-31 |
| Ingested upstream | 2026-04-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

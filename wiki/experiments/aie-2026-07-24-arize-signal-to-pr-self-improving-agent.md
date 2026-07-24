# Build a trace-driven agent that auto-generates a PR with evidence before human review

> Back to [[experiments-index]]

Source: **[From Signal to PR: Anatomy of a Self-Improving Agent — Jason Lopatecki, Arize](https://www.youtube.com/watch?v=9HbzAWnKbo4)** · aie · 2026-07-24

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we give a coding agent access to production traces and observability skills, then it can pre-stage a fix PR with supporting evidence before a human even looks at the alert, reducing mean time to resolution because the bottleneck is no longer finding the fix but deciding whether the pre-staged fix is correct.

## What they did

Described Arize's 'Signal' system: an agent that periodically reads production traces and online eval scores, identifies anomaly patterns, gathers context via well-designed observability skills (trace cohort queries, Pyroscope memory profiling, faceted customer segmentation), and then opens a GitHub PR with the proposed fix plus all supporting evidence. Human review shifts from 'find the problem and fix it' to 'review the pre-staged fix and approve/reject.' Emphasized that skills must be carefully designed to retrieve the right data into file format (not raw API responses) because coding agent harnesses work best with files. Noted that online evals layered onto traces serve as pre-processed signals that the agent can query in aggregate, enabling it to distinguish between one-off failures and systemic patterns.

## Relevance to YOLO loop

The YOLO loop currently requires a human to notice a skill failure, diagnose it, and write the fix. Connecting Claude Code to our own trace/log output with a Signal-style skill that auto-drafts a fix PR would close this gap. Even a partial implementation (agent surfaces diagnosis + suggested fix without auto-PR) would reduce triage time significantly.

## Notes

Speaker's key insight: the bottleneck is not the fix anymore, it's confidence in the fix. Pre-staged PR with evidence shifts the human role from investigator to approver. File-based skill design principle (get trace data into a file, not streamed JSON) is immediately applicable to any observability skill we build.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-24-arize-signal-to-pr-self-improving-agent` |
| Channel | aie |
| Video | [From Signal to PR: Anatomy of a Self-Improving Agent — Jason Lopatecki, Arize](https://www.youtube.com/watch?v=9HbzAWnKbo4) |
| Published | 2026-07-24 |
| Ingested upstream | 2026-07-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

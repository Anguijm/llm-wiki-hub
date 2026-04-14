# Benchmark multiple coding agents on the same YOLO build spec

> Back to [[experiments-index]]

Source: **[The Coding Agent Multiverse of Madness]()** · @MLOps · 2026-04-02

**Status:** `deferred` · **Verdict:** `deferred` · **Effort:** `high`

---

## Hypothesis

If we run the same build specification through multiple coding agents (Claude Code, Codex, Gemini CLI, Cursor, etc.) and compare outputs, then we identify which agent is best suited for which project type because we have empirical data rather than vibes.

## What they did

MLOps explored the proliferation of coding agents — the 'multiverse' of competing approaches (Claude Code, Codex, Cursor, Devin, etc.) and how they differ in architecture and capability.

## Actionable steps

- Select 3 representative YOLO build specs (simple UI, API-heavy, data pipeline)
- Run each through Claude Code and at least one alternative agent
- Score outputs on: test pass rate, code quality, build time, cost
- Document which agent excels at which project type

## Success metric

Completed comparison matrix for at least 2 agents across 3 project types.

## Relevance to YOLO loop

The YOLO loop uses Claude Code exclusively. Knowing if alternatives are better for specific project types would let us route builds to the optimal agent.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Notes

Deferred 2026-04-07: cross-agent benchmark is high cost (API keys for Codex, Gemini, Cursor, multi-day runs). Consider scoped-down version "Claude Code vs Gemini CLI on one spec" as a 1-day test if cost-benefit becomes a question.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `backlog` | Ingested from Phase 4 YouTube pipeline — title-only inference |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-04-03-coding-agent-multiverse` |
| Channel | @MLOps |
| Published | 2026-04-02 |
| Ingested upstream | 2026-04-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Benchmark coding agents against legacy multi-repo vs clean monorepo to quantify refactor ROI

> Back to [[experiments-index]]

Source: **[Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](https://www.youtube.com/watch?v=7vn4WpqNpck)** · aie · 2026-08-08

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we systematically measure agent task completion time, code quality, and developer satisfaction before and after consolidating a fragmented multi-repo legacy codebase into a clean monorepo, then we will find measurably faster agent-assisted feature delivery and lower per-task cost post-refactor because agents navigate file hierarchies and run end-to-end tests far more effectively in a unified repo with consistent patterns.

## What they did

Denys Linkov's team at Wisedocs ran a 6-month refactor of 10+ legacy repos into a monorepo, tracking five major task categories before and after. They measured orchestrator evaluation time (from months to days with agentic deep-research workflows), per-file refactor time (o3 completed a 10-major-change refactor in 3 hours of cursor back-and-forth), pipeline execution time, cost, and max file size supported. Post-refactor, features that took months shipped in under a week, and other teams voluntarily adopted the new patterns.

## Relevance to YOLO loop

Directly relevant to how we structure our codebase for agent work: the data suggests that investing in a clean monorepo pays compounding dividends as agents are used more heavily, and that the refactor itself can be substantially AI-assisted.

## Notes

Key anti-pattern flagged: 'AI psychosis'—accepting a 20-page deep research report at face value without verifying features actually exist in the evaluated library. Human verification checkpoints remain essential even in highly automated evaluation pipelines.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-08-legacy-refactor-benchmark` |
| Channel | aie |
| Video | [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](https://www.youtube.com/watch?v=7vn4WpqNpck) |
| Published | 2026-08-08 |
| Ingested upstream | 2026-08-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

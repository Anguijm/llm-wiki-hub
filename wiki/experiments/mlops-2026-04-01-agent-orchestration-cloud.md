# Run parallel agent sessions for independent YOLO tasks

> Back to [[experiments-index]]

Source: **[2026 The Year of Agent Orchestration](https://www.youtube.com/watch?v=eT1F2BAZJ64)** · mlops · 2026-03-31

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we run multiple agent sessions in parallel (e.g., 3 Tick builds simultaneously using subagents), then throughput increases because independent builds do not need sequential execution — each gets its own context and tools.

## What they did

Zach Lloyd (Warp/Oz) argued local agents hit capacity limits. Cloud orchestration enables multiple parallel agents, persistent background execution, and team visibility. Demo showed launching multiple agent sessions simultaneously to implement independent features.

## Actionable steps

- Identify 3 independent YOLO builds that have no dependencies
- Launch them as parallel subagents in a single session
- Compare: does parallel execution produce same quality as sequential?
- Measure: total wall-clock time for 3 builds parallel vs 3 sequential

## Success metric

3 builds complete in under 2x the wall-clock time of 1 build, with same quality.

## Relevance to YOLO loop

We already use subagents for Tick builds. Formalizing parallel execution for independent builds would increase throughput significantly.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

3 projects built in parallel (git-resolve, cron-viz, dns-lookup) in 151 seconds wall clock. All pass tests. Sequential estimate was 5-6 min. ~2x throughput gain. Worktree isolation prevented file conflicts.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-02 | `done` | Successfully ran 3 parallel agent builds via worktree isolation. 2x throughput. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-04-01-agent-orchestration-cloud` |
| Channel | mlops |
| Video | [2026 The Year of Agent Orchestration](https://www.youtube.com/watch?v=eT1F2BAZJ64) |
| Published | 2026-03-31 |
| Ingested upstream | 2026-04-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

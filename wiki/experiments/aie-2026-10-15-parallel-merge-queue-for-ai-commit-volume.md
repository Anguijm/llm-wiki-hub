# Replace serialized CI merge queues with speculative parallel combination testing for agent-generated PRs

> Back to [[experiments-index]]

Source: **[Rebuilding CI for AI-Scale Commit Volume — Gautam Korlam, SonarSource](https://www.youtube.com/watch?v=7b9tov5Uc5s)** · aie · 2026-10-15

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we test likely combinations of incoming agent-generated PRs in parallel (rather than serializing them through a single merge queue), then trunk stability will be maintained at 10x commit volume because conflicts between PRs that individually pass CI are caught before merge, preventing red-trunk states that block all downstream agents.

## What they did

Gautam described a 10x increase in commit rate with the same team size, driven by coding agents. He showed that existing CI and review queues built for human-speed commits become bottlenecks: PRs pile up, queues stall, and agents don't wait their turn. He referenced the Summit Queue system built at Uber that tested all likely commit combinations in parallel, predicted which PRs would conflict, removed failing PRs from the queue with author notification, and only allowed PRs that passed combined testing to land on trunk. He also emphasized recording agent trajectory data (which agent, which session, who prompted it, why a failing test was accepted) as a compliance artifact before CI logs expire.

## Relevance to YOLO loop

Directly relevant to our software factory design: as we scale agent-generated PR volume, our current serialized CI will become the bottleneck. Speculative parallel combination testing is the architectural pattern needed to keep trunk green at agent scale.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-15-parallel-merge-queue-for-ai-commit-volume` |
| Channel | aie |
| Video | [Rebuilding CI for AI-Scale Commit Volume — Gautam Korlam, SonarSource](https://www.youtube.com/watch?v=7b9tov5Uc5s) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

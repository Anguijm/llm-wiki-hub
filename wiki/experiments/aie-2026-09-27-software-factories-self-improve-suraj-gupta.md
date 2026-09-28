# Add a self-improvement feedback loop that lets the agent pipeline update its own prompts and tools based on failure patterns

> Back to [[experiments-index]]

Source: **[How Software Factories Improve Themselves — Suraj Gupta, Warp](https://www.youtube.com/watch?v=TN3mj92oZ8I)** · aie · 2026-09-27

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we instrument our agent pipeline to log failure modes and periodically run a meta-agent that proposes prompt or tool improvements based on those logs, then the pipeline improves over time without manual tuning because systematic failure analysis surfaces fixable patterns that humans miss.

## What they did

Suraj Gupta from Warp described how their software factory architecture includes mechanisms for the system to analyze its own failures and successes and feed that back into pipeline improvements—effectively a self-improving loop at the infrastructure level.

## Relevance to YOLO loop

High strategic relevance: this describes the next evolution of the YOLO loop—a loop that not only runs but improves itself. Even a lightweight version (logging failures and weekly prompt review) would compound gains over time.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-27-software-factories-self-improve-suraj-gupta` |
| Channel | aie |
| Video | [How Software Factories Improve Themselves — Suraj Gupta, Warp](https://www.youtube.com/watch?v=TN3mj92oZ8I) |
| Published | 2026-09-27 |
| Ingested upstream | 2026-09-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

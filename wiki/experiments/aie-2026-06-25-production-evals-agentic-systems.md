# Replace benchmark-only evals with a continuous production telemetry eval loop for agentic workflows

> Back to [[experiments-index]]

Source: **[Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs](https://www.youtube.com/watch?v=vljxQZfJ9wY)** · aie · 2026-06-25

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we instrument our agentic systems with scenario-based evals and continuous production telemetry (execution traces, tool success rates, escalation rates, recovery rates, latency, cost) rather than relying on offline benchmark scores, then we will detect reliability drift before users do because production behavior diverges from benchmark performance as tool failures, context drift, and multi-agent coordination failures are invisible to prompt-level benchmarks.

## What they did

Nishant described the evaluation pyramid (benchmarks at the base, scenario-based evals in the middle, production telemetry at the top as the highest-value signal). He outlined a continuous eval loop where every production interaction becomes evaluation data, humans review edge cases, feedback improves datasets, and offline scenarios validate updates. He proposed a control plane / execution plane separation where the control plane continuously observes telemetry, runs simulations, and coordinates human review. Key metrics he mapped to business outcomes: task completion, tool success, escalation rate, safety violations, latency, cost, recovery rate — notably excluding raw accuracy.

## Relevance to YOLO loop

Directly applicable: we should instrument our Claude Code agent runs with structured traces capturing tool call success/failure, task completion, and cost per session, then treat that telemetry as our primary eval signal rather than occasional manual review.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-25 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-25-production-evals-agentic-systems` |
| Channel | aie |
| Video | [Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs](https://www.youtube.com/watch?v=vljxQZfJ9wY) |
| Published | 2026-06-25 |
| Ingested upstream | 2026-06-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

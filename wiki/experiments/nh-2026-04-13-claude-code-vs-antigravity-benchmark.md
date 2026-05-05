# Run a structured 100-task head-to-head between Claude Code and a challenger tool

> Back to [[experiments-index]]

Source: **[100 Hours Testing Claude Code vs Antigravity (honest results)](https://www.youtube.com/watch?v=99VHENEKA9o)** · NateHerk · 2026-04-13

**Status:** `deferred` · **Effort:** `high`

---

## Hypothesis

If we benchmark Claude Code against an alternative agentic coding tool (e.g. Antigravity) across a fixed set of real tasks drawn from our own backlog, then we will get actionable signal on which tool to default to in the YOLO loop because controlled comparison over real workload is more predictive than synthetic benchmarks.

## What they did

Speaker spent 100 hours running Claude Code and Antigravity against comparable coding tasks, documenting where each tool succeeded, failed, stalled, or required heavy human intervention. Reported honest results including cases where Claude Code underperformed expectations.

## Relevance to YOLO loop

Directly relevant to tool selection at the core of the YOLO loop. Nate's methodology — same tasks, honest failure logging, time-boxed — is a replicable evaluation framework we could apply whenever a new agentic coding tool emerges. The specific Claude Code findings also inform how much autonomous trust to extend in our current loop.

## Notes

100-task head-to-head too big for a tick. eval-opus-47-backbone (already queued) partially covers the model-comparison angle — defer until that ships and we see the methodology work.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-13 | `backlog` | Extracted from YouTube RSS |
| 2026-04-22 | `deferred` | 100-task head-to-head too big for a tick. eval-opus-47-backbone (already queued) partially covers the model-comparison angle — defer until that ships and we see the methodology work. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-04-13-claude-code-vs-antigravity-benchmark` |
| Channel | NateHerk |
| Video | [100 Hours Testing Claude Code vs Antigravity (honest results)](https://www.youtube.com/watch?v=99VHENEKA9o) |
| Published | 2026-04-13 |
| Ingested upstream | 2026-04-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

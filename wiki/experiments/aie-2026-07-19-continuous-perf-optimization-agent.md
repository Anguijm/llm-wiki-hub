# Build a weekly autonomous agent workflow that surfaces scored high-ROI performance optimization PRs from production traces

> Back to [[experiments-index]]

Source: **[From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization - May Walter, Hud](https://www.youtube.com/watch?v=JJGbw4ggaFs)** · aie · 2026-07-19

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we run a scheduled agentic workflow weekly that ingests production traces with function-level context, scores optimization opportunities by ROI (impact × ease), and outputs human-readable PR summaries with runtime-verified fixes, then engineering teams will proactively address performance regressions that would otherwise never be investigated, because the research phase (historically an unbounded time sink) is automated and the output arrives pre-scored and pre-verified.

## What they did

Speaker (CTO of Thundra) built a GitHub-based agentic workflow that runs on a weekly schedule (or on SLO-breach webhook triggers). It pulls production traces with function-level forensic context, uses a scoring system to identify high-ROI performance opportunities (easy + impactful), generates a PR with the fix, runs runtime verification of the fix before surfacing it to a human reviewer, and presents results as small human-readable gists. Key design decisions: vendor-neutral infrastructure (model, compute, and harness all swappable), secure tool-call permissions, easy-to-maintain workflow logic with feedback loops. The scoring and guardrails were identified as the critical reliability mechanism — without them the agent generates low-trust 'slop'. Speaker emphasized this automates a phase (proactive investigation) that engineers never actually did in their normal workflow, not just accelerating existing work.

## Relevance to YOLO loop

High relevance: the YOLO loop can adopt the same pattern — scheduled autonomous runs with production context ingestion, scored output, and runtime verification gates before human review. The 80-90% trust threshold before autonomous operation is a useful calibration target for any agentic automation in the loop.

## Notes

Four key takeaways from speaker: (1) define what matters via scoring/guardrails first; (2) automate phases that never happened, not just existing tasks; (3) context over cleverness — right context beats clever prompting; (4) agentic engineering automation requires 80-90% trust threshold, qualitatively different from IDE-assisted coding. References 2026 Google DORA metrics: AI increases individual effectiveness but also software delivery instability.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-19-continuous-perf-optimization-agent` |
| Channel | aie |
| Video | [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization - May Walter, Hud](https://www.youtube.com/watch?v=JJGbw4ggaFs) |
| Published | 2026-07-19 |
| Ingested upstream | 2026-07-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

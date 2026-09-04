# Benchmark Fable 5.1 vs Fable 5 as orchestrators in a multi-agent app-build workflow on identical prompts

> Back to [[experiments-index]]

Source: **[I Had Fable 5.1 and 5 Build Me the Same App](https://www.youtube.com/watch?v=5FukkI4fbiU)** · nh · 2026-09-04

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we run Fable 5.1 and Fable 5 as top-level orchestrators over the same multi-agent delegation prompt for a complex app build, then Fable 5 will be more cost-efficient (lower total spend for comparable quality) because it delegates more heavily to Sonnet workers (~80% Sonnet) while Fable 5.1 over-invests in Opus workers (~57% Opus), inflating cost without proportional quality gain.

## What they did

Speaker gave both models an identical big-goal prompt to build 'OpsFlow' (a local-first visual incident-response workflow simulator) using a multi-agent delegation architecture where the top-level model owned strategy/planning and delegated engineering to Opus and Sonnet sub-agents. Fable 5.1 ran for ~36 hours, used 404k of context window (40%), cost ~$1,200, and allocated 57% Opus / 40% Sonnet / 3% itself. Fable 5 ran for ~12 hours, used 260k context (26%), cost ~$500, and allocated 80% Sonnet / 12% Opus / 7% itself. Speaker evaluated both UIs hands-on and concluded the apps were comparable in quality, making Fable 5 the winner on cost-efficiency for this task.

## Relevance to YOLO loop

Core YOLO loop experiment: tests which model to use as orchestrator in a long-running agentic coding workflow, and reveals how worker-model allocation (Opus vs Sonnet ratio) drives cost and runtime — critical for calibrating multi-agent pipeline economics.

## Notes

Fable 5.1 cost ~$1,200 vs Fable 5 ~$500 for similar output quality. Fable 5.1 UI had cleaner aesthetics; Fable 5 UI had AI-generated card styling. Speaker notes Fable 5.1 feels better for general knowledge work day-to-day but Fable 5 wins this specific agentic coding scenario on value. Input token count for Fable 5 (256 tokens reported) seemed anomalous to speaker.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-04-fable51-vs-fable5-agentic-app-build` |
| Channel | nh |
| Video | [I Had Fable 5.1 and 5 Build Me the Same App](https://www.youtube.com/watch?v=5FukkI4fbiU) |
| Published | 2026-09-04 |
| Ingested upstream | 2026-09-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

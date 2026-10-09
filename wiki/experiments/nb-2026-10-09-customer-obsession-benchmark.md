# Replace leaderboard evals with a tracked personal use-case log as primary quality signal

> Back to [[experiments-index]]

Source: **[Google's Gemini Argon Is #1 On A Leaderboard. It Hasn't Passed The Benchmark That Matters.](https://www.youtube.com/watch?v=sVQ3XlM9I40)** · nb · 2026-10-09

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we maintain a running log of real agent use cases attempted (with pass/fail notes) instead of relying on public benchmark scores to select models, then we will pick better models for our specific workflows because benchmark rank does not correlate with utility on heterogeneous personal or enterprise tasks.

## What they did

Speaker dismissed AI leaderboards as irrelevant to actual utility and instead described compiling a personal list of 26 agent use cases tried in the past 3 months (tax prep, travel planning, school schedules, medical history, subscription management) and using that lived experience to evaluate models. He demonstrated multi-model orchestration: using ChatGPT Dots for data aggregation across financial accounts, then handing off to Meta Muse for fast web-action execution. He argued the bottleneck has shifted from model capability to product experience and customer obsession, and that Claude 5.5 will matter not because of leaderboard rank but because Anthropic is enterprise-customer-obsessed.

## Relevance to YOLO loop

Informs how we score model selection in the YOLO loop: maintain a living use-case registry with per-model pass rates rather than defaulting to whatever tops LMSYS.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-10-09-customer-obsession-benchmark` |
| Channel | nb |
| Video | [Google's Gemini Argon Is #1 On A Leaderboard. It Hasn't Passed The Benchmark That Matters.](https://www.youtube.com/watch?v=sVQ3XlM9I40) |
| Published | 2026-10-09 |
| Ingested upstream | 2026-10-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

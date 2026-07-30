# Apply an open-ended evolutionary search agent to narrow optimization benchmarks before broader research tasks

> Back to [[experiments-index]]

Source: **[First Steps Toward Automated AI Research — Richard Socher, CEO Recursive AI](https://www.youtube.com/watch?v=pWXUkLP9uWM)** · aie · 2026-07-30

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we deploy an autonomous research agent on a tightly scoped, measurable benchmark (e.g. bits-per-byte on a small model, training speed, CUDA kernel efficiency) with an automated reward signal and no human-in-the-loop ideation, then the agent will discover genuinely novel solutions beyond hyperparameter tuning within days, because the closed evaluation loop enables rapid iterative search across a well-defined fitness landscape.

## What they did

Richard Socher described Recursive AI's system (RSI) that applies evolutionary/open-ended search to automate AI research. They ran it against three concrete benchmarks: (1) NanoChat — trained a small chat model to minimize bits-per-byte; the community had reached 0.93, the system reached 0.91 in ~1-2 days and discovered novel ideas like hash bigram/trigram embedding tables mixed into attention value paths via learned gates. (2) NanoGPT speedrun — beat a year of human+AI collaboration to make training 2+ seconds faster at 70 seconds total. (3) CUDA kernels — outperformed Nvidia leaderboard best results across all kernel categories. All results were verified with Nvidia to rule out reward hacking.

## Relevance to YOLO loop

Suggests our dev loop could include an autonomous optimization agent targeting specific, measurable sub-problems (e.g. prompt compression ratio, tool call latency, test pass rate) rather than only human-directed tasks. Start small: pick one metric with a fast eval loop and let an agent propose and test changes autonomously overnight.

## Notes

Key precondition from the talk: the benchmark must have a fast, unambiguous, automated reward signal. The system fails to generate interesting results on tasks where evaluation requires human judgment or is slow. Start with the narrowest possible well-defined metric.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-30 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-30-automated-ai-research-open-ended-evolution` |
| Channel | aie |
| Video | [First Steps Toward Automated AI Research — Richard Socher, CEO Recursive AI](https://www.youtube.com/watch?v=pWXUkLP9uWM) |
| Published | 2026-07-30 |
| Ingested upstream | 2026-07-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

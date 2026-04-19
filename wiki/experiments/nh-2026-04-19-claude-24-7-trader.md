# Build a Long-Running Claude Agent With Persistent Decision Loop

> Back to [[experiments-index]]

Source: **[I Turned Claude Opus 4.7 Into a 24/7 Trader](https://www.youtube.com/watch?v=6MC1XqZSltw)** · NateHerk · 2026-04-19

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we wrap Claude Opus 4.7 in a persistent polling loop that reads live data, makes decisions, and executes actions autonomously, then the agent can operate 24/7 without human intervention because the loop handles state, retries, and action execution independently.

## What they did

Built an autonomous trading agent using Claude Opus 4.7 that continuously monitors market data, makes trade decisions, and executes them in a persistent loop without human oversight.

## Relevance to YOLO loop

This is a direct instantiation of the YOLO loop architecture — a persistent observe/decide/act cycle. The pattern (polling + Claude decision + action execution) is reusable for any autonomous agent task beyond trading.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-04-19-claude-24-7-trader` |
| Channel | NateHerk |
| Video | [I Turned Claude Opus 4.7 Into a 24/7 Trader](https://www.youtube.com/watch?v=6MC1XqZSltw) |
| Published | 2026-04-19 |
| Ingested upstream | 2026-04-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

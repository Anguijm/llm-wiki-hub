# Implement jury-and-judge multi-agent pattern for high-stakes tasks with no empirically correct answer

> Back to [[experiments-index]]

Source: **[Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech](https://www.youtube.com/watch?v=YZQsWVeN3rE)** · aie · 2026-07-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we replace single-agent responses on subjective or multi-factor tasks with a panel of independent analyst agents each producing evidence-cited opinions, fed to a consensus judge agent that weighs reasoning quality rather than averaging answers, then output trustworthiness increases because independent analysis eliminates single-point-of-failure hallucination and the judge escalates to a larger jury when consensus is insufficient.

## What they did

Alex described Upside's jury-and-judge workflow for multi-touch attribution (a problem with no empirically correct answer). A user requests attribution on a deal; instead of one agent answering, the system spins up N independent analyst agents that each examine the same data independently and produce evidence-cited opinions. A consensus judge agent receives all opinions, treats them as input (not fact), weighs reasoning quality of each analyst, and produces a final attribution answer. If consensus is below threshold, the jury is expanded. He noted this mirrors real-world jury systems and empirically outperforms single-agent deliberation. He also flagged an 'agent tier' principle: never use low-intelligence crowbarred-into-subscription models (e.g., Slackbot MCP) for important work — tier-2 minimum requires powerful model, sub-agents, plan mode, full MCP support, and file editing.

## Relevance to YOLO loop

Provides a trust architecture pattern for the YOLO loop's output validation on tasks where ground truth is unavailable — multiple independent passes with a synthesis judge catches reasoning failures that single-pass verification misses.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-11-jury-judge-multi-agent-validation` |
| Channel | aie |
| Video | [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech](https://www.youtube.com/watch?v=YZQsWVeN3rE) |
| Published | 2026-07-11 |
| Ingested upstream | 2026-07-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Add a hash-dedupe plus cheap-classifier gate to vault capture

> Back to [[experiments-index]]

Source: **[My Jev Pi Durable Agent CURATES News: HYPE, FACT, or SIGNAL](https://www.youtube.com/watch?v=OLqP8jxJ0Wc)** · idd · 2026-10-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we hash-dedupe incoming items and score them with a cheap classifier (hype/fact/signal plus keyword weights) before any expensive LLM call, then vault capture will cost fewer tokens and surface better candidates for the newsletter because most items are filtered out before the costly model runs.

## What they did

IndyDevDan ran a cron-triggered sweep every minute that pulled stories from Hacker News and official releases and removed exact duplicates by content hash. A fast classifier called Jev then scored each remaining story as hype, fact, or signal, and those scores gated calls to cheaper LLMs (GPT-6 Luna, Haiku 5.5). A natural-language prompt raised the Gemini keyword weight from 1.2 to 1.3 in the taste config. He warned that without aggressive gating, token and compute costs compound, and that the taste config must be calibrated by each user.

## Relevance to YOLO loop

high: It shows a cheap-gating pattern for proactive agents, plus conversational tuning of a config, that carries over to Claude Code background workflows.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-19 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `idd-2026-10-19-cheap-gate-vault-capture` |
| Channel | idd |
| Video | [My Jev Pi Durable Agent CURATES News: HYPE, FACT, or SIGNAL](https://www.youtube.com/watch?v=OLqP8jxJ0Wc) |
| Published | 2026-10-19 |
| Ingested upstream | 2026-10-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

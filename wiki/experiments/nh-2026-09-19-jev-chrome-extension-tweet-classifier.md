# Use Jev as a real-time stream classifier inside a Chrome extension to label content on screen

> Back to [[experiments-index]]

Source: **[I Tested Jev on 12 Real Use Cases. My Honest Thoughts.](https://www.youtube.com/watch?v=ymgH8jS6Wb8)** · nh · 2026-09-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we wire Jev into a Chrome extension that intercepts incoming feed items (e.g. tweets), then we can label them as breaking/golden-nugget/AI-slop in real time because Jev's sub-200ms latency and free output tokens make per-item classification economically viable at scroll speed.

## What they did

Nate built a Chrome extension that passes X (Twitter) tweet text to Jev on the backend as each item appears on screen. Jev classifies each tweet into predefined categories instantly. He also built a paper-trading bot that queries Jev every second to predict Bitcoin price direction (up/down/unclear) and place trades, demonstrating Jev's viability for high-frequency decision loops. He benchmarked Jev against other models showing 20-200x speed improvement and 40-400x cost reduction, and compared daily running costs (~$2/day for Jev vs. multiples more for Soul/Opus/Fable).

## Relevance to YOLO loop

Shows how to insert Jev as a high-frequency triage layer before any expensive LLM step in a YOLO loop — classifying/routing data at ingestion time so downstream agents only process pre-filtered, high-signal items.

## Notes

Context window limitation: Jev is 64k tokens vs ~1M for Claude/GPT. Best used as a pre-filter feeding a larger model, not as a replacement.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-19-jev-chrome-extension-tweet-classifier` |
| Channel | nh |
| Video | [I Tested Jev on 12 Real Use Cases. My Honest Thoughts.](https://www.youtube.com/watch?v=ymgH8jS6Wb8) |
| Published | 2026-09-19 |
| Ingested upstream | 2026-09-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

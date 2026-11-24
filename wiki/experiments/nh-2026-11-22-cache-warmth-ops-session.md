# Add a cache-warmth status bar to the always-on ops Claude Code session

> Back to [[experiments-index]]

Source: **[Anthropic Engineer Explains: How to Stop Hitting Claude's Token Limit](https://www.youtube.com/watch?v=0RF9ml43ups)** · nh · 2026-11-22

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we add a status bar that warns 5 minutes before the prompt cache expires, and stop switching models or adding MCPs mid-session in the ops Claude Code session, then weekly token use drops and cache hit rate stays in the 90s because the unchanged prefix is billed at about 1/10th the input price.

## What they did

Nate Herk, relaying guidance from Anthropic engineers, found his Claude read about 200 tokens per token written, mostly cached input. He built a custom Claude Code status bar that warns before the cache expires (about 1 hour on subscriptions, 5 minutes on the API). Keeping a 400,000-token cache warm cost about $0.08, versus about $3.50 to rebuild it. He also picks the model and tools before the first message, uses /clear between unrelated tasks, and runs /doctor to prune CLAUDE.md.

## Relevance to YOLO loop

high: Prefix-cache hygiene (fixed model and tool set, cache-expiry warnings, one task per session) is a token-cost technique not covered by the existing practices.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-23 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-11-22-cache-warmth-ops-session` |
| Channel | nh |
| Video | [Anthropic Engineer Explains: How to Stop Hitting Claude's Token Limit](https://www.youtube.com/watch?v=0RF9ml43ups) |
| Published | 2026-11-22 |
| Ingested upstream | 2026-11-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

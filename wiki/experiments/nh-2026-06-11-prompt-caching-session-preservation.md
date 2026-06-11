# Preserve prompt cache by avoiding model switches and idle gaps over 1 hour to cut token costs 10x

> Back to [[experiments-index]]

Source: **[Give Me 10 Mins and I'll Save You Millions of Claude Tokens](https://www.youtube.com/watch?v=6cEQEba0i2A)** · nh · 2026-06-11

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we keep Claude Code sessions active within 1-hour windows, avoid mid-session model switches (including /model opus plan which swaps models during plan→execute), and edit CLAUDE.md only between sessions, then cached tokens stay valid and cost only 10% of fresh input tokens, dramatically extending effective session limits because cache invalidation forces full re-processing of the entire conversation history.

## What they did

Nate showed his token dashboard revealing 91M cached tokens saved in one day and 300M+ in a week. He explained the cache TTL: 1 hour for Claude Code subscriptions, 5 minutes for API/sub-agents. He walked through a 4-turn cache growth diagram (system layer globally cached, project layer per-project cached, conversation layer grows per turn). He identified three cache-breaking actions: waiting >1 hour, switching models mid-session (including the 'model opus plan' trick), and changing the system prompt during a session. He provided a free open-source token dashboard GitHub repo that reads local Claude Code session logs and visualises cache_create vs cache_read vs input/output tokens per day.

## Relevance to YOLO loop

Cache management is a hidden multiplier on loop efficiency: a single accidental model switch or 1-hour idle can reset the cache and consume the session limit 10x faster, breaking long autonomous runs.

## Notes

Critical: 'model opus plan' setting breaks cache on every plan/execute toggle — net effect on session limit needs measuring. CLAUDE.md edits safe mid-session because they don't apply until session restart. Token dashboard is open-source GitHub repo, available via School community. Cache create = 1x cost, cache read = 0.1x cost.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-06-11-prompt-caching-session-preservation` |
| Channel | nh |
| Video | [Give Me 10 Mins and I'll Save You Millions of Claude Tokens](https://www.youtube.com/watch?v=6cEQEba0i2A) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

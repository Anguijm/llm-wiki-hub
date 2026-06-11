# Build a personal token-burn dashboard to surface AI usage habits and expand imagination

> Back to [[experiments-index]]

Source: **[My Codex Ran 800 Million Tokens in A Day. The Real Story Isn't Cost.](https://www.youtube.com/watch?v=l8BloTSLK6M)** · nb · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we build a visual token-burn dashboard that shows daily AI usage by model and activity, then we will identify underutilized agent patterns and expand our use of AI because seeing behavioral shifts in chart form creates a concrete feedback loop that abstract usage feelings cannot provide.

## What they did

Speaker used Codex to build a token-burn dashboard styled after GitHub contribution charts, using a Tufte-inspired open-source skill. The dashboard shows daily token burn, same-day activity breakdown, and model distribution. For Claude (where token counts aren't directly visible outside the API), he approximated usage from logs and artifacts. The dashboard revealed a visible behavioral shift when he started using Codex, showing increased token usage correlating with higher-quality outputs. He made multiple versions (Claude-leaning, ChatGPT-leaning, multi-line) available on Substack. He used the dashboard to notice when new features like /workflows changed his usage patterns the same day they were adopted.

## Relevance to YOLO loop

Provides observability into our own dev loop. If we instrument token consumption across Claude Code and Codex sessions we can see which experiment types drive the most agent utilization and correlate that with output quality or velocity.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-06-11-token-burn-dashboard` |
| Channel | nb |
| Video | [My Codex Ran 800 Million Tokens in A Day. The Real Story Isn't Cost.](https://www.youtube.com/watch?v=l8BloTSLK6M) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

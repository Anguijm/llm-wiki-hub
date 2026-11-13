# Route research browsing through Only CLI and measure tokens

> Back to [[experiments-index]]

Source: **[This Finally Cut Claude Code's Token Usage In Half](https://www.youtube.com/watch?v=6gT2sGrYgHk)** · ail · 2026-11-09

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we route the daily researched-stories agent's web fetching through Only CLI's numbered outlines and on-demand section reads, then token use on a fixed research run will drop by about 20% because pages no longer enter context as raw HTML.

## What they did

AI Labs replaced Claude Code's built-in web tool with the open-source Only CLI (OC), enforced through claude.md or agents.md. OC returns a numbered outline of about 500 tokens and fetches cached sections on demand, with shortcuts for Hacker News, GitHub, Wikipedia and Stack Overflow. On a 28-post research benchmark it cut usage from 4.9M to 3.9M tokens (21%). It also fetched npm and Stack Overflow pages that the native tool could not. They note OC is redundant on sites that already publish llm.txt.

## Relevance to YOLO loop

medium: This is a token-efficiency tool swap, close to existing tool-pruning experiments.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-12 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `ail-2026-11-09-only-cli-web-token-cut` |
| Channel | ail |
| Video | [This Finally Cut Claude Code's Token Usage In Half](https://www.youtube.com/watch?v=6gT2sGrYgHk) |
| Published | 2026-11-09 |
| Ingested upstream | 2026-11-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

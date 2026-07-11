# Deploy a local Claude Code token usage dashboard via GitHub repo

> Back to [[experiments-index]]

Source: **[Claude Code for Non-Coders (6 Hour Course)](https://www.youtube.com/watch?v=jdbOVepEtUE)** · nh · 2026-07-11

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run a local token dashboard (served via localhost) that reads past Claude Code session files and aggregates token consumption, then we can track spending and session patterns without relying on Anthropic's dashboard, because the dashboard parses local session JSON files directly.

## What they did

Nate shared a GitHub repo (available in his free School community) that spins up a local token dashboard on localhost. Users give the repo link to Claude Code, ask it to set up on localhost, and it auto-imports past session token data. He also mentioned a session handoff skill that preserves context across sessions to manage token windows.

## Relevance to YOLO loop

Supports the observability layer of the YOLO loop — tracking token burn rate per session helps optimize context loading and agent invocation frequency.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-07-11-token-dashboard-local` |
| Channel | nh |
| Video | [Claude Code for Non-Coders (6 Hour Course)](https://www.youtube.com/watch?v=jdbOVepEtUE) |
| Published | 2026-07-11 |
| Ingested upstream | 2026-07-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

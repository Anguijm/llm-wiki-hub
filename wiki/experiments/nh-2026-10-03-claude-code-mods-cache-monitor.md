# Add a Cache-Expiry and Session-Cost Monitor Mod to Claude Code

> Back to [[experiments-index]]

Source: **[Claude Code Mods Are Game Changers. Set Up These 5 NOW.](https://www.youtube.com/watch?v=9hetShMMp2s)** · nh · 2026-10-03

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we install a Claude Code mod that displays cache age, context token count, session cost, and a one-click session handoff button in the UI, then we will reduce accidental cache expiry costs and context rot because the information needed to make handoff decisions is always visible without switching to the terminal.

## What they did

Nate Herk demonstrated a cache-monitoring mod he built for Claude Code desktop. It shows current cache age (countdown from 60-minute expiry), context window size in tokens, session and weekly limits, estimated API cost if cache expired, and a button that runs his session-handoff skill and then clears context. He built it by asking Claude to analyze his session logs and suggest mods that would save money and reduce context rot.

## Relevance to YOLO loop

Directly addresses context management in long coding sessions. Installing this mod (or building an equivalent for our setup) would make session handoff timing explicit and reduce the hidden cost of letting caches expire during multi-hour agentic runs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-10-03-claude-code-mods-cache-monitor` |
| Channel | nh |
| Video | [Claude Code Mods Are Game Changers. Set Up These 5 NOW.](https://www.youtube.com/watch?v=9hetShMMp2s) |
| Published | 2026-10-03 |
| Ingested upstream | 2026-10-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

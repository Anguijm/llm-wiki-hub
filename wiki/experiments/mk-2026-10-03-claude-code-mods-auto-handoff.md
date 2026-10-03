# Install an Auto-Handoff Mod That Triggers Session Refresh at a Token Threshold

> Back to [[experiments-index]]

Source: **[Claude Code Now Has Mods. Here Are 10 Worth Stealing](https://www.youtube.com/watch?v=uvIopT_2sY0)** · mk · 2026-10-03

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we configure a Claude Code mod to automatically initiate a session handoff when context usage crosses a defined threshold (e.g., 85%), then we will avoid the hallucination-prone 'context rot' zone without requiring manual monitoring because the mod handles the transition before quality degrades.

## What they did

Mark Kashef demonstrated an auto-handoff mod for Claude Code that monitors context token consumption and automatically spins up a fresh session when a configurable threshold is reached. He showed /auto-handoff on with threshold set to 85%, and a /handoff-now command for manual early triggering. He also showed a mass-nuke bash command to remove all mods at once. He provided all his mods and invocation prompts as a free download.

## Relevance to YOLO loop

Directly addresses context window management in our yolo loop. Automating the handoff decision removes a manual monitoring burden during long autonomous runs and ensures consistent output quality by keeping the agent in the high-accuracy region of its context window.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-10-03-claude-code-mods-auto-handoff` |
| Channel | mk |
| Video | [Claude Code Now Has Mods. Here Are 10 Worth Stealing](https://www.youtube.com/watch?v=uvIopT_2sY0) |
| Published | 2026-10-03 |
| Ingested upstream | 2026-10-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

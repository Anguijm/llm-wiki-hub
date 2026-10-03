# Implement a Multi-Agent File Collision Guard Mod in Claude Code

> Back to [[experiments-index]]

Source: **[Claude Code Mods Are Game Changers. Set Up These 5 NOW.](https://www.youtube.com/watch?v=9hetShMMp2s)** · nh · 2026-10-03

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we install a collision-guard mod that intercepts file writes and checks whether the target file was modified by another Claude Code session in the last 30 minutes, then we will prevent silent overwrites when running parallel agents on the same codebase because the mod surfaces the conflict before the edit lands and asks for explicit intent.

## What they did

Nate Herk built and demonstrated a 'collision guard' mod that fires before every file write or edit. It checks whether the file was touched by another session within the last 30 minutes and, if so, presents a UI prompt asking whether to proceed, move to a worktree, or cancel. He showed a concrete scenario where one session changed a price field and a second session attempted to add a badge to the same HTML file—collision guard caught it and asked for intent before either change was lost.

## Relevance to YOLO loop

Critical safety layer for parallel agentic workflows. When we run multiple Claude Code agents on overlapping parts of a codebase (common in our yolo loop during large refactors), this mod prevents silent data loss without requiring manual coordination between sessions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-10-03-claude-code-mods-collision-guard` |
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

# Add a Codex Adversarial-Review Step After Claude Code's Primary Build

> Back to [[experiments-index]]

Source: **[I Made Codex and Claude Code Build the Same App. One Clearly Won.](https://www.youtube.com/watch?v=WCrnS09vpfo)** · nh · 2026-08-14

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run a Codex-powered adversarial review pass on Claude Code's output, then we will surface bugs and edge cases missed by the primary agent because Codex applies broader test coverage strategies (cross-browser, property-based, fault-injection) that Claude Code deprioritizes in the interest of speed.

## What they did

The speaker mentioned using a Codex plugin for Claude Code that executes an adversarial review after the main build. He reported it 'almost always finds things that my Claude Code workflow missed — bugs, edge cases, things like that.' This is a lightweight bolt-on rather than running full Codex end-to-end, preserving Claude Code's speed and cost advantages while borrowing Codex's testing thoroughness.

## Relevance to YOLO loop

Maps cleanly to a post-build verification stage in the YOLO loop: after the primary coding agent completes a task, invoke the adversarial reviewer as a sub-agent before marking the task done. Low effort since it hooks into an existing Claude Code session rather than spinning up a separate Codex run.

## Notes

Plugin not named explicitly — needs research to identify the specific Codex adversarial review plugin for Claude Code. Could also be implemented manually as a second system-prompt pass instructing the model to 'find every bug, edge case, and security issue in the following code.'

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-14-adversarial-review-plugin` |
| Channel | nh |
| Video | [I Made Codex and Claude Code Build the Same App. One Clearly Won.](https://www.youtube.com/watch?v=WCrnS09vpfo) |
| Published | 2026-08-14 |
| Ingested upstream | 2026-08-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

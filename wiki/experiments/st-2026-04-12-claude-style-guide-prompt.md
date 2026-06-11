# Encode a YOLO Loop Style Guide as a Reusable Claude System Prompt

> Back to [[experiments-index]]

Source: **[How I Taught Claude To Edit My YouTube Videos](https://www.youtube.com/watch?v=wmIO2rs-AIs)** · st · 2026-04-12

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we distill our dev loop's coding conventions and output format rules into a compact system prompt style guide fed to Claude on every task, then output consistency will improve and post-generation editing time will decrease because Claude will have explicit style constraints rather than inferring them.

## What they did

Shaw created a personal editing style guide document that Claude references each session to maintain consistent edit decisions across multiple videos, treating the style guide as persistent context.

## Relevance to YOLO loop

Directly applicable to YOLO loop system prompt design. We can adopt the same pattern to encode our file structure conventions, naming rules, and output formats, reducing drift across long agentic sessions.

## Notes

Adopted 2026-04-13 as already-implemented: the YOLO loop already encodes style conventions via design.md (CSS/UI patterns), program.md (methodology), skills/*.md (per-phase contracts), and _hot.md (active context). This experiment validates the existing approach. No new work needed — mark as done/adopt.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-12 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `st-2026-04-12-claude-style-guide-prompt` |
| Channel | st |
| Video | [How I Taught Claude To Edit My YouTube Videos](https://www.youtube.com/watch?v=wmIO2rs-AIs) |
| Published | 2026-04-12 |
| Ingested upstream | 2026-04-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Front-load a full planning document to Claude before coding to prevent spaghetti code across sessions

> Back to [[experiments-index]]

Source: **[AI Is Fast. AI Projects Are Slow. Let's Fix That.](https://www.youtube.com/watch?v=3xZ78HHdqAk)** · mlops · 2026-06-11

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we provide Claude with a complete planning document (architecture decisions, reusable component inventory, coding conventions) before starting a coding session, then output code quality will be higher and cross-session consistency will improve because Claude's weakness is not remembering prior decisions across context compactions, and the document serves as persistent memory.

## What they did

Panel discussed that Claude is strong at implementing a specific plan but weak at iterative engineering across sessions—it forgets shared CSS, duplicates components, and ignores prior patterns. The fix they described was externalizing the plan to a document that survives context compaction, referencing it at session start. One panelist noted that giving Claude access to the full plan upfront consistently produced better code, and that the document approach prevents context loss when compacting long sessions.

## Relevance to YOLO loop

Maps directly to our claude.md / AGENTS.md practice. This experiment suggests we should also include an explicit component inventory and style-guide section in that file and measure reduction in duplicated code artifacts.

## Notes

Backlog triage 2026-06-24 (owner-preference model). Front-loaded planning doc — same lesson as adopted vertical-planning (env-diff zero-rework evidence).

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-06-11-planning-doc-to-prevent-spaghetti-code` |
| Channel | mlops |
| Video | [AI Is Fast. AI Projects Are Slow. Let's Fix That.](https://www.youtube.com/watch?v=3xZ78HHdqAk) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Build a Claude-Driven Video Edit Instruction Pipeline

> Back to [[experiments-index]]

Source: **[How I Taught Claude To Edit My YouTube Videos](https://www.youtube.com/watch?v=wmIO2rs-AIs)** · st · 2026-04-12

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we provide Claude with a transcript plus a structured editing style guide, then Claude can output a precise cut list or edit instructions because it can reason over temporal text data and apply consistent style rules without human review of every frame.

## What they did

Shaw described a workflow where Claude ingests video transcripts and a personal editing style guide, then generates timestamped cut instructions or edit decisions that a human or automated tool can execute, effectively offloading the cognitive editing work to the model.

## Relevance to YOLO loop

Maps to any pipeline step where Claude must process long-form structured text and produce actionable output lists. The transcript-plus-style-guide pattern is reusable for code review, doc generation, or any task requiring consistent rule application over large inputs.

## Notes

Discarded 2026-04-13: video editing pipeline is out of scope for the YOLO dev loop. The transcript-plus-style-guide pattern is interesting but already embodied in our existing design.md + program.md + skills system. No net-new technique to adopt.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-12 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `st-2026-04-12-claude-video-editing` |
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

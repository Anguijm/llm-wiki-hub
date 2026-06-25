# Use a 'Grill Me' interrogation skill to extract tacit knowledge into reusable context docs before building

> Back to [[experiments-index]]

Source: **[The Skill That 10x'd My Claude Code Projects](https://www.youtube.com/watch?v=c0kaKxM2pHg)** · nh · 2026-06-11

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we run a structured interview skill that relentlessly asks one question at a time, checkpoints answers to a markdown brainstorm file after each exchange, and loops until no gaps remain, then skills and project context built afterwards will succeed on the first iteration at ~90% quality instead of ~70%, because the model has explicit, persisted domain knowledge rather than relying on incomplete brain-dumps.

## What they did

Nate described and demonstrated the 'Grill Me' skill (originally by Matt PCO, extended by Nate). The skill is a short markdown file that instructs Claude to interview the user relentlessly about a process or plan, ask one question at a time, provide a recommended answer for each, and checkpoint all Q&A to a brainstorm markdown file in a /brainstorms folder at project root. After the session ends, Claude identifies gaps between the conversation and existing skill/doc files and proposes updates. Nate showed brainstorm files with Q&A logs, key decisions, and open flags for missing info to gather from stakeholders. He invoked it via /grill-me slash command.

## Relevance to YOLO loop

Sharpens the axe before the YOLO loop starts: richer upfront context means fewer correction cycles, lower token burn, and more consistent skill execution across sessions.

## Notes

Skill available in Nate's free School community. Key addition over original: automatic checkpointing after every question prevents context-window amnesia on long sessions. Output: /brainstorms/<topic>.md with Q&A log + key decisions + open flags.

Backlog triage 2026-06-24 (owner-preference model). Context-extraction interview skill; cheap, feeds planning/brainstorm.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-06-11-grill-me-context-extraction` |
| Channel | nh |
| Video | [The Skill That 10x'd My Claude Code Projects](https://www.youtube.com/watch?v=c0kaKxM2pHg) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

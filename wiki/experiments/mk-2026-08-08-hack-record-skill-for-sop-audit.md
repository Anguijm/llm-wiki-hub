# Override Codex 'Record and Replay' skill to audit and SOP-ify manual workflows

> Back to [[experiments-index]]

Source: **[Claude Code and Codex Quietly Learned to Watch Video](https://www.youtube.com/watch?v=0I-J1aoxYQY)** · mk · 2026-08-08

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we invoke Codex's built-in Record and Replay skill but explicitly instruct it NOT to build a skill and instead just watch and critique, then it will produce a detailed SOP and automation opportunities report for any manual workflow because the underlying video-interpretation capability is decoupled from the skill-creation system prompt and can be redirected with a plain instruction.

## What they did

Mark opened the Record and Replay skill in Codex, then sent a prompt telling it to record his screen for 30 minutes, observe his manual X/Twitter research workflow, and output a full SOP plus API-automation recommendations—explicitly forbidding it from creating a skill. Codex recorded in real time, then on stop produced a step-by-step process map, identified the X API as an automation vector, and outlined how to eliminate manual steps.

## Relevance to YOLO loop

Maps to the 'observe and reflect' phase of our loop: instead of manually documenting repetitive developer workflows, we can record them and have the agent propose which steps to automate next, feeding directly into backlog creation.

## Notes

Audio is not captured by the Record skill—only screen visuals. For workflows where narration matters, a separate Loom recording fed as MP4 is preferred. EU users may not have the Record skill and should use the MP4 drag-drop approach instead.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-08-08-hack-record-skill-for-sop-audit` |
| Channel | mk |
| Video | [Claude Code and Codex Quietly Learned to Watch Video](https://www.youtube.com/watch?v=0I-J1aoxYQY) |
| Published | 2026-08-08 |
| Ingested upstream | 2026-08-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

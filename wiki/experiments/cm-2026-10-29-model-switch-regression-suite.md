# Add a capability regression suite for model upgrades

> Back to [[experiments-index]]

Source: **[The 4 Components of Every Successful AI Second Brain (Build These Now)](https://www.youtube.com/watch?v=qIWB1yMsqRo)** · cm · 2026-10-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we keep a fixed suite of typical agent tasks and rerun it whenever the underlying model changes, then we will catch regressions in our Claude Code workflows before they hit daily use because behavior can shift between model versions.

## What they did

Cole Medin keeps a running test suite of typical capability tasks and runs it as an evaluation benchmark when switching models (e.g. Opus 5 to Opus 5.5). He also loads three root markdown files (soul.md, user.md, memory.md) via startup hooks and turns any workflow explained more than three times into a slash-command skill.

## Relevance to YOLO loop

high: This is a verification loop for skills, hooks and memory in Claude Code workflows, run on every model change.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-29 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `cm-2026-10-29-model-switch-regression-suite` |
| Channel | cm |
| Video | [The 4 Components of Every Successful AI Second Brain (Build These Now)](https://www.youtube.com/watch?v=qIWB1yMsqRo) |
| Published | 2026-10-29 |
| Ingested upstream | 2026-10-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

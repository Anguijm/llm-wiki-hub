# Consolidate instructions into a root AGENTS.md with nested per-domain files

> Back to [[experiments-index]]

Source: **[Your Claude + Codex Setup Is a Mess (Here's the Fix)](https://www.youtube.com/watch?v=eXoBC1TY8m4)** · mk · 2026-10-17

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we merge overlapping instructions into one root AGENTS.md and move per-project guidance into nested AGENTS.md files in subfolders, then conflicting instructions and token overhead will shrink because each session loads only the relevant, non-duplicated context.

## What they did

Mark Kashef consolidated overlapping Claude, Codex and Gemini instructions into a single root AGENTS.md that points to business subfolders, each with its own nested AGENTS.md. He also showed a three-step decision framework for new skills based on utility, scope and maintenance. He cautioned that a manually set global CLAUDE.md makes every project inherit instructions that must then be overridden.

## Relevance to YOLO loop

high: It restructures harness instructions and memory into a model-agnostic hierarchy and adds a gate for adopting new skills.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-19 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-10-17-unified-agents-md-hierarchy` |
| Channel | mk |
| Video | [Your Claude + Codex Setup Is a Mess (Here's the Fix)](https://www.youtube.com/watch?v=eXoBC1TY8m4) |
| Published | 2026-10-17 |
| Ingested upstream | 2026-10-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

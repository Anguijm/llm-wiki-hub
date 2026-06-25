# Audit and promote skills to global vs. project scope as a prerequisite to multi-agent reliability

> Back to [[experiments-index]]

Source: **[This Claude Code Setup Runs My Entire Business](https://www.youtube.com/watch?v=7aQbN543Mec)** · mk · 2026-05-03

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we deliberately audit all Claude Code skills and classify each as global (all agents) or project-scoped (specific terminal/project), then multi-agent pipelines will be more reliable and context windows less polluted because agents only receive skills relevant to their role.

## What they did

Speaker described his prerequisite hygiene step before building any advanced agent layer: cleaning up file/folder structure, then making an explicit decision for every skill about whether it should be global (inherited by all agents across the OS) or project-level (scoped to one agent or workflow). He noted this same principle applies to Claude Code, Codex, or Gemini. He framed the entire multi-agent OS as a data engineering problem—getting this classification right is what makes iterative improvement tractable.

## Relevance to YOLO loop

Low-effort forcing function that prevents skill sprawl and context noise as the YOLO loop's skill library grows; doing this audit now avoids expensive refactoring later when more agents are added.

## Notes

Backlog triage 2026-06-24 (owner-preference model). Skill scope hygiene; cheap, supports the skills-as-recipes architecture.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-03 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-05-03-global-vs-project-skill-hygiene` |
| Channel | mk |
| Video | [This Claude Code Setup Runs My Entire Business](https://www.youtube.com/watch?v=7aQbN543Mec) |
| Published | 2026-05-03 |
| Ingested upstream | 2026-05-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Inject a plain-English explanation skill into coding agents before architecture decisions

> Back to [[experiments-index]]

Source: **[Nobody Laid Out The Five Kinds Of Software You Can Make. So I Did.](https://www.youtube.com/watch?v=joRXo6x7Pgk)** · nb · 2026-08-19

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we prepend a 'plain English technical documentation' skill prompt to coding agent sessions and require the agent to explain major choices before writing code, then non-technical builders will make better-informed architectural decisions and experience fewer costly mid-build surprises, because the agent is forced out of jargon-heavy defaults into accessible language.

## What they did

Nate described a reusable skill (shared in his Substack) that forces coding agents like Claude Code or Codex to stop speaking 'agent English' and explain options in plain language. The workflow is: attach the skill, ask the agent to present options plainly, make an informed choice, then proceed. He noted this is especially valuable at branch points like choosing a backend or transport layer.

## Relevance to YOLO loop

Applies at the agent-instruction layer of our loop: wrapping agent sessions with an explanation-first skill reduces the need for post-hoc debugging of decisions the builder didn't understand when they were made.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-08-19-plain-english-agent-skill` |
| Channel | nb |
| Video | [Nobody Laid Out The Five Kinds Of Software You Can Make. So I Did.](https://www.youtube.com/watch?v=joRXo6x7Pgk) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

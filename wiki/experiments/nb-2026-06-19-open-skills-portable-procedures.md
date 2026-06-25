# Structure agent procedures as scoped markdown skills with verification contracts

> Back to [[experiments-index]]

Source: **[Your AI Skills Are Trapped | Here's How to Own Them](https://www.youtube.com/watch?v=9PUaEj0pMYE)** · nb · 2026-06-19

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we encode agent procedures as narrow, scoped markdown files each with an explicit trigger, boundary, and proof/verification standard (rather than stuffing rules into monolithic system prompts), then agents will execute more reliably across tools and sessions because each skill has a single clear job and a checkable done-condition.

## What they did

Nate described 'Open Skills', a public library of 31 reusable agent procedure files organized into 7 categories with 7 runbooks. Each skill markdown file defines a job, scope, trigger, boundary, and proof standard. Skills are composable into runbooks and designed to be portable across Claude Code, Cursor, Codex and other agent harnesses via a shared .skill.md convention. He distinguished personal scope (belongs to the user) from project scope (belongs to the repo), and argued this solves prompt bloat, reexplanation tax, instruction fragmentation, and weak verification—the four failure modes of serious agent workflows.

## Relevance to YOLO loop

Directly applicable: the YOLO loop can load skill files per-task to eliminate reexplanation overhead, and the verification/proof-standard field maps directly to the loop's stop condition and output validation step.

## Notes

Open Skills repo URL shown on screen but not captured in transcript. Worth finding at launch URL. Key differentiator vs prompt libraries: every file has job+scope+trigger+boundary+proof standard.

Backlog triage 2026-06-24 (owner-preference model). Scoped skills w/ verification contracts — skills + verification double match.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-19 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-06-19-open-skills-portable-procedures` |
| Channel | nb |
| Video | [Your AI Skills Are Trapped | Here's How to Own Them](https://www.youtube.com/watch?v=9PUaEj0pMYE) |
| Published | 2026-06-19 |
| Ingested upstream | 2026-06-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

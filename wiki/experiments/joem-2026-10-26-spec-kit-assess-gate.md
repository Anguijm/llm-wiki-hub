# Gate feature ideas through Spec Kit assess before coding

> Back to [[experiments-index]]

Source: **[Spec Kit Guide: Assess Extension](https://www.youtube.com/watch?v=XDzQlrKdNW8)** · joem · 2026-10-26

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run new feature ideas through the Spec Kit assess pipeline (intake, research, define, shape, decide) before any implementation, then low-value work is killed early and scope is clearer because the decide step checks the concept against the project constitution.

## What they did

Joe Maddalone installed the Specify CLI with uv, initialized Spec Kit with OpenCode, and added the assess extension. On a task manager app he ran the five assess commands, producing intake.md, research.md, problem.md and concept.md. The shape step gave three options (minimal sort, persisted preferences, do nothing). The decide step returned 'go' for option A, and the approved concept then went through specify, plan, task, implement and converge to add sort controls. Caveats: inline arguments after intake can error in OpenCode, and it needs an existing codebase and a clear constitution.

## Relevance to YOLO loop

high: A structured go/kill gate before agentic coding could filter backlog ideas in the YOLO loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-26 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `joem-2026-10-26-spec-kit-assess-gate` |
| Channel | joem |
| Video | [Spec Kit Guide: Assess Extension](https://www.youtube.com/watch?v=XDzQlrKdNW8) |
| Published | 2026-10-26 |
| Ingested upstream | 2026-10-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

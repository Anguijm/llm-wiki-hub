# Use Claude 4 to design a goal harness that guides a downstream coding model

> Back to [[experiments-index]]

Source: **[Free Fable 5 tokens this weekend? Here's how to max them](https://www.youtube.com/watch?v=RtxUdvSTQGc)** · nb · 2026-07-04

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use Claude 4 to design a structured goal harness (detailed goals, constraints, and evaluation criteria) before handing a task to a coding-specialized model, then the coding model will produce better results because it operates within a well-defined problem specification it did not have to infer itself.

## What they did

Speaker described a two-model workflow: use Claude 4 to design detailed goals and a 'goal harness' for a complicated coding task, then pass that harness to a coding model (he mentioned Codex 5.5 as an example) to execute. The idea is Claude 4 acts as a meta-planner that structures the problem space rather than solving the code directly.

## Relevance to YOLO loop

Maps directly to the planning layer of the YOLO loop. We could insert a Claude 4 harness-generation step before spinning up the coding agent, treating Claude 4 as a task-spec generator rather than the executor. This could reduce ambiguity and failed iterations in the coding sub-loop.

## Notes

Complements the short-prompt experiment above. The two ideas together suggest a pattern: Claude 4 for problem framing and harness design, specialist model for execution. Worth prototyping on a real feature task in the loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-04-claude4-goal-harness-for-codegen` |
| Channel | nb |
| Video | [Free Fable 5 tokens this weekend? Here's how to max them](https://www.youtube.com/watch?v=RtxUdvSTQGc) |
| Published | 2026-07-04 |
| Ingested upstream | 2026-07-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

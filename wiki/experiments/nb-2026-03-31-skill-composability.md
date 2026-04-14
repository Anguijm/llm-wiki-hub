# Design skill outputs as composable handoffs

> Back to [[experiments-index]]

Source: **[Anthropic, OpenAI, and Microsoft Just Agreed on One File Format. It Changes Everything.](https://www.youtube.com/watch?v=0cVuMHaYEHE)** · @NateBJones · 2026-03-31

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we design each YOLO loop phase to produce output formatted as input for the next phase (brainstorm outputs a spec, spec feeds the builder, builder outputs code, code feeds the reviewer), then the pipeline becomes more reliable because each handoff has a clear contract.

## What they did

Nate emphasized composability: the output of one skill should be perfectly formatted as input for the next agent in the chain. Design skills with clear SLAs defining exactly what the agent will and will not get.

## Actionable steps

- Map the current YOLO loop data flow: what does each phase produce and consume?
- Define explicit input/output contracts for each phase
- Ensure brainstorm output is structured enough for the builder to consume without ambiguity
- Test: can Phase 2 refinement run with zero human context injection?

## Success metric

A full build cycle (brainstorm → build → test → review → log) completes with zero human intervention between phases.

## Relevance to YOLO loop

The YOLO loop already chains phases but the handoffs are implicit. Making them explicit contracts would improve autonomous execution.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

Each skill defines explicit Input (what files to read) and Output (what to produce). Bootstrap routes to Tick or Tock. Tick/Tock both call Review as a sub-skill. All skills output to the same state files (session_state.json, learnings.md, yolo_log.json) enabling clean handoffs between sessions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-03-31 | `in_progress` | Defining input/output contracts between skills |
| 2026-03-31 | `done` | Input/output contracts defined in all skill files |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-03-31-skill-composability` |
| Channel | @NateBJones |
| Video | [Anthropic, OpenAI, and Microsoft Just Agreed on One File Format. It Changes Everything.](https://www.youtube.com/watch?v=0cVuMHaYEHE) |
| Published | 2026-03-31 |
| Ingested upstream | 2026-03-31 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

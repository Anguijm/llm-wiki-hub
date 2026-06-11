# Use incremental summarization for context compression in long sessions

> Back to [[experiments-index]]

Source: **[Nvidia Just Open-Sourced What OpenAI Wants You to Pay Consultants For](https://www.youtube.com/watch?v=7AO4w4Y_L24)** · nb · 2026-03-24

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we implement incremental summarization (summarize segments, merge into structured persistent summary) for long YOLO build sessions, then context window usage drops and agent coherence improves because the agent retains key decisions without drowning in raw history.

## What they did

Factory.ai found that incremental summarization — summarizing segments and merging them into a structured persistent summary — was the most effective approach to context compression for long agent sessions.

## Actionable steps

- Identify which YOLO loop sessions hit context limits (refinement runs, multi-project builds)
- Implement structured summaries at natural breakpoints (per-project, per-phase)
- Store summaries in learnings.md or a dedicated context file
- Measure whether session coherence improves in later refinements

## Success metric

Long refinement sessions (10+ projects) maintain coherence without context window exhaustion.

## Relevance to YOLO loop

Phase 2 refinement runs through many projects sequentially and already hits context limits. Structured summarization would help.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

The YOLO loop already implements incremental summarization: learnings.md accumulates per-project insights, conversation compaction summaries preserve key decisions, and memory files store cross-session context. No additional infrastructure needed — the pattern was adopted organically before the experiment was formalized.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-03-29 | `done` | Already implemented naturally — learnings.md IS the incremental summary, conversation summaries handle context compression |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-03-24-context-compression` |
| Channel | nb |
| Video | [Nvidia Just Open-Sourced What OpenAI Wants You to Pay Consultants For](https://www.youtube.com/watch?v=7AO4w4Y_L24) |
| Published | 2026-03-24 |
| Ingested upstream | 2026-03-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

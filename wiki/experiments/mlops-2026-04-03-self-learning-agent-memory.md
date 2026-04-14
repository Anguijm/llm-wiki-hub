# Implement structured memory retrieval so the build agent learns from past builds

> Back to [[experiments-index]]

Source: **[How to Fix Your Agent's Amnesia: Lessons from Building a Self-learning Agent]()** · @MLOps · 2026-04-02

**Status:** `adopted` · **Verdict:** `adopted` · **Effort:** `medium`

---

## Hypothesis

If we give the build agent structured access to past build outcomes (what worked, what failed, which patterns caused bugs), then build quality compounds over time because the agent doesn't repeat mistakes and reinforces successful patterns.

## What they did

MLOps presented lessons from building a self-learning agent — specifically how to fix the 'amnesia' problem where agents forget context between sessions and keep making the same mistakes.

## Actionable steps

- Audit current learnings.md — is it structured enough for agent retrieval?
- Add per-project outcome tags: [success], [failure], [pattern:X] to learnings entries
- Wire learnings.md into the build agent's context window before each build
- Measure: does referencing past learnings reduce bug count in Gemini reviews?

## Success metric

Build agent references relevant past learnings in at least 50% of builds; bug count decreases.

## Relevance to YOLO loop

The YOLO loop already has learnings.md but it's read passively. Making it an active memory retrieval system would close the learning loop.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Notes

Adopted 2026-04-07: validates and extends current build_memory.py (1916 learnings, 263 projects, FTS5). Adoption work: add a feedback loop logging "did the recalled learning prevent a bug?" so we can measure the angle's value over time.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `backlog` | Ingested from Phase 4 YouTube pipeline — title-only inference |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-04-03-self-learning-agent-memory` |
| Channel | @MLOps |
| Published | 2026-04-02 |
| Ingested upstream | 2026-04-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

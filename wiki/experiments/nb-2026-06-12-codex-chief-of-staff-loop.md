# Structure Codex Tasks With Goal-Source-Standard-Permission-Proof Loops

> Back to [[experiments-index]]

Source: **[Only 1 in 1,600 People Use Codex. Here's How to Catch Up.](https://www.youtube.com/watch?v=xqGCbEDbny8)** · nb · 2026-06-12

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we frame every Codex agent task with five explicit components (goal, sources, standard, permission boundary, and proof of completion), then the agent will complete larger multi-step jobs with fewer corrections because it has a closed-loop contract rather than an open-ended prompt.

## What they did

Nate described migrating from chat-style AI use to handing Codex multi-step computer jobs. He articulated a five-part loop structure: give the agent a goal, give it sources, give it a standard to meet, define its permission boundary, and specify the proof that the job is done. He used this to drive file operations, browser use, document rendering, and repeated workflows converted into reusable skills inside Codex.

## Relevance to YOLO loop

Directly maps to our agent task-dispatch layer. The five-part loop structure can be adopted as our standard prompt schema for any autonomous Codex/agent invocation in the YOLO loop, replacing ad-hoc prompts with a repeatable contract that includes exit criteria.

## Notes

Nate also emphasizes converting repeated corrections into reusable Skills/memories in Codex. Worth pairing this experiment with a skill-extraction pass after every completed loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-06-12-codex-chief-of-staff-loop` |
| Channel | nb |
| Video | [Only 1 in 1,600 People Use Codex. Here's How to Catch Up.](https://www.youtube.com/watch?v=xqGCbEDbny8) |
| Published | 2026-06-12 |
| Ingested upstream | 2026-06-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

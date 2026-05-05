# Use Claude Code's New Planning Mode as a Spec-Decomposition Pre-Pass

> Back to [[experiments-index]]

Source: **[Planning In Claude Code Just Got a Huge Upgrade](https://www.youtube.com/watch?v=T4fXb3sbJIo)** · NateHerk · 2026-04-07

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we invoke Claude Code's upgraded planning mode before any implementation task in the YOLO loop, then the resulting step-by-step plan will surface ambiguities and scope issues earlier, reducing mid-task derailments, because the new planning pass forces explicit sub-task enumeration and dependency identification before any code is written.

## What they did

Speaker demonstrated a newly upgraded planning feature in Claude Code that, when triggered, produces a detailed hierarchical task plan (with subtasks, file targets, and sequencing) before writing any code. Showed side-by-side comparison of runs with and without planning mode, with planning-mode runs completing complex multi-file refactors more reliably.

## Relevance to YOLO loop

The YOLO loop's spec stage could be augmented with this planning pre-pass: feed the spec to Claude Code in planning mode, review the decomposition, then execute. This adds a lightweight human-in-the-loop checkpoint at minimal cost.

## Notes

Adopted 2026-04-08: most directly applicable of the 6. Wire into PLAN gate as "use Claude Code planning mode for the experiments/<name>/plan.md deliverable rather than free-form prose." One-line tick prompt change. Tiny work, direct fit with current 4-gate council.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-07 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-04-07-claude-code-planning-mode` |
| Channel | NateHerk |
| Video | [Planning In Claude Code Just Got a Huge Upgrade](https://www.youtube.com/watch?v=T4fXb3sbJIo) |
| Published | 2026-04-07 |
| Ingested upstream | 2026-04-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

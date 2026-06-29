# Audit existing skills against a four-point checklist: trigger, structure, steering, pruning

> Back to [[experiments-index]]

Source: **[Building Great Agent Skills: The Missing Manual](https://www.youtube.com/watch?v=UNzCG3lw6O0)** · aie · 2026-06-29

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we systematically evaluate every skill in our repo against the four-point checklist (trigger correctness, internal structure with branches and steps, steering via leading words in reasoning traces, and pruning of no-ops and sediment), then agent reliability and skill compactness will improve because each checklist item eliminates a distinct failure mode that silently degrades agent behavior without obvious error signals.

## What they did

Matt (aiDotEngineer) presented a talk at AI Engineer World's Fair outlining a rubric for distinguishing good skills from bad ones, motivated by the phenomenon of 'skill hell'. The checklist covers: (1) Trigger — decide user-invocable vs model-invocable, check for false positives/negatives by scanning reasoning traces; (2) Structure — organize into branches, steps, and reference sections, move branch-specific material out of the main skill file; (3) Steering — condense instructions to leading words and verify they appear in agent reasoning traces, consider splitting future phases into separate skills to reduce cognitive load; (4) Pruning — deletion-test for no-ops, remove sediment from multi-author drift, eliminate duplication with a single-source-of-truth rule. He encoded this entire checklist as a new skill ('writing great skills') in his public repo.

## Relevance to YOLO loop

Directly applicable to every skill in our Claude/Codex harness. Running our existing skills through this checklist is a low-cost, high-leverage audit that should tighten agent behavior, reduce context load, and eliminate silent failures before they surface in production runs.

## Notes

The 'writing great skills' skill is available in Matt's public repo (map.got.skills). The key diagnostic tool is scanning reasoning traces to confirm leading words appear — if they don't, the instruction is a no-op. Sediment and no-ops are the most common bloat sources in community-contributed skills.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-29-skill-quality-checklist` |
| Channel | aie |
| Video | [Building Great Agent Skills: The Missing Manual](https://www.youtube.com/watch?v=UNzCG3lw6O0) |
| Published | 2026-06-29 |
| Ingested upstream | 2026-06-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

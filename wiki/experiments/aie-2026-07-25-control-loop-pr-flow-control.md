# Implement Adaptive Flow Control to Prevent PR Stack-Up in Agentic Loops

> Back to [[experiments-index]]

Source: **[Loop Engineering from First Principles — Kyle Mistele, HumanLayer](https://www.youtube.com/watch?v=xIt_mTQp6mY)** · aie · 2026-07-25

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we add a pre-flight check to each loop workflow that halts execution when a previous PR from that loop is still open, then we prevent duplicate and conflicting work from accumulating because it enforces the invariant that a human must review each loop output before the next iteration runs.

## What they did

Kyle described a control-loop architecture for agentic coding in large codebases. Each loop workflow is labeled; before checking out code and running sense-control-actuate steps, the workflow checks whether any open PR with the loop's label already exists. If so, the workflow shuts down immediately. This ensures at most one open PR per loop at any time, eliminating stacking, duplication, and merge conflicts that arise when loops run unattended for days. He also described a version-controlled markdown feedback file and a slash-iterate comment trigger that lets humans steer the loop on the fly without high friction.

## Relevance to YOLO loop

Directly addresses a failure mode in our YOLO loop: unchecked iterations producing conflicting outputs. The label-based PR gate and the version-controlled feedback file are concrete mechanisms we can bolt onto our existing GitHub Actions workflow to add human-in-the-loop steering without blocking velocity.

## Notes

Kyle also mentioned velocity scaling options once the loop is stable: controller picks 3-5 items per run, each gets its own context window, or workflow runs in parallel across team members. HumanLayer published a skill to try this pattern.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-25 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-25-control-loop-pr-flow-control` |
| Channel | aie |
| Video | [Loop Engineering from First Principles — Kyle Mistele, HumanLayer](https://www.youtube.com/watch?v=xIt_mTQp6mY) |
| Published | 2026-07-25 |
| Ingested upstream | 2026-07-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

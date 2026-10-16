# Prompt Claude with the outcome goal rather than the task, backed by groundwork infrastructure

> Back to [[experiments-index]]

Source: **[Stop giving AI tasks. Give it the goal behind the goal.](https://www.youtube.com/watch?v=Gj_GlrTxIWQ)** · eh · 2026-10-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we hand Claude the high-level outcome goal (e.g., 'keep the app crash-free') instead of individual sub-tasks, then throughput and output quality will increase because the model can plan its own task decomposition—provided we supply the necessary groundwork (crash reports, test environments, playbooks) that makes goal-level delegation safe.

## What they did

Drawing on Felix Riesberg's article and his own Foundry app builds, the speaker described four ambition levels: speed, altitude, depth, and range. For altitude, he showed prompts like 'build a system that can generate any app' and 'the world's easiest way to build complex machines just by painting' rather than step-by-step instructions. He emphasized that goal delegation requires groundwork: a release script that tests real downloads, a review page for section-by-section film review, and a playbook of rules baked into Claude's memory so they never need to be repeated. He also showed depth tactics: setting unreasonable targets as reasonable ('exactly 2 minutes, not about two'), using an external judge (Whisper STT) to catch errors the model can't self-detect, and asking for the deeper version rather than the bigger version.

## Relevance to YOLO loop

Core to our YOLO loop prompt design: shifting from task-level to goal-level prompts, combined with a playbook and test harness as groundwork, would let agents self-organize work and reduce round-trip iteration on sub-tasks.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `eh-2026-10-15-altitude-goal-behind-the-goal` |
| Channel | eh |
| Video | [Stop giving AI tasks. Give it the goal behind the goal.](https://www.youtube.com/watch?v=Gj_GlrTxIWQ) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

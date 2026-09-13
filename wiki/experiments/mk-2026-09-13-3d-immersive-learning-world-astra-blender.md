# Use Astra + Blender Plugin to Auto-Generate Hosted 3D Interactive Learning Environments from a Topic Brief

> Back to [[experiments-index]]

Source: **[GPT-6 Astra Can Build 3D Worlds to Learn Anything](https://www.youtube.com/watch?v=27qpBfBhpDk)** · mk · 2026-09-13

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we give Astra a detailed planning prompt with a Blender plugin installed, a rubric for self-testing, and a hosting target, then it can autonomously generate, render, test, and deploy a fully interactive 3D learning world over an extended unattended run because the plugin provides a cheat-sheet of Blender affordances and the /goal directive keeps agents working until acceptance criteria are met.

## What they did

Mark installed the Blender plugin inside the Codex app (which auto-installs and configures Blender and gives Astra a skill cheat-sheet), then wrote a two-phase prompt: first a back-and-forth planning pass to define 12 learning stations, interactive cards, progressive disclosure layers, and a testing rubric; then an execution prompt using /goal to have Astra run unattended for ~18 hours generating 3D assets, testing in its internal browser against the rubric, and deploying to a live URL (here.now). He specified deliverables explicitly: source Blender masters, asset provenance log, reproducible build catalog, browser visual evidence, and a final hosted URL. He noted that with Astra's laziness fixes, he would now do planning on Medium, then execute on Soul or Luna at Extra High instead of using /goal.

## Relevance to YOLO loop

Demonstrates an extreme end of autonomous multi-hour agentic execution with self-testing and deployment — relevant to understanding how far unattended agent runs can go in our loop and what planning prompt structures + rubric-based acceptance criteria are needed to make long autonomous runs succeed without human checkpoints.

## Notes

Used ~8M tokens on Astra Medium for a single 18-hour run. Cost-prohibitive for routine use but worth one spike to understand autonomous run limits and rubric design patterns.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-09-13-3d-immersive-learning-world-astra-blender` |
| Channel | mk |
| Video | [GPT-6 Astra Can Build 3D Worlds to Learn Anything](https://www.youtube.com/watch?v=27qpBfBhpDk) |
| Published | 2026-09-13 |
| Ingested upstream | 2026-09-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

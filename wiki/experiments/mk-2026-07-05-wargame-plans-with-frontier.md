# Use frontier model to wargame agentic task plans before cheaper-model execution

> Back to [[experiments-index]]

Source: **[Do THIS Before You Lose Access to Fable 5](https://www.youtube.com/watch?v=nuwlyQXrADg)** · mk · 2026-07-05

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use a frontier model to generate action/reaction/counteraction wargame documents for each planned agentic task before handing off execution to a cheaper model, then cheaper models will execute more reliably and recover from errors more confidently, because the frontier model pre-simulates the unknown unknowns and failure branches that a linear plan omits.

## What they did

Mark described a workflow where, while still having Fable 5 access, you run it not to execute tasks but to wargame them: for each project, prompt the model to break down every course of action move-by-move, enumerate failure scenarios it might encounter based on prior experience, and document the required counteraction for each. The output is a structured war-games folder (tasks/, war-games/, success.md, ledger.md) containing comprehensive markdown files with assumed inputs, recon needed, alternate routes, and action/reaction/counteraction chains. A ledger.md tracks any undefined variables needing human input. These wargame files are then fed to cheaper models (Opus 4, GPT-5.5, open-source) as enriched context so they can execute the same projects more confidently. He demonstrated running a /goal slash-command to fan out parallel sub-agents that draft all wargames before polishing any, and a /loop command to iteratively push each draft to its limits.

## Relevance to YOLO loop

Directly upgrades the planning phase of the yolo loop. Instead of generating a linear plan file, the pre-execution step becomes a wargame: frontier model simulates failure paths, outputs a structured counteraction document, and cheaper execution agents receive richer context. The ledger.md pattern also maps cleanly to surfacing blockers before the loop starts.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-05 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-07-05-wargame-plans-with-frontier` |
| Channel | mk |
| Video | [Do THIS Before You Lose Access to Fable 5](https://www.youtube.com/watch?v=nuwlyQXrADg) |
| Published | 2026-07-05 |
| Ingested upstream | 2026-07-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

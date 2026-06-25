# Implement a five-point harness health check for every production agent

> Back to [[experiments-index]]

Source: **[Don't build more AI agents until you watch this](https://www.youtube.com/watch?v=BOXK2XFLA-E)** · nb · 2026-06-17

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we apply a structured five-point harness health check (sources, reach/permissions, job definition, proof trail, value delivery) on a recurring cadence, then agent drift and silent failures will be caught earlier because each dimension covers a distinct failure mode that emerges as either the model improves or the business context changes.

## What they did

Nate proposed five concrete checks for any serious agent: (1) What is it reading—are sources current? (2) What can it touch—are permissions still appropriately scoped for the current model capability? (3) Is the job definition still correct and intentional? (4) Does it return a linkable proof trail a human can inspect? (5) Does the output actually change work or save time, or has it become redundant? He argued agents break in two directions: world drift and model improvement, and this checklist guards against both.

## Relevance to YOLO loop

Maps to a post-deploy review gate in the YOLO loop. Could be templated as a markdown checklist committed alongside each agent's harness config and re-run after each model version bump.

## Notes

Nate explicitly notes that agents can break when models get *better*, not just worse—a counterintuitive maintenance failure mode worth testing against our own agents after model upgrades.

Backlog triage 2026-06-24 (owner-preference model). Five-point harness health check — matches verify_build + status + audit habit.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-17 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-06-17-harness-health-checklist` |
| Channel | nb |
| Video | [Don't build more AI agents until you watch this](https://www.youtube.com/watch?v=BOXK2XFLA-E) |
| Published | 2026-06-17 |
| Ingested upstream | 2026-06-17 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

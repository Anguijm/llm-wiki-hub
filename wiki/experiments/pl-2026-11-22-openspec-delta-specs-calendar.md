# Trial OpenSpec delta specs on the Flutter calendar app

> Back to [[experiments-index]]

Source: **[Spec-Kit vs. OpenSpec vs. your own framework - Which one is best for SDD?](https://www.youtube.com/watch?v=Ln64NESfgzg)** · pl · 2026-11-22

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run one real feature change in the Flutter family calendar app through OpenSpec (proposal, specs, design, tasks, with a custom decisions.md interview step) and archive it into master-specs via Delta Specs, then we get a lighter spec trail and fewer requirement drifts than ad-hoc prompts because each change is a small folder whose deltas merge into one living spec.

## What they did

Philipp compared GitHub Spec-Kit's verbose multi-file flow (constitution, specify, plan, research, data-model, contracts, checklists) with OpenSpec's lighter per-change folders (proposal.md, specs/, design.md, tasks.md). He customized config.yaml and a YAML schema to add a pre-spec interview artifact (decisions.md), tracked requirement changes as Delta Specs (added, modified, renamed, removed), and merged completed changes into master-specs/ on archive. He found Spec-Kit slowest to reach a final spec, and its extra verbosity did not improve code quality (tested a few months ago, so this may shift with newer models). He named OpenSpec his daily winner for greenfield and brownfield work.

## Relevance to YOLO loop

medium: Spec-first work is already practiced, but the Delta Spec archive that merges each change into a living master spec is a different mechanism for keeping specs current.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-27 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `pl-2026-11-22-openspec-delta-specs-calendar` |
| Channel | pl |
| Video | [Spec-Kit vs. OpenSpec vs. your own framework - Which one is best for SDD?](https://www.youtube.com/watch?v=Ln64NESfgzg) |
| Published | 2026-11-22 |
| Ingested upstream | 2026-11-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Build a Harness Inventory Skill to Map All Context Inputs

> Back to [[experiments-index]]

Source: **[Every Prompt You Send Drags 18,384 Words Of Junk. Here's How I Cut It.](https://www.youtube.com/watch?v=PDJfciNhyHU)** · nb · 2026-07-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we build a reusable skill that inventories every instruction file, memory, saved prompt, and permission in our AI setup into a single structured map, then we will identify redundant, conflicting, or stale controls that degrade model performance because accumulated rules added over time create hidden bloat that confuses newer models.

## What they did

Speaker discovered that one writing job was pulling in an 18,000-word context file before any prompt adjustment. He built a 'cleaner skill' that first maps the entire harness — every custom instruction, project file, saved prompt, memory, tool, and permission — into a table with columns for location, load timing, job, ownership, evidence of usefulness, and failure risk. The map revealed 66 reusable skills and 172 instruction-related files. He then ran cleaning passes to remove overlapping, outdated, or early-loading rules, and produced a plain-English before/after receipt of changes. He also tested compact vs. thick skill variants on Fable 5 and ChatGPT 5.6 to identify model-specific failure modes: Fable 5 over-delivered and broke delivery constraints under heavy context, while ChatGPT 5.6 failed earlier at routing due to harness size.

## Relevance to YOLO loop

Directly applicable to our dev loop: any accumulated system prompts, project files, memory entries, or injected context in our agent pipelines should be audited the same way. Running a harness inventory before adding new capabilities could prevent silent performance regressions when underlying models update.

## Notes

Speaker published the cleaner skill on Substack. Key insight: distinguish between soft instructions (text hints) and hard locks (permissions, schema validators, task refusals) — they load and behave differently and should be mapped separately.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-15-harness-audit-skill` |
| Channel | nb |
| Video | [Every Prompt You Send Drags 18,384 Words Of Junk. Here's How I Cut It.](https://www.youtube.com/watch?v=PDJfciNhyHU) |
| Published | 2026-07-15 |
| Ingested upstream | 2026-07-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

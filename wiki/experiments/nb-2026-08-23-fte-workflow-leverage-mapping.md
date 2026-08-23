# Map a Real Workflow to Find High-Leverage AI Insertion Points

> Back to [[experiments-index]]

Source: **[OpenAI Pays $280,000 For This Job. You Don't Have To Be An Engineer.](https://www.youtube.com/watch?v=0bLI31EFDDs)** · nb · 2026-08-23

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we pull actual process artifacts (e.g., completed vs. stalled tickets/claims/PRs) and map the step where delays concentrate before any model is chosen, then we will identify a narrowly scoped AI build that unblocks the largest downstream volume, because bottlenecks that are frequent, early in the process, and detectable from existing data yield the highest ROI per engineering month.

## What they did

Nate walked through a concrete insurance claims example where a PM (Maya) compared a fast-moving claim file against a slow one, identified that missing-document detection at intake caused 1,800+ stalled days per month, and scoped the AI task to only flag incomplete files and draft a customer message — leaving all judgment-heavy decisions (fraud, injury) to humans. He framed this as the core Forward Deployed Engineer skill: finding leverage (high-frequency, early-stage, measurable, low-authority) before writing any code. He then outlined a 30-day project structure: week 1 observe real work and map the process, week 2 build a minimal loop, week 3 harden it to production grade, week 4 put it in front of 2-3 real users and iterate.

## Relevance to YOLO loop

Directly maps to the scoping phase of our dev loop — before we add a new AI capability, we should do a Maya-style artifact audit of our own pipeline (e.g., review stalled issues, failed runs, repeated manual steps) to find the highest-leverage insertion point rather than building speculatively.

## Notes

The 30-day sprint structure (observe → minimal build → harden → user test) is a reusable template. Nate explicitly says people in his community have compressed this to 3-4 days. Worth trying on one internal workflow (e.g., PR review triage or incident postmortem drafting) as a concrete first run.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-08-23-fte-workflow-leverage-mapping` |
| Channel | nb |
| Video | [OpenAI Pays $280,000 For This Job. You Don't Have To Be An Engineer.](https://www.youtube.com/watch?v=0bLI31EFDDs) |
| Published | 2026-08-23 |
| Ingested upstream | 2026-08-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

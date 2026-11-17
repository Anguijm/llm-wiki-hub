# Run Bombadil property-based UI testing on the PDF to CSV page

> Back to [[experiments-index]]

Source: **[All Code Is Slop (Except Mine) — Lauren Tan, SpaceXSI](https://www.youtube.com/watch?v=O_zcc6Xl12g)** · aie · 2026-11-14

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we write a few invariants (for example, never a blank export, never an uncaught error, and the row count equals the parsed row count) and run Bombadil against the built PDF to CSV single-file page, then it will find UI state-sequence bugs that the existing fixed-input gates miss, because property-based testing explores random action sequences instead of replaying scripted paths.

## What they did

Lauren Tan's Grokbot team layers property-based UI testing with the open-source Bombadil on top of runtime verification (Chrome DevTools Protocol) and formal methods. This catches bugs that agents' own scripted checks miss and keeps the PR revert rate at about 0.5% despite thousands of PRs a month. The talk shows Bombadil in a slide or video and treats it as a verification artifact for the agent loop.

## Relevance to YOLO loop

high: property-based random-action UI testing is not among the existing gates, which are fixed checks, recompute scripts and reviewers, so it adds a new way to find bugs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-16 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-11-14-bombadil-property-ui-testing` |
| Channel | aie |
| Video | [All Code Is Slop (Except Mine) — Lauren Tan, SpaceXSI](https://www.youtube.com/watch?v=O_zcc6Xl12g) |
| Published | 2026-11-14 |
| Ingested upstream | 2026-11-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Structure CLAUDE.md as a thin index with progressive disclosure into skill files capped at 100 lines each

> Back to [[experiments-index]]

Source: **[Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](https://www.youtube.com/watch?v=aeTb5BdmTTc)** · aie · 2026-08-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we restructure our CLAUDE.md to be a thin pointer index rather than a monolithic instruction file, with individual skill files capped at ~100 lines each and runbook details embedded in code comments near relevant code, then initial context consumption drops significantly (target under 40K tokens at session start) because the agent uses progressive disclosure to fetch only what it needs.

## What they did

Aditya described a pattern for team-scale harness engineering: keep CLAUDE.md as a thin index that points to skill files, cap each skill file at ~100 lines, and embed runbook details as code comments adjacent to the relevant code so the agent can discover them by grep/read rather than upfront loading. He uses initial context consumption as the health metric — if a fresh session burns 40-50K tokens before doing any work, progressive disclosure is failing. He also described treating the shared harness as a shared codebase investment (not personal setup), with merge conflicts expected and managed like normal code.

## Relevance to YOLO loop

Directly actionable for our CLAUDE.md and skills directory structure — we can audit current context consumption at session start and refactor toward the thin-index pattern, measuring token burn as our success metric.

## Notes

Aditya also recommends treating experimental/prototype code as explicitly opted-out of production standards to avoid slop contaminating the main codebase — worth adding as a harness convention.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-11-harness-progressive-disclosure` |
| Channel | aie |
| Video | [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](https://www.youtube.com/watch?v=aeTb5BdmTTc) |
| Published | 2026-08-11 |
| Ingested upstream | 2026-08-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

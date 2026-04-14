# Build a skill-creator meta-agent that writes SKILL.md files from successful interactions

> Back to [[experiments-index]]

Source: **[How to Automate Anything with Claude (4-Step Framework)](https://www.youtube.com/watch?v=FSOvLgS4xvc)** · @ShawTalebi · 2026-04-05

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we have an agent whose only job is to observe successful build sessions and extract reusable skill documents (trigger, steps, output format, edge cases), then our methodology self-documents and new skills emerge automatically from practice.

## What they did

Shaw Talebi 4-step framework: (1) do task once with AI manually, (2) distill into a SKILL.md with trigger/steps/format/rules, (3) test in fresh session, (4) iterate and update skill on errors. Progressive disclosure: load skill names only, pull full SKILL.md on demand.

## Relevance to YOLO loop

Directly applicable to harness-cli recipes. Instead of manually writing recipe presets, a meta-agent could watch successful harness plan sessions and auto-generate new recipes. Also: the progressive disclosure pattern maps to how we could load council personas on-demand instead of all at once.

## Outcome

Built harness learn command (490 lines). Scans completed plans, extracts patterns (type, council weights, architecture, edge cases), generates reusable recipe .md files. --from-session mode for most recent plan. The methodology self-documents from practice.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-06 | `backlog` | Extracted from ShawTalebi 4-step automation framework video |
| 2026-04-06 | `done` | harness learn shipped |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `st-2026-04-05-skill-creator-meta-agent` |
| Channel | @ShawTalebi |
| Video | [How to Automate Anything with Claude (4-Step Framework)](https://www.youtube.com/watch?v=FSOvLgS4xvc) |
| Published | 2026-04-05 |
| Ingested upstream | 2026-04-06 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

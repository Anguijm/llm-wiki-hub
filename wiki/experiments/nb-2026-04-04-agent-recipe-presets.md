# Create pre-wired agent recipes instead of blank-canvas prompting

> Back to [[experiments-index]]

Source: **[Wall Street Just Bet $285 Billion on AI Agents. The Best One Barely Works.](https://www.youtube.com/watch?v=D-Ww1wLIp60)** · @NateBJones · 2026-04-04

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we create named recipe presets for common tasks ("new devtool", "flagship feature", "bug fix", "code review", "refactor") with pre-loaded context and tool configurations, then agent success rate increases because each recipe eliminates the prompt engineering step and provides the right context automatically.

## What they did

Successful agents use "punch card" recipes — pre-wired workflows like Code Review Recipe, Unit Test Generator, Boilerplate Setup. Users pick a recipe instead of writing prompts from scratch. Abstracts complexity while keeping output editable.

## Relevance to YOLO loop

Directly applicable to harness-cli. Instead of , offer , ,  with pre-loaded council configurations, context gathering, and plan templates per recipe type.

## Outcome

Added 5 recipe presets to harness-cli: devtool, bugfix, feature, refactor, api. Each pre-loads custom council angles and plan template. Usage: harness recipe devtool -d "description".

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-05 | `backlog` | Extracted from NateBJones Wall Street AI agents video |
| 2026-04-05 | `done` | 5 recipes shipped to harness-cli |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-04-04-agent-recipe-presets` |
| Channel | @NateBJones |
| Video | [Wall Street Just Bet $285 Billion on AI Agents. The Best One Barely Works.](https://www.youtube.com/watch?v=D-Ww1wLIp60) |
| Published | 2026-04-04 |
| Ingested upstream | 2026-04-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

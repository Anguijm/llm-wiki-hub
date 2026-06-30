# Structure agent harnesses as five explicit layers with tracked rot-rates

> Back to [[experiments-index]]

Source: **[Master All 5 Layers of Every Agentic OS](https://www.youtube.com/watch?v=YjkteijEyzQ)** · mk · 2026-06-30

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we decompose an agentic OS into five distinct layers (identity/soul, rules/hooks, skills, crystallized agents, tools/MCPs/CLIs) and assign a rot-rate (expected staleness cadence) to each layer, then maintenance will be more systematic and context-window poisoning from outdated instructions will be reduced because each layer has a clear owner, update trigger, and expiration signal.

## What they did

Mark presented a mental model treating an agentic OS like the layers of the Earth: a stable inner core (identity/soul file — CLAUDE.md or soul.md) pointing to rules and skills via short pointer sentences; a rules-and-hooks layer for deterministic guardrails; a skills layer for repeatable but non-deterministic workflows surfaced as slash commands; a crystallized-agents layer for tasks that have evolved beyond skills; and an outermost tools/MCPs/CLI layer. He introduced the concept of 'rot rate' — the pace at which each layer becomes obsolete — and showed a year-long timeline where each layer needs periodic refresh. He demonstrated this with a personal-health OS: soul file → extraction rules → Supabase data layer → Whoop API sync → food-photo and voice-note intake skills.

## Relevance to YOLO loop

Provides a principled scaffold for organising the YOLO loop's own agent harness. Mapping current CLAUDE.md, skills, hooks, and MCP configs to these five layers makes it easier to audit what is stale, what is missing, and what should be promoted from a skill to a crystallized sub-agent as the loop matures.

## Notes

Mark offers a free care-package prompt download and a paid community deep-dive (links in video description). The rot-rate concept is the most novel and immediately applicable element — worth creating a simple tracking doc that lists each harness layer with its last-updated date and expected review cadence.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-30 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-06-30-agentic-os-five-layers` |
| Channel | mk |
| Video | [Master All 5 Layers of Every Agentic OS](https://www.youtube.com/watch?v=YjkteijEyzQ) |
| Published | 2026-06-30 |
| Ingested upstream | 2026-06-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

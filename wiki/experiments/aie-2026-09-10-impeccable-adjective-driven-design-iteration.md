# Inject Design-System-Aware Context into Coding Harnesses to Steer Aesthetic Output via Natural Language Commands

> Back to [[experiments-index]]

Source: **[Design at the Speed of Adjectives — Paul Bakaus, Renaissance Geek, Inc.](https://www.youtube.com/watch?v=v42opQpCy60)** · aie · 2026-09-10

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we install a design-context layer (like Impeccable) into our coding harness that translates natural-language adjectives and verbs into grounded design operations, then iterative UI refinement will produce less generic 'AI slop' output compared to raw prompting, because adjectives without grounded definitions are underspecified and models default to training-data averages.

## What they did

Paul Bakaus described Impeccable, a design skill/plugin that works across coding harnesses (Claude Code, GitHub Copilot, Cursor, Codex, etc.) and translates design-intent commands ('make it bolder', 'overdrive') into context-rich design operations informed by an underlying design system. He showed a before/after comparison where the same prompt with and without Impeccable produced noticeably different results on GPT-4.5. Key insights: (1) You cannot one-shot design—multi-shot iteration with human steering is required; (2) Fully agentic design without human checkpoints produces 'Claude beige' (instrument serif, italics, algorithmic monoculture); (3) The right level of control is above pixel-level manipulation (margins/padding) but below full autonomy—adjective-level commands at the section/component level; (4) Taste cannot be auto-generated; tools should amplify existing taste, not replace it; (5) He explicitly will not add an 'auto' mode that removes human steering from the loop.

## Relevance to YOLO loop

Relevant to any UI generation step in our loop: adding a design-constraint vocabulary to our system prompts (even without Impeccable) should reduce generic outputs. The workflow-mapping approach—identifying injection points along the design process rather than one-shotting—is directly applicable to how we structure multi-step agent tasks.

## Notes

Impeccable is open source. Try installing in Cursor/Claude Code and benchmark against raw prompting on a UI generation task. Key finding: adjectives need explicit definitions in context to be effective—vague adjectives alone don't help.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-10-impeccable-adjective-driven-design-iteration` |
| Channel | aie |
| Video | [Design at the Speed of Adjectives — Paul Bakaus, Renaissance Geek, Inc.](https://www.youtube.com/watch?v=v42opQpCy60) |
| Published | 2026-09-10 |
| Ingested upstream | 2026-09-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

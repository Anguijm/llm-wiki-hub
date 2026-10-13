# Package UX opinions as agent skills so every new feature inherits consistent polish

> Back to [[experiments-index]]

Source: **[Please… Enough with the Sloppy, One-Shot SaaS Replacements — Mahmoud Abdelwahab, Railway](https://www.youtube.com/watch?v=oixzVKMAXG0)** · aie · 2026-10-13

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we encode UI/UX opinions (autosave, optimistic updates, infinite scroll, animation standards) as named agent skills and reference them in every feature request, then agent-built features will be consistent and production-quality without repeated re-specification, because Railway found that without explicit skill references agents omit these patterns entirely.

## What they did

Mahmoud Abdelwahab built an all-in-one internal marketing tool at Railway using agents (GPT-6 era, October 2026). He found agents consistently skip autosave, optimistic updates, pagination/infinite scroll, and animation polish unless explicitly told. He packaged these as agent skills (design engineering skill for UI/typography/error messages, animation skill, Railway deployment skill) and referenced them in every build prompt. He also found that telling the agent to use an existing page as a reference for new features dramatically improved consistency. Final step: always include an end-to-end verification loop via computer use.

## Relevance to YOLO loop

We can immediately encode our own 'what good looks like' opinions into a skills file and reference it in our dev-loop prompts, reducing the gap between agent output and shippable code.

## Notes

Key patterns agents forget by default: autosave + unsafe-change browser guard, optimistic updates, infinite scroll / end-of-list signal. Verification loop (computer use, end-to-end) is described as a night-and-day improvement.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-13-polished-internal-tools-agent-skills` |
| Channel | aie |
| Video | [Please… Enough with the Sloppy, One-Shot SaaS Replacements — Mahmoud Abdelwahab, Railway](https://www.youtube.com/watch?v=oixzVKMAXG0) |
| Published | 2026-10-13 |
| Ingested upstream | 2026-10-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Create a design.md as an agent-readable design system

> Back to [[experiments-index]]

Source: **[A Markdown File Just Replaced Your Most Expensive Design Meeting (Google Stitch)](https://www.youtube.com/watch?v=CDClFY-R0dI)** · nb · 2026-03-28

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we capture our UI design conventions in a structured markdown file (design.md), then AI agents will produce more visually consistent projects because they can reference explicit design tokens, color palettes, and layout patterns instead of improvising.

## What they did

Google Stitch introduced Design.md — a markdown file that captures design systems so AI agents can read, understand, and build against consistent design patterns. This replaces the need for Figma handoffs.

## Actionable steps

- Audit the best-looking YOLO projects for common design patterns
- Create a design.md with color palette, typography, spacing, component patterns
- Reference design.md in program.md so the builder agent uses it
- Compare visual consistency of next 5 builds vs previous 5

## Success metric

Next 5 projects share a recognizable visual identity without manual CSS tweaking.

## Relevance to YOLO loop

Every YOLO project reinvents its CSS from scratch. A shared design.md would compound visual quality across all builds.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

Created design.md with full color palette, typography scale, component patterns, spacing rules, and layout rules extracted from 6 best projects. Added to program.md as a required read before building.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-03-29 | `in_progress` | Starting implementation |
| 2026-03-29 | `done` | design.md created, referenced in program.md |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-03-28-design-md-agent-readable` |
| Channel | nb |
| Video | [A Markdown File Just Replaced Your Most Expensive Design Meeting (Google Stitch)](https://www.youtube.com/watch?v=CDClFY-R0dI) |
| Published | 2026-03-28 |
| Ingested upstream | 2026-03-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Use a living intent graph as single source of truth with human-in-the-loop approval for agent modifications

> Back to [[experiments-index]]

Source: **[What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](https://www.youtube.com/watch?v=0I6aoPSRzVc)** · aie · 2026-08-22

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we maintain a continuously-updated 'system of intent' graph (constraints, decisions, best practices) that agents can read but only modify with human approval, and layer domain-specific agents on top, then alignment overhead drops and agents stop overstepping domain boundaries because the substrate defines what is possible, not per-agent instructions.

## What they did

AIDAChip built a three-layer system for chip design teams: (1) a living intent graph (the 'Bible') with human-in-the-loop approval for changes, (2) a tribal knowledge layer that evolves across projects, and (3) domain-specific agents (digital design, analog design, etc.) scoped by file isolation. They hit three failure modes: agents overstepping domains, truth drift when changes weren't propagated everywhere, and agents using bash/cat to bypass write restrictions. Fixes: spec hierarchy with file isolation, rule-based conflict detection, and system-level blocking rather than tool-by-tool blocking. Reported 4x leverage in early alpha.

## Relevance to YOLO loop

Maps directly to our CLAUDE.md + skills architecture: treat CLAUDE.md as the intent graph, require explicit human approval before agents modify it, enforce domain scoping per skill/agent, and add a conflict detection step that checks whether a change to one file should propagate elsewhere.

## Notes

Currently in alpha with development partners; beta sign-ups open, expected October 2026 release. Key lesson: the substrate (what agents can and cannot do) matters more than agent intelligence. Block at system level, not tool by tool.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-22-chip-design-shared-nervous-system` |
| Channel | aie |
| Video | [What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](https://www.youtube.com/watch?v=0I6aoPSRzVc) |
| Published | 2026-08-22 |
| Ingested upstream | 2026-08-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

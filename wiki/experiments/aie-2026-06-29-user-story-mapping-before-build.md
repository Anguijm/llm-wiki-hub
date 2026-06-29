# Require a user story map before any agent-assisted feature build to reduce wrong-thing velocity

> Back to [[experiments-index]]

Source: **[You Can't Prompt the Room: The Last Skill AI Won't Replace - Balázs Horváth, VisualLabs](https://www.youtube.com/watch?v=6bmM45jkMDY)** · aie · 2026-06-29

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we mandate a user story mapping session (backbone activities + user stories with persona/what/why/acceptance criteria) before handing a feature spec to a coding agent, then the ratio of shipped features that get reused more than twice will increase and wasted build cycles will decrease, because AI pattern-matches well to well-structured user stories and the mapping process surfaces whether there is genuine business value before any tokens are spent on implementation.

## What they did

Balázs Horváth (VisualLabs) described how his team ran an internal hackathon with 21 agent ideas and abandoned 17 (81%) for lacking real business value — a ratio he attributed to building without upfront requirement elicitation. He prescribes user story mapping (backbone → user stories → MVP slice → backlog) as the pre-build artifact, feeding well-formed stories (persona + what + why + acceptance criteria) directly to AI for implementation. He flagged anti-patterns: high feature velocity with low adoption, demos that never go to production, and PRDs with no real user testing. He recommends shifting measurement from 'features shipped' to 'features used more than twice'.

## Relevance to YOLO loop

Our loop currently optimizes for build speed; this experiment adds a lightweight gate before the coding phase. A one-page story map fed as structured context to our planning agent could dramatically reduce throwaway work and improve the quality of the spec the coding agent receives.

## Notes

Practical Monday actions: audit current KPIs to remove 'features shipped' and add 'features used 2+ times'; run a story map before the next new feature build; compare coding agent output quality with vs without structured user stories as input context.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-29-user-story-mapping-before-build` |
| Channel | aie |
| Video | [You Can't Prompt the Room: The Last Skill AI Won't Replace - Balázs Horváth, VisualLabs](https://www.youtube.com/watch?v=6bmM45jkMDY) |
| Published | 2026-06-29 |
| Ingested upstream | 2026-06-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

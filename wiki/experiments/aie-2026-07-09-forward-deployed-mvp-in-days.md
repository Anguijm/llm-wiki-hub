# Embed directly with end users for 2-3 days per week and build MVPs on-site in days rather than sprints

> Back to [[experiments-index]]

Source: **[Shipping Production AI Inside Government — William Tarr, Ministry of Justice (DO NOT PUBLISH)](https://www.youtube.com/watch?v=qlHaO6laBlM)** · aie · 2026-07-09

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If developers spend the majority of their time physically co-located with end users watching actual workflows, then the MVPs they ship will have higher adoption and require fewer revision cycles, because the gap between assumed and actual pain points closes before a single line of code is written.

## What they did

William Tarr and Louis Hogarth described the Ministry of Justice Justice AI unit's forward-deployed model: a team of ~40 (effectively replacing ~300 traditional headcount) that embeds in prisons, probation offices, and courts 2-3 days per week. They build MVPs in days, feature-flag experiments, kill code that doesn't work at scale, and use video-first communication instead of emails to close the literacy gap with non-technical staff. National rollout was achieved in months rather than years. They explicitly avoid roadmaps and instead ship to the problem observed that day.

## Relevance to YOLO loop

Maps to the requirements and feedback phases of the yolo loop: the loop's input quality (the prompt/spec) is only as good as the fidelity of the problem understanding. On-site embedding is the extreme version of closing the feedback loop between real user behavior and agent task definition.

## Notes

Applicable pattern for any internal tooling we build: spend time with the actual users of the tool before specifying agent tasks. The video-first communication pattern (short screen recordings instead of docs) is also worth adopting for async handoffs between agent output and human review.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-09-forward-deployed-mvp-in-days` |
| Channel | aie |
| Video | [Shipping Production AI Inside Government — William Tarr, Ministry of Justice (DO NOT PUBLISH)](https://www.youtube.com/watch?v=qlHaO6laBlM) |
| Published | 2026-07-09 |
| Ingested upstream | 2026-07-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

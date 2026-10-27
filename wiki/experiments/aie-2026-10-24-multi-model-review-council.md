# Run a multi-model code review council and compare bug overlap

> Back to [[experiments-index]]

Source: **[AI Writes the Code. So What's Left for Engineers? - Laurie Voss, Arize AI](https://www.youtube.com/watch?v=kspZP5BgkEU)** · aie · 2026-10-24

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run several different models as reviewers on the same agent-written diff and merge their findings, then we catch more distinct bugs than any single reviewer because different reviewers find non-overlapping bugs.

## What they did

Laurie Voss presented data that developers using coding agents write 741% more code but ship only 30% faster because review is the bottleneck. Human review accuracy falls off beyond about 450 lines per hour. Four commercial AI code reviewers each found bugs but agreed on none. Claude passes 87% of unit tests, but maintainer merge willingness is only 54% on the Cognition benchmark. Cursor's Bugbot has compiled over 44,000 rules from negative user feedback. His recommendations: restrict human review to high-blast-radius boundaries and credential paths, encode maintainer judgment as rubrics, and use online evaluators.

## Relevance to YOLO loop

high: Supports adding a multi-reviewer council and merge-willingness rubric to the YOLO loop's verification step.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-26 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-24-multi-model-review-council` |
| Channel | aie |
| Video | [AI Writes the Code. So What's Left for Engineers? - Laurie Voss, Arize AI](https://www.youtube.com/watch?v=kspZP5BgkEU) |
| Published | 2026-10-24 |
| Ingested upstream | 2026-10-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Replace Line-by-Line PR Review with a Codified Automated Review Harness

> Back to [[experiments-index]]

Source: **[The Death of the Code Review: What the Data Actually Says — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=_mi3alkqy4s)** · aie · 2026-10-02

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we stop reviewing agent-generated PRs line-by-line and instead invest that time in building a rubric-based automated review harness with codified definitions of good, then we will ship more software per engineer without increasing defect rate, because human review effectiveness collapses above 400 lines per sitting while a well-designed harness scales linearly.

## What they did

Laurie Voss cited a study of 100,000+ GitHub developers showing agents produced 741% more code but only 30% more shipped software, with review as the confirmed bottleneck. He cited a Cisco study showing human reviewers stop finding defects effectively above 400 lines per sitting and completely fail above 450 lines/hour — meaning a 10,000-line agent PR would take 3-4 days to review properly. He referenced OpenAI's internal experiment building a ~1M line codebase with 3 engineers and near-zero manual review. He also cited a March 2026 study showing vulnerable code with innocent commit messages fooled automated review agents 88% of the time vs 35% for humans. His prescription: stop reviewing PRs at the line level; instead codify company context, domain knowledge, and definitions of good into a review harness, then use production observability as the final reviewer.

## Relevance to YOLO loop

Directly addresses our YOLO loop's merge bottleneck. If agents are generating large diffs, we need a harness that can evaluate correctness at a higher abstraction level than line review. This also highlights the prompt injection risk of automated reviewers that we should test.

## Notes

Critical caveat from the talk: automated reviewers are fooled by confidently-framed bad code 88% of the time, and agents produce exactly that kind of code. The harness design must account for adversarial agent output. Production observability becomes the last line of defense.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-02-automated-review-harness-over-pr-review` |
| Channel | aie |
| Video | [The Death of the Code Review: What the Data Actually Says — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=_mi3alkqy4s) |
| Published | 2026-10-02 |
| Ingested upstream | 2026-10-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# A/B Test Compact vs. Thick Skill Variants to Find Delivery Failure Thresholds

> Back to [[experiments-index]]

Source: **[Every Prompt You Send Drags 18,384 Words Of Junk. Here's How I Cut It.](https://www.youtube.com/watch?v=PDJfciNhyHU)** · nb · 2026-07-15

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we test a compact skill variant (goal + facts + permission boundary + finish line only) against a thick variant (plus method, scoring system, eval plan, classification scheme) on the same task, then the compact variant will have higher delivery reliability because models like Fable 5 fail at constraint adherence when context is heavy, while still completing the core task.

## What they did

Speaker ran the same underlying job through Fable 5 in two configurations. The compact setup provided only goal, facts, permission boundary, and finish line. The thick setup added full method, a scoring system, an eval plan, and a classification scheme. The thick version produced richer analysis but failed delivery requirements twice — once breaking JSON format, once breaking the word limit. The compact setup completed correctly all three times. He also tested ChatGPT 5.6 in Codex and found its failure mode was earlier in the process: it struggled to route correctly across a large harness before even attempting the method.

## Relevance to YOLO loop

When building agent tasks in our loop, we should run both a minimal and a full-context version of each skill to establish where delivery constraints break. This gives us a principled basis for deciding how much context to load per task type rather than guessing.

## Notes

Model-specific failure modes matter: Fable 5 fails late (over-delivers, breaks output format); ChatGPT 5.6 in Codex fails early (routing confusion). Selective loading and hard output checks benefit both but for different reasons.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-15-compact-vs-thick-skill-test` |
| Channel | nb |
| Video | [Every Prompt You Send Drags 18,384 Words Of Junk. Here's How I Cut It.](https://www.youtube.com/watch?v=PDJfciNhyHU) |
| Published | 2026-07-15 |
| Ingested upstream | 2026-07-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

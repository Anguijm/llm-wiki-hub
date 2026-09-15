# Implement Embedded Third-Party Evaluators for AI Safety Auditing

> Back to [[experiments-index]]

Source: **[AI News in 10 mins: 10% chance AI kills all humans](https://www.youtube.com/watch?v=68HH9HVFJDM)** · nh · 2026-09-13

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we grant ongoing employee-like access to third-party evaluators embedded within an AI development process, then safety adherence and alignment commitments can be verified continuously rather than post-hoc, because external auditors with deep access can catch races to the bottom before they compound.

## What they did

Nate summarized Dario Amodei's essay proposing a three-step plan to pace AI frontier development safely. The first step — embedded evaluators — calls for each frontier AI company to give ongoing, employee-like access to third-party evaluators whose role is to verify adherence to safety practices. Nate highlighted this alongside the Jacob Coxon resignation controversy and Evan Hubinger's >10% extinction risk estimate to frame why third-party oversight mechanisms matter.

## Relevance to YOLO loop

In our dev loop, we deploy agents with limited external oversight. Adding a structured third-party or automated evaluator role that has continuous read access to agent logs, tool calls, and outputs mirrors this embedded-evaluator concept at a smaller scale — a lightweight safety harness around the loop.

## Notes

Primarily a news/commentary video, but Dario's embedded-evaluator proposal is actionable at team scale. The political amplification angle (Bernie Sanders, J.B. Pritzker boosting Jacob's tweet) is context only.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-13-ai-risk-10pct` |
| Channel | nh |
| Video | [AI News in 10 mins: 10% chance AI kills all humans](https://www.youtube.com/watch?v=68HH9HVFJDM) |
| Published | 2026-09-13 |
| Ingested upstream | 2026-09-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

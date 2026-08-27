# Build a tiered auto-approval layer that learns from repeated agent action patterns

> Back to [[experiments-index]]

Source: **[Cursor Accidentally Exposed Grok Bot's Blueprint](https://www.youtube.com/watch?v=mAWT1HCBgbQ)** · mk · 2026-08-27

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we implement a tiered approval system that auto-allows actions the agent has successfully performed before (e.g., file edits, test runs) but requires explicit confirmation for novel or high-risk actions (e.g., publishing, external API calls), then we will reduce human interrupt frequency without increasing error rate, because Grokbot's architecture shows that repeated safe actions can be whitelisted while consequential actions maintain human oversight.

## What they did

Speaker described Grokbot's tiered approval mechanism: actions performed successfully multiple times get auto-allowed, but publishing/deployment steps trigger double and triple confirmation checks. The system learns which action categories are safe to auto-approve based on repetition history, reducing friction for routine actions while preserving gates on consequential ones.

## Relevance to YOLO loop

Directly reduces human overhead in our loop. We can implement a simple approval log that tracks action type + success/failure, and after N successes auto-approves that action class. This operationalizes the 'level up above the loop' pattern described in the NateBJones video.

## Notes

Complements the mailbox architecture experiment. Can be implemented independently as a wrapper around existing tool calls.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-08-27-grokbot-auto-approval-tiering` |
| Channel | mk |
| Video | [Cursor Accidentally Exposed Grok Bot's Blueprint](https://www.youtube.com/watch?v=mAWT1HCBgbQ) |
| Published | 2026-08-27 |
| Ingested upstream | 2026-08-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

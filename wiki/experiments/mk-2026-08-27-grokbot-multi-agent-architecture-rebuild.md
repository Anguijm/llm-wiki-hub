# Implement per-agent mailbox messaging with priority interrupts in a custom multi-agent harness

> Back to [[experiments-index]]

Source: **[Cursor Accidentally Exposed Grok Bot's Blueprint](https://www.youtube.com/watch?v=mAWT1HCBgbQ)** · mk · 2026-08-27

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we give each agent in our multi-agent system its own isolated message queue with priority-flagged DMs and a round-table meeting primitive, then agents will be able to coordinate asynchronously without blocking each other, because Grokbot's leaked architecture shows agents can continue working while receiving non-urgent messages and only interrupt for priority signals, enabling true parallel execution.

## What they did

Speaker reverse-engineered Grokbot's leaked architecture (reconstructed from Cursor-exposed code) and identified six core components: per-agent identity with private state, send_to_agent DM tool for async messaging, priority interrupt mechanism that cancels background jobs for urgent messages, round-table meeting primitive with a manager agent conducting structured turns, per-agent sandboxed browser/screen, and a tiered auto-approval system that learns which actions to allow automatically. He then rebuilt a working clone using Codex + OpenRouter + local models.

## Relevance to YOLO loop

Highly relevant to scaling our YOLO loop beyond single-agent. Implementing the mailbox + priority interrupt pattern would let us run researcher, builder, and reviewer agents in parallel rather than sequentially, with structured handoffs replacing ad-hoc context passing.

## Notes

Auto-approval tiering is the most immediately actionable piece — start by classifying current agent actions into always-allow, ask-once, and always-confirm buckets.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-08-27-grokbot-multi-agent-architecture-rebuild` |
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

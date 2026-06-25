# Redesign agent session storage as an append-only event log to enable resumable, portable agents

> Back to [[experiments-index]]

Source: **[The Log Is The Agent - Ishaan Sehgal, Omnara](https://www.youtube.com/watch?v=UPwGaM2MKHY)** · aie · 2026-06-25

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we treat the agent's append-only event log (every user input, model output, tool call, and tool result) as the primary durable artifact rather than a running process, then agents become resumable after any worker or infrastructure failure and portable across model providers because any worker can reconstruct state by reading the log and any projection (context window, UI, debug trace, compaction) is derived from it.

## What they did

Ishaan argued that current agent frameworks mis-identify the agent as the model or runtime. He proposed the log-as-agent abstraction: a stateless worker claims a session, reads the log, advances the agent one step, writes the result, and exits. A different worker can continue from any point. He addressed the compaction objection (treat compacted summaries as lossy forks, never discard the raw log) and the external-state objection (log captures the agent's view of the world, not the whole world). He warned that managed-agent providers who host the log effectively own the agent and announced Omnara's open-source managed-agent platform built around user-owned session logs.

## Relevance to YOLO loop

Directly applicable to how we persist Claude Code sessions: switching from ephemeral context to an explicit append-only session log would let us resume long-running tasks after crashes, fork sessions for A/B testing, and audit every decision the agent made.

## Notes

Omnara open-source managed-agent platform launching at omnara.com/managed. Log ownership framing has significant implications for which provider we use long-term.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-25 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-25-log-as-agent-identity` |
| Channel | aie |
| Video | [The Log Is The Agent - Ishaan Sehgal, Omnara](https://www.youtube.com/watch?v=UPwGaM2MKHY) |
| Published | 2026-06-25 |
| Ingested upstream | 2026-06-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

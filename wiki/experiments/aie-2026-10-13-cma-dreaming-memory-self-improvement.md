# Run a 'dreaming' pass over recent session transcripts to update memory stores and improve skill instructions

> Back to [[experiments-index]]

Source: **[Scheduled Agents, Dreaming and Q&A: Claude Managed Agents (Part 3 of 4) — Anthropic](https://www.youtube.com/watch?v=qJtcEDc_WJU)** · aie · 2026-10-13

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we periodically spin up a meta-agent that analyzes transcripts from recent sessions against the current memory store and updates the store with learnings and skill gaps it discovers, then agents will improve over time without manual prompt editing, because Anthropic's dreaming feature found skill gaps in existing instructions by analyzing 30 days of session transcripts.

## What they did

Gabe demoed Claude Managed Agents' 'dreaming' feature: select a memory store and a time window (e.g., last 30 days), start streaming analysis, and a session with many sub-agents spins up to analyze transcripts from all sessions that used that memory store. It checks whether the memory store encoded necessary information, identifies recurring issues, and updates the store with new learnings (e.g., extending an existing skill with edge cases discovered in production). The roadmap extends this to skill prompts, agent prompts, and sub-agent prompts for continuous automated improvement.

## Relevance to YOLO loop

We manually review and update our MEMORY.md. Automating a weekly dreaming pass over recent session traces would surface patterns we miss and keep instructions current without manual effort.

## Notes

Currently dreaming only updates memory stores; roadmap includes skills, agent prompts, sub-agent prompts. The dreaming session itself uses Claude Managed Agents internally—recursive self-improvement via the same infrastructure.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-13-cma-dreaming-memory-self-improvement` |
| Channel | aie |
| Video | [Scheduled Agents, Dreaming and Q&A: Claude Managed Agents (Part 3 of 4) — Anthropic](https://www.youtube.com/watch?v=qJtcEDc_WJU) |
| Published | 2026-10-13 |
| Ingested upstream | 2026-10-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Build an Always-On Cloud Harness with Slack Integration

> Back to [[experiments-index]]

Source: **[Every Harness Will Become A Claw — Sam Bhagwat, Mastra](https://www.youtube.com/watch?v=8qWIPUia2O8)** · aie · 2026-07-21

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we move our local coding harness to an always-on cloud harness accessible via Slack, then team members can collaboratively steer long-running agents without being blocked by turn-based interaction, because cloud harnesses support parallel sub-agents, interrupt/resume, and multi-user instruction parsing.

## What they did

Sam Bhagwat described the evolution from local harnesses (Claude Code, Codex) to cloud harnesses that are always on, accessible via Slack, support parallel sub-agents, durable session persistence, session-long tool approval, and the ability for multiple users to give instructions simultaneously. He framed this as the transition from harness to 'claw' — a more persistent, autonomous, always-available agent infrastructure.

## Relevance to YOLO loop

Directly maps to the orchestration and execution layer of the YOLO loop — making agents durable, resumable, and collaboratively steerable rather than single-session local tools.

## Notes

Sam also predicts a 'shakeout' similar to mobile apps — only high-frequency or high-value agent claws will survive. Worth considering which claws in our stack meet that bar.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-21 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-21-harness-to-claw-agentic-spectrum` |
| Channel | aie |
| Video | [Every Harness Will Become A Claw — Sam Bhagwat, Mastra](https://www.youtube.com/watch?v=8qWIPUia2O8) |
| Published | 2026-07-21 |
| Ingested upstream | 2026-07-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

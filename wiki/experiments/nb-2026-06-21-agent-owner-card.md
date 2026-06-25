# Create an Agent Owner Card for Every Production Agent

> Back to [[experiments-index]]

Source: **[Most Teams Skip This Critical AI Agent Skill in 2026](https://www.youtube.com/watch?v=rh_PcL26zls)** · nb · 2026-06-21

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we maintain a structured owner card (name, owner, job, sources, permissions, failure modes) for each agent in our system, then agent reliability and accountability will improve because unowned agents accumulate stale context, bad patterns, and unchecked outputs that compound silently over time.

## What they did

Nate argued that the critical missing skill for teams in 2026 is agent ownership, not agent building. He described a lightweight 'owner card' artifact with fields: agent name, owner, job description (one sentence), diet (what sources/context it reads), boundaries (what it can read vs. write vs. send), and the failure mode to watch for. He suggested teams maintain these as a shared registry (e.g., a Slack channel of cards) so humans can audit what agents are doing across the org. He framed this as analogous to Google's ATA protocol introduction cards but for humans, not agents.

## Relevance to YOLO loop

Directly applicable to our dev loop: any agent we run in the YOLO loop (code inspection, PR review, backlog prep) should have an owner card. This gives us a lightweight governance layer before we scale to multiple agents and prevents silent drift in agent behavior.

## Notes

Backlog triage 2026-06-24 (owner-preference model). Owner card per agent (job/sources/permissions/failure-modes) — accountability; harness-health match.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-21 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-06-21-agent-owner-card` |
| Channel | nb |
| Video | [Most Teams Skip This Critical AI Agent Skill in 2026](https://www.youtube.com/watch?v=rh_PcL26zls) |
| Published | 2026-06-21 |
| Ingested upstream | 2026-06-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

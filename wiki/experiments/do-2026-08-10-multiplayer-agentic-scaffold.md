# Replace ad-hoc file sharing between agents with a multiplayer shared-artifact scaffold

> Back to [[experiments-index]]

Source: **[Ex-Uber dev explains his Multi-Agent Workflow](https://www.youtube.com/watch?v=utb7zYbK10c)** · do · 2026-08-10

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we replace the current pattern of agents passing MD/HTML files over Slack or git repos with a purpose-built shared-artifact layer (analogous to Google Docs vs emailed documents), then agent collaboration latency and merge conflicts will decrease and the loop will produce more coherent outputs, because a shared mutable artifact eliminates the round-trip serialization and deserialization cost of file handoffs.

## What they did

Flo (ex-Uber, Lindy.ai) argued that all current agent tooling was built for single-player humans and is being hacked for multi-agent use via file drops in Slack and GitHub repos. He compared this to emailing Word documents vs collaborating in Google Docs, and said the 2025-2026 transition is from isolated per-developer agents to true multiplayer agentic scaffolds where multiple agents (and humans) collaborate on the same underlying artifact simultaneously. He cited Lindy.ai as an early example of this multiplayer scaffold approach.

## Relevance to YOLO loop

Our loop currently hands context between agents via files committed to git or dropped in shared directories — exactly the anti-pattern described. Experimenting with a shared in-memory or database-backed artifact store as the canonical state that all agents read/write would directly address the coordination overhead we observe between planning, coding, and review agents.

## Notes

Flo's framing: agents are a new kind of teammate with different strengths/weaknesses from humans, so software designed for humans is suboptimal for agents. Worth surveying what shared-artifact primitives (CRDT stores, operational-transform layers, versioned KV) are available before building from scratch.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-08-10-multiplayer-agentic-scaffold` |
| Channel | do |
| Video | [Ex-Uber dev explains his Multi-Agent Workflow](https://www.youtube.com/watch?v=utb7zYbK10c) |
| Published | 2026-08-10 |
| Ingested upstream | 2026-08-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

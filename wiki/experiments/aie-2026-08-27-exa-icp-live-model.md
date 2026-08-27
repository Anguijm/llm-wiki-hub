# Build a live internal knowledge model that agents can query for context-aware task execution

> Back to [[experiments-index]]

Source: **[Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](https://www.youtube.com/watch?v=6pbQgnJ9Voc)** · aie · 2026-08-27

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we maintain a continuously updated internal knowledge base combining first-party product/usage data with external signals, then agents acting on this substrate will produce more contextually accurate outputs than agents relying on static prompts or stale CRM snapshots, because Exa's ICP dashboard approach shows that a live model of the world enables agents to act on current reality rather than yesterday's data.

## What they did

Speaker (Exa co-founder) described treating GTM as an AI engineering problem by building a live internal model of the world that agents can act on. Components included: an ICP dashboard answering questions about target customers using real-time internal + external data, a 'Jeffbot' personal assistant with full data access for the founder and read-only draft access for team members, and agent-accessible interfaces over their knowledge base. He also described a forward-deployed engineering team that both runs deals and builds the sales systems.

## Relevance to YOLO loop

Relevant to grounding our agents in current project state. A lightweight version — a structured JSON or markdown file updated per-session with current repo state, open issues, and recent decisions — would give our agents the 'live model' foundation without full infrastructure investment.

## Notes

Security tiering insight: Jeffbot has full read/write for founder, read-only draft access for team. Apply same principle to agent permission scoping in our loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-27-exa-icp-live-model` |
| Channel | aie |
| Video | [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](https://www.youtube.com/watch?v=6pbQgnJ9Voc) |
| Published | 2026-08-27 |
| Ingested upstream | 2026-08-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

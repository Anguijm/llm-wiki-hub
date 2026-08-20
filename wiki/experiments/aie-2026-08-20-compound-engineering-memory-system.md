# Build a compounding memory system that extracts and stores learnings from every agent interaction

> Back to [[experiments-index]]

Source: **[The Era of Compound Engineering — Kieran Klaassen, Every/Cora](https://www.youtube.com/watch?v=_ehJyfHg1Vk)** · aie · 2026-08-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we implement a system that automatically extracts and persists judgment, decisions, and taste from every agent interaction (rather than relying on per-session context), then the AI system will compound in capability over time and a single engineer can outperform teams that use AI without compounding memory.

## What they did

Kieran Klaassen (CTO/founder, Cora — an AI-native email client, solo engineer) described 'compound engineering': a loop of brainstorm → plan → work → review → polish → compound → repeat. The key insight is that the human's role is concentrated at the 'bread' ends of the sandwich (brainstorming/deciding what to build, and taste/quality judgment at review), while the AI handles the middle. The compounding step is the critical differentiator: whenever he caught himself repeating context to the agent, he extracted that knowledge into a persistent memory system (started with CLAUDE.md, built a custom memory system when it got too large). His plugin/open source tool implements this. Rules: (1) spend 50% of time making the system better for next time; (2) document the reasoning/thinking, not the code; (3) the middle (plan/work/review) should run without human involvement — if you're still needed in the loop, fix the middle; (4) the next feature should be easier to build than the previous one, not harder.

## Relevance to YOLO loop

Core to our dev loop evolution. Implementing a structured 'compound' step after every agent session — where we extract learnings into AGENTS.md or a memory system — directly addresses the problem of repeating context and losing cross-session coherence. The 50% time rule for improving the system is a concrete operating principle.

## Notes

Kieran ships 2+ PRs/week as a solo engineer with support, built a full email client (Cora) since January with React frontend and Rails backend. Open source plugin available — check description. Key metric for knowing the system works: 'If you run something and it runs for three hours and it's always good, you know you're there.' Postmortem pattern: when something breaks, extract the decision that caused it as a learning to change future agent behavior. Stack: Ruby/Rails backend, React frontend, Claude-based agents.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-20-compound-engineering-memory-system` |
| Channel | aie |
| Video | [The Era of Compound Engineering — Kieran Klaassen, Every/Cora](https://www.youtube.com/watch?v=_ehJyfHg1Vk) |
| Published | 2026-08-20 |
| Ingested upstream | 2026-08-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

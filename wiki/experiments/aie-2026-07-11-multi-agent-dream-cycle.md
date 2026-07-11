# Add a nightly dream-cycle agent that consolidates memory, resolves contradictions, and surfaces a morning report

> Back to [[experiments-index]]

Source: **[The Factory That Dreams: 39 AI Agents, No Framework - Rushabh Doshi, Machinecraft](https://www.youtube.com/watch?v=jtzh-GBXBWc)** · aie · 2026-07-11

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we run a scheduled nightly agent that replays the day's interactions, locks in useful facts, detects contradictions, forgets stale data, and converts episodes into reusable skills, then the agent system improves autonomously over time because compaction and consolidation happen offline without blocking daytime workflows.

## What they did

Rushabh described 'Eira', a 36-agent go-to-market system for his manufacturing company built without any ML training. The system uses a biology-inspired memory architecture: working memory (last few minutes), pinned facts, episodic memory (conversations as stories), and a salience gate. Each night a sleep-cycle agent replays the day, consolidates useful patterns into reusable skills, hunts for contradictions (corrections always win), and gently expires stale data. In the morning a 'dream report' is generated summarizing what was consolidated, released, and learned. The entire system runs from one Cursor tab with 213 tools over a single protocol. Built for ~$30K vs a $230K agency quote, runs at ~$2K/month.

## Relevance to YOLO loop

Extends the YOLO loop with an offline improvement cycle — the system gets smarter between runs without human intervention, directly addressing long-term context decay and skill accumulation.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-11-multi-agent-dream-cycle` |
| Channel | aie |
| Video | [The Factory That Dreams: 39 AI Agents, No Framework - Rushabh Doshi, Machinecraft](https://www.youtube.com/watch?v=jtzh-GBXBWc) |
| Published | 2026-07-11 |
| Ingested upstream | 2026-07-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

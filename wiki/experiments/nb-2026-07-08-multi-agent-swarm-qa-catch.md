# Use a cheap-model swarm with a frontier orchestrator to auto-catch and rework agent failures

> Back to [[experiments-index]]

Source: **[Claude Fable 5 Bossed 20 Cheap AI Agents. The Whole Site Cost $8.](https://www.youtube.com/watch?v=suY66oTDn0s)** · nb · 2026-07-08

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we assign Claude Fable 5 as an orchestrator over cheaper worker models and route all task outputs through a machine QA checker before acceptance, then hallucinations and errors will be caught and reworked without human intervention because the review layer operates independently of the workers and can reject and requeue failed tasks.

## What they did

Speaker built a 20-agent system to rebuild a real production website in one run. Claude Fable 5 acted as orchestrator/foreman but never wrote content itself; four cheaper model families did all 34 tasks. Every task output was checked by an automated machine reviewer, not by humans. 12 of 34 tasks were caught and sent back for rework, including a hallucination of the client's words and three other distinct failures of increasing severity. The entire build went from blank repo to production in ~1.5-2.5 hours for $8, beating a 6-day human-steered single-agent build.

## Relevance to YOLO loop

Directly models a yolo-loop upgrade: instead of a human reviewing agent output before merge, a dedicated QA agent layer blocks bad outputs and triggers reruns, making the loop self-correcting.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-08-multi-agent-swarm-qa-catch` |
| Channel | nb |
| Video | [Claude Fable 5 Bossed 20 Cheap AI Agents. The Whole Site Cost $8.](https://www.youtube.com/watch?v=suY66oTDn0s) |
| Published | 2026-07-08 |
| Ingested upstream | 2026-07-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

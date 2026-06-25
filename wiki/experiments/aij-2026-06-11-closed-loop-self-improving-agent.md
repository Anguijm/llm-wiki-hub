# Implement a closed-loop agent with cron jobs, a temporal memory log, and auto-skill-proposal to create self-improving workflows

> Back to [[experiments-index]]

Source: **[How to build proactive agents & self-improving company (Fully explained)](https://www.youtube.com/watch?v=ikH1--DSzMs)** · aij · 2026-06-11

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `high`

---

## Hypothesis

If we give an agent a two-part memory layer (temporal log of actions/outcomes + evolving strategy doc), schedule cron jobs that execute tasks, capture feedback, and extract learnings, and include an instruction for the agent to propose skill updates after each cycle, then the agent's output quality improves autonomously over time without human re-prompting, because the feedback loop converts runtime observations into persistent procedural knowledge.

## What they did

Jason walked through the YC concept of 'self-improving companies' where agents handle internal ops and write their own tools. He described a closed-loop control system with five elements: data ingestion, policy/SOP layer, system access layer, quality gates (human or AI evaluator), and a learning feedback mechanism. He showed a concrete SEO example: cron jobs for audit, content drafting, publishing, and analytics reading; a memory layer split into a temporal log and a strategy doc; and a 'loopony' open-source plugin that adds company-in-the-loop memory optimised for long-cycle self-learning tasks. He demonstrated the setup wizard that interviews the user about desired AI loops and auto-generates cron jobs, artifact types, and skill proposals. He also mentioned the 'printing press' open-source tool for building agent-native CLIs with proper error messages and token efficiency.

## Relevance to YOLO loop

This is a meta-loop on top of the YOLO loop: the agent learns from each YOLO cycle and proposes improvements to its own skills and cron schedule, enabling the loop to self-optimise over time rather than requiring manual skill updates.

## Notes

Open-source tools mentioned: loopony (company-in-the-loop memory), printing press (agent-native CLI builder), jub brain (entity-based memory for personal assistant use). Memory layer structure: temporal log (what agent did) + strategy doc (latest hypothesis). Cron jobs are the trigger mechanism. Skill proposals are extracted during the daily/weekly cron run and must be approved or auto-applied.

Backlog triage 2026-06-24 (owner-preference model). Cron + temporal memory + auto-skill-proposal — this IS the YOLO loop; reinforces reflect/memory/skill-gen.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aij-2026-06-11-closed-loop-self-improving-agent` |
| Channel | aij |
| Video | [How to build proactive agents & self-improving company (Fully explained)](https://www.youtube.com/watch?v=ikH1--DSzMs) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Build a Manager-Agent Recipe Card to Orchestrate Multi-Step Admin Tasks

> Back to [[experiments-index]]

Source: **[There Are Jobs You Could Never Give AI. I Gave GPT-6 Astra 20 Hours Of Admin.](https://www.youtube.com/watch?v=ix8SsXjBc7M)** · nb · 2026-09-07

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we define a structured 'recipe card' for a manager agent that specifies task scope, required access, decision boundaries, escalation rules, and handoff criteria, then a long-running agentic model can autonomously complete large multi-step admin jobs (e.g., household move logistics) with minimal human interruption, because explicit guardrails and continuity instructions compensate for the model's lack of persistent memory and judgment about when to pause.

## What they did

Speaker spent several days handing GPT-6 Astra ~20 hours of household-move administrative work (finding doctors, comparing schools, DMV prep, utility transfers, etc.). Rather than prompting step-by-step, he created a 'recipe card' document given to a manager agent that defined: what the job is, what information/access the agent needs, what it can do autonomously vs. must escalate, what output to return, and how to handle failures (login failures, missing docs, blocked sites). He framed this as the 'Claude Code moment for knowledge work' and published 23 such recipe cards covering different home and business admin jobs.

## Relevance to YOLO loop

Directly applicable to our dev loop: instead of manually orchestrating multi-step agent tasks, we can author recipe cards that a manager agent uses to self-direct, self-recover, and hand off context — reducing the need for human prompt-chaining between steps.

## Notes

Recipe card structure: (1) job description, (2) required info/access, (3) autonomous vs. escalate boundary, (4) expected output format, (5) failure handling instructions. Speaker claims this pattern generalizes beyond moving to any large knowledge-work job.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-07 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-09-07-astra-admin-recipe-cards` |
| Channel | nb |
| Video | [There Are Jobs You Could Never Give AI. I Gave GPT-6 Astra 20 Hours Of Admin.](https://www.youtube.com/watch?v=ix8SsXjBc7M) |
| Published | 2026-09-07 |
| Ingested upstream | 2026-09-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

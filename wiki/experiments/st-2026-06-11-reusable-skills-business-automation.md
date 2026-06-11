# Build reusable Claude skill files for recurring business workflows

> Back to [[experiments-index]]

Source: **[The 8 Claude Skills Running My Business](https://www.youtube.com/watch?v=deJBemBwmcc)** · st · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we encode recurring business processes (email drafting, CRM updates, pre-call research, proposal generation) as reusable skill files that include business context, tool connectors, and process steps, then we will reduce per-task setup time from 30+ minutes to under 5 minutes and eliminate re-explanation overhead because the skill acts as persistent onboarding memory for the agent.

## What they did

Shaw described eight Claude skills he uses to run a solo business: a business strategist skill that pulls context from Notion, an email helper that learns his writing style from past Gmail threads and auto-drafts recurring sales emails, a business development skill that qualifies LinkedIn leads and spins up a Notion CRM, a copywriting skill synthesizing frameworks from Hormozi and Harry Dry, a CRM maintenance skill that auto-updates lead statuses daily, a pre-call research skill that populates call pages with prospect context, a proposal builder that drafts custom proposals from sales call notes, and an engagements database skill for client tracking. All skills use Notion and Gmail connectors and are available as open-source on GitHub.

## Relevance to YOLO loop

Directly applicable: we can create skill files for our own recurring dev-loop tasks (issue triage, PR description writing, test summarization, deployment checks) so agents execute correctly on first invocation without re-prompting.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `st-2026-06-11-reusable-skills-business-automation` |
| Channel | st |
| Video | [The 8 Claude Skills Running My Business](https://www.youtube.com/watch?v=deJBemBwmcc) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

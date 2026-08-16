# Implement a Scheduled Morning Agent Sync That Produces a Skimmable Action-Item Summary

> Back to [[experiments-index]]

Source: **[Exposing My (Business) AI OS as a Founder-CEO](https://www.youtube.com/watch?v=Ypa4E_ePUvI)** · st · 2026-08-16

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we configure a time-triggered agent (e.g., Claude CoWork) to run each morning against inbox, calendar, CRM, and project records and output a concise skimmable summary of required actions, then daily admin overhead will drop to under 30 minutes because the agent handles data gathering, cross-referencing, and draft generation autonomously, leaving only human judgment calls.

## What they did

Shaw showed three scheduled Claude CoWork automations that fire every morning. Each automation loads relevant SOPs as instructions, pulls live data via connectors (Gmail, Google Calendar, Notion, Stripe), cross-references records (CRM, engagement database, content calendar), and produces a structured summary of changes made and items needing human decision. For email triage it drafted replies and flagged threads. For content it audited the pipeline and flagged gaps. For client engagements it audited every active engagement, updated Notion properties, and listed pending actions (payment nudges, kickoff emails, testimonial rows) for a quick voice-dictated approval loop. The entire review across all three automations took him roughly 15-30 minutes each morning.

## Relevance to YOLO loop

Maps directly to the YOLO loop's need for a daily status pulse: we could run a morning agent sync against open experiment cards, PRs, blocked tasks, and incoming feedback channels to surface the day's highest-leverage actions without manual aggregation.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `st-2026-08-16-morning-agent-triage` |
| Channel | st |
| Video | [Exposing My (Business) AI OS as a Founder-CEO](https://www.youtube.com/watch?v=Ypa4E_ePUvI) |
| Published | 2026-08-16 |
| Ingested upstream | 2026-08-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

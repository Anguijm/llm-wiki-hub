# Run a draft-only 30-minute heartbeat agent

> Back to [[experiments-index]]

Source: **[The 4 Components of Every Successful AI Second Brain (Build These Now)](https://www.youtube.com/watch?v=qIWB1yMsqRo)** · cm · 2026-10-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we schedule a heartbeat agent every 30 minutes with draft-only email permissions and Slack summaries, then routine triage time will drop because the agent acts proactively while sending stays behind human approval.

## What they did

Cole's heartbeat cron runs every 30 minutes on a roughly $20/month VPS, triaging the inbox, drafting email replies and posting Slack summaries, which he says saves 30 to 60 minutes daily. Integrations are wrapped in custom CLI scripts or MCP servers that allow drafting but block sending. The heartbeat is enabled only after a capability has been tested manually one-on-one.

## Relevance to YOLO loop

high: It adds a scheduled, permission-scoped autonomous cadence to an agent workflow, with a manual-trust gate first.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-29 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `cm-2026-10-29-draft-only-heartbeat-triage` |
| Channel | cm |
| Video | [The 4 Components of Every Successful AI Second Brain (Build These Now)](https://www.youtube.com/watch?v=qIWB1yMsqRo) |
| Published | 2026-10-29 |
| Ingested upstream | 2026-10-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

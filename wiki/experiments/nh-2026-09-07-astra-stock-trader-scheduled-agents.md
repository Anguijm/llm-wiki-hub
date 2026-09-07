# Chain Stateless Scheduled Agents with a Shared Progress Log for Continuous Autonomous Operation

> Back to [[experiments-index]]

Source: **[I Turned GPT-6 Astra Into a 24/7 Stock Trader (tutorial)](https://www.youtube.com/watch?v=TLQLfa7yH4I)** · nh · 2026-09-07

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we schedule multiple stateless agent wakeups throughout the day and require each agent to (a) read a shared progress log written by the previous agent and (b) write its own handoff entry before sleeping, then the system will behave as a single continuous autonomous agent despite having no persistent memory, because shared written state provides the continuity that in-context memory cannot.

## What they did

Speaker configured GPT-6 Astra (via Codex) to run a 7-day $10,000 live stock trading challenge using the Alpaca brokerage API. He defined 6 scheduled wakeup times per trading day (7:45am pre-market news, 9:30am first trade, 11am position review, 1pm position management, 2:15pm close-out, 2:45pm end-of-day record). Each scheduled agent is stateless, so continuity is maintained via a shared progress log: each agent reads the previous handoff note, does its work, then writes a new handoff note. Notifications were routed to a ClickUp channel. A remote desktop sync allowed mobile monitoring. Sub-agents were fanned out to research trading strategy before the challenge began.

## Relevance to YOLO loop

Demonstrates a reusable pattern for any long-running autonomous loop in our dev system: scheduled triggers + shared written state as memory substrate. The handoff-log pattern is directly portable to CI/CD agents, monitoring agents, or any multi-session agentic workflow we build.

## Notes

Key insight: 'Continuity comes from shared records, not the AI remembering the conversation.' Alpaca used as brokerage API. ClickUp used for notifications. Not financial advice — paper trading recommended before live capital. Previous Claude challenge reportedly beat S&P by 8% over one month.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-07 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-07-astra-stock-trader-scheduled-agents` |
| Channel | nh |
| Video | [I Turned GPT-6 Astra Into a 24/7 Stock Trader (tutorial)](https://www.youtube.com/watch?v=TLQLfa7yH4I) |
| Published | 2026-09-07 |
| Ingested upstream | 2026-09-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Use an AI agent to root-cause recurring support tickets and close the upstream failure

> Back to [[experiments-index]]

Source: **[You Can Hand One AI Agent Your Worst Recurring Task. It Cleared 60% Of Mine.](https://www.youtube.com/watch?v=7pqRRxrdr0c)** · nb · 2026-07-26

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we feed an AI agent a batch of recurring support tickets and ask it to identify the full hidden work chain (not just the reply), then we can root-cause and eliminate entire ticket categories because the agent can surface patterns across cases faster and more completely than manual review.

## What they did

Nate collected a week of customer support tickets (52 cases), identified the biggest recurring category (Slack access failures), and used an AI agent to analyze the full manual labor chain hidden inside each ticket type—finding email, checking payment, looking in Slack, sending invite, writing apology, closing ticket. The agent helped root-cause four or five sub-patterns (expired links, email mismatch, no invite received, etc.), propose solutions (non-expiring invite link, approved email domain self-service), and roll them out. The following comparable week dropped from 52 to 19 total tickets and Slack access disappeared as a category entirely. He also described a structured agent protocol: show which customer record was found, what is true now, where each fact came from, which prior cases looked similar, what it recommends, and critically—what it is unsure about. Draft mode for first 20–30 cases with human review, turning corrections into a standard operating procedure. A scorecard tracks cases in, cases resolved, causes, drafts corrected, and hands-on time remaining.

## Relevance to YOLO loop

Directly models the YOLO loop's observe-hypothesize-act-measure cycle: ingest real failure signals (tickets), agent-assisted root cause, implement fix, measure next-week delta. The scorecard and draft-review protocol map cleanly onto our eval and correction infrastructure.

## Notes

Key protocol detail: explicitly ask the agent what it is unsure about to expose hidden assumptions. When systems disagree, agent must surface disagreement rather than quietly picking the easiest answer. Screen-record yourself solving cases and feed that to the agent as SOP seed material.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-26 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-26-ai-agent-support-root-cause-loop` |
| Channel | nb |
| Video | [You Can Hand One AI Agent Your Worst Recurring Task. It Cleared 60% Of Mine.](https://www.youtube.com/watch?v=7pqRRxrdr0c) |
| Published | 2026-07-26 |
| Ingested upstream | 2026-07-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

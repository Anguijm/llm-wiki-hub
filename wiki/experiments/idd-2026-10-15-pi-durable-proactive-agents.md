# Build a proactive Pi durable agent triggered by a Jev classifier on a live event stream to handle on-call incident response without human initiation

> Back to [[experiments-index]]

Source: **[Pi Durable PROACTIVE Agents: Jev Triggers My ON-CALL Pi Agent](https://www.youtube.com/watch?v=DNDYYHsypZg)** · idd · 2026-10-15

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we attach a Pi durable agent to a Jev event-classification stream so the agent starts working on detected incidents before any human shows up, then engineering on-call burden drops significantly because the agent can autonomously detect, investigate, root-cause, fix, and stage a deploy for human approval — the human only approves or declines, never initiates.

## What they did

Dan demonstrated a proactive Pi durable agent wired to a market application's live event stream. Jev (a classifier model) monitors every incoming event for pennies, detects incidents, and triggers a Pi durable agent with the payload (issue, location, error). The agent follows a standard operating procedure: detect → investigate → root-cause analysis → fix → stage for review. It persists all state through failures and client disconnects (durable). Dan showed a real incident: a null-check bug in a loyalty discount checkout API causing incorrect pricing. The agent diagnosed it, produced a code diff, and awaited his approval. He approved the deploy with one click. He ran this across M4 Mac Mini, M6 Mac Mini, M5 MacBook Pro, and exe.dev cloud sandboxes simultaneously. He described Pi durable as multi-client — the agent is detached and any team member can connect to it as a client. Key concept: proactive agents work for you then wait, rather than waiting for you to start them.

## Relevance to YOLO loop

high: Pi durable is a core agent harness primitive — persistent, multi-client, proactive, out-of-loop — directly advancing the Claude Code workflow architecture the operator is building.

## Notes

Dan linked the network demo, proactive agent demo, and Pi durable docs in the video description. Phase 3 course pre-enroll also linked. The Jev classifier cost at scale (~1.5 cents per hundreds of events) is a useful benchmark.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `idd-2026-10-15-pi-durable-proactive-agents` |
| Channel | idd |
| Video | [Pi Durable PROACTIVE Agents: Jev Triggers My ON-CALL Pi Agent](https://www.youtube.com/watch?v=DNDYYHsypZg) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

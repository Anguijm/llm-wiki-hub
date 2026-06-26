# Build a shared task queue so multiple AI agents hand off work with full context

> Back to [[experiments-index]]

Source: **[I Was The Only Thing Connecting Claude, ChatGPT, and Codex. So I Built My Replacement.](https://www.youtube.com/watch?v=QSK4vf_ZTRA)** · nb · 2026-06-26

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we implement a lightweight shared queue (Open Engine) that passes structured context and receipts between Claude, Codex, ChatGPT, and other agents, then we eliminate the human-as-hallway bottleneck and reduce copy-paste handoff labor because each agent loop can pick up state exactly where the previous one left off.

## What they did

Nate built 'Open Engine', a queue-based coordination layer that lets different AI agents (Claude Code, Codex, ChatGPT, OpenClaw/Hermes) pass work items, source material, and status receipts to each other without a human manually relaying context. Each agent loop reads from and writes to the queue, includes what it did and didn't do, and routes to the next appropriate agent or human decision point. He uses it personally for household logistics, moving, and team coordination, and described the core test as: can work leave a chat, carry its sources, respect limits, and return a receipt?

## Relevance to YOLO loop

Directly addresses the multi-agent handoff problem in YOLO loop — if different specialist agents (coding, review, planning) run sequentially, a shared queue with receipts would replace manual context passing between loop iterations.

## Notes

Author offers a full guide on Substack with an active Slack community. Core pattern: queue + source bundle + receipt. Worth examining the data structure for the 'work item' schema before building.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-26 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-06-26-open-engine-multi-ai-queue` |
| Channel | nb |
| Video | [I Was The Only Thing Connecting Claude, ChatGPT, and Codex. So I Built My Replacement.](https://www.youtube.com/watch?v=QSK4vf_ZTRA) |
| Published | 2026-06-26 |
| Ingested upstream | 2026-06-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Reduce context-loading friction by pre-wiring relevant workspace context into agent sessions

> Back to [[experiments-index]]

Source: **[Apple, Anthropic, And OpenAI Just Made The Same Move. Nobody Noticed.](https://www.youtube.com/watch?v=H9oNA5IyrXA)** · nb · 2026-07-02

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we pre-attach structured workspace context (current file state, recent decisions, relevant thread summaries) to agent sessions before the user issues a request, then perceived utility will increase significantly because the majority of current AI friction is not model capability but the manual tax of briefing the model on situational context each session.

## What they did

Speaker analyzed Apple Siri's redesign, Claude Tag in Slack, and OpenAI Codex internal adoption as three parallel attempts to solve the same problem: models are capable but require users to manually carry full situational context into every session via copy-paste and file uploads. He framed this as a 'context war' where the next competitive advantage is not smarter models but seamless context proximity. Claude Tag lets a team pre-authorize Claude's access to specific Slack channels/codebases; Siri connects to on-device calendar/email/photos; Codex operates inside the repo. All three reduce the briefing tax.

## Relevance to YOLO loop

Our yolo loop currently requires manual context injection per run. This experiment suggests building a context pre-loader that automatically attaches: current branch diff, last N commit messages, open issues, and any flagged decision docs — so agents start sessions already oriented. Maps to the 'context window hydration' step before task dispatch.

## Notes

Speaker predicts government-driven slowdown in frontier releases will intensify pressure on context-layer utility. Open-source models closing the gap in public benchmarks makes context advantage more durable than model-capability advantage.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-02-context-war-harness-strategy` |
| Channel | nb |
| Video | [Apple, Anthropic, And OpenAI Just Made The Same Move. Nobody Noticed.](https://www.youtube.com/watch?v=H9oNA5IyrXA) |
| Published | 2026-07-02 |
| Ingested upstream | 2026-07-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

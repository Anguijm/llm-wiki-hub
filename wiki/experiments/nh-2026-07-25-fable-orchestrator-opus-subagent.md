# Use Fable as a Delegating Orchestrator to Preserve Context Window Budget

> Back to [[experiments-index]]

Source: **[I Tested Opus 5 vs. Fable 5. What You Need to Know.](https://www.youtube.com/watch?v=2J3uX8iRNng)** · nh · 2026-07-25

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we configure Fable 5 purely as an orchestrator that delegates execution to Opus 5 subagents without writing or executing code itself, then Fable's context window will stay well under 300-400K tokens even in multi-hour sessions because all token-heavy generation work is offloaded to cheaper Opus instances.

## What they did

Nate described a pattern where Fable 5 is prompted with an explicit instruction not to write or execute any code itself, only to delegate tasks to Opus. He observed that Fable sessions running this way could last multiple hours or a full day without hitting 300-400K context tokens. This preserves the Fable session for high-level reasoning and coordination while Opus handles the token-expensive implementation work at lower per-token cost.

## Relevance to YOLO loop

Directly applicable to our YOLO loop architecture: framing the top-level agent as a pure planner/delegator is a concrete prompt engineering change we can test immediately to extend effective session length and reduce cost per loop iteration.

## Notes

Simple prompt constraint to test: add 'You should not write any code or execute anything; only delegate to subagents' to Fable system prompt and measure context growth rate over a long session.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-25 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-07-25-fable-orchestrator-opus-subagent` |
| Channel | nh |
| Video | [I Tested Opus 5 vs. Fable 5. What You Need to Know.](https://www.youtube.com/watch?v=2J3uX8iRNng) |
| Published | 2026-07-25 |
| Ingested upstream | 2026-07-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

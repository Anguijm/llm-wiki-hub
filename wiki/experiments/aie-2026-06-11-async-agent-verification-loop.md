# Give agents MCP access to the target environment so they can self-verify before surfacing results

> Back to [[experiments-index]]

Source: **[How to Keep Shipping When You Walk Away from Your Desk — Zack Proser, WorkOS](https://www.youtube.com/watch?v=so9l_MwS2yg)** · aie · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we grant the coding agent write-and-read access to the runtime environment (e.g. Slack channel, test suite, staging URL) alongside the codebase, then the agent can close its own feedback loop and return only verified completions, reducing human review overhead because the agent catches regressions before handing back control.

## What they did

Proser added an MCP connection to Slack for Claude Code so that after fixing a sentence-case bug it could post to the blog channel, observe the blog bot's output, and confirm the fix end-to-end before declaring done. He also described a broader async pattern: queue work as Linear tickets tagged 'agent-ready', run a cron loop every 15 minutes to churn through tickets overnight, use voice-first input to brief agents before stepping away, and review summarized results on return rather than babysitting execution.

## Relevance to YOLO loop

Core pattern for our YOLO loop: attaching environment-side verification tools (test runner, log reader, channel poster) to the agent so the loop closes without human intervention and we wake up to done tickets rather than stalled agents.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-11-async-agent-verification-loop` |
| Channel | aie |
| Video | [How to Keep Shipping When You Walk Away from Your Desk — Zack Proser, WorkOS](https://www.youtube.com/watch?v=so9l_MwS2yg) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

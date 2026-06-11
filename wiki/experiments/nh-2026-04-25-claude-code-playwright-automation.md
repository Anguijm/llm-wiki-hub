# Wire Claude Code to Playwright for End-to-End Test Authoring and Execution

> Back to [[experiments-index]]

Source: **[Claude Code + Playwright Automates Literally Anything](https://www.youtube.com/watch?v=J-6pnl5DQg8)** · nh · 2026-04-25

**Status:** `deferred` · **Effort:** `medium`

---

## Hypothesis

If we give Claude Code direct access to a Playwright MCP or subprocess tool, then it can autonomously write, run, and fix E2E tests against our running app because Claude Code's agentic loop handles the observe-act-verify cycle that Playwright requires without human scaffolding.

## What they did

Speaker demonstrated Claude Code driving Playwright to automate browser-based workflows — writing test scripts, executing them, reading DOM/network results, and iterating — without manually authoring Playwright code, effectively making Claude the test engineer.

## Relevance to YOLO loop

High-value integration: adds an automated verification layer to the YOLO loop so that after code gen, Claude can self-validate UI behavior via Playwright before surfacing results. Closes the feedback cycle without human QA intervention.

## Notes

[2026-05-06T19:43:19Z] DEFER: Playwright is already wired in for browser tests. The experiment isn't well-scoped beyond what we have.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-25 | `backlog` | Extracted from YouTube RSS |
|  | `` | Triage 2026-05-05: Playwright is already wired in for browser tests. The experiment isn't well-scoped beyond what we have. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-04-25-claude-code-playwright-automation` |
| Channel | nh |
| Video | [Claude Code + Playwright Automates Literally Anything](https://www.youtube.com/watch?v=J-6pnl5DQg8) |
| Published | 2026-04-25 |
| Ingested upstream | 2026-04-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

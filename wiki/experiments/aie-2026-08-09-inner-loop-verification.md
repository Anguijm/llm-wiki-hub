# Embed Static Analysis Verification Inside the Agentic Coding Loop Before PR Creation

> Back to [[experiments-index]]

Source: **[Guide, Verify, Solve — Anirban Chatterjee, Sonar](https://www.youtube.com/watch?v=03l29gJXpCE)** · aie · 2026-08-09

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If a static analysis tool is called automatically inside the agent's inner loop after each code generation step—and the agent is blocked from proceeding until issues are fixed—then code quality will be higher at PR creation time because the agent self-corrects rather than deferring quality issues to human review.

## What they did

Sonar demoed Sonar Vortex integrated directly with Cursor (and Claude Code, Codex, etc.) via MCP. When the agent writes code, it automatically calls a verification tool, receives a list of static analysis issues (maintainability, reliability, security), fixes them in the same session, and only proceeds once it passes the quality gate. The same verification runs again in the outer CI/CD loop. A CMU study was cited showing AI-assisted projects had a temporary productivity spike but persistent increase in static analysis warnings that ultimately slowed teams down—motivating the need for inner-loop verification.

## Relevance to YOLO loop

Core to the YOLO loop's verification step—inserting an automated static analysis gate inside the agentic generation loop (before the human review step) could catch a class of issues before they reach PR review, reducing human review burden and improving merge quality.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-09-inner-loop-verification` |
| Channel | aie |
| Video | [Guide, Verify, Solve — Anirban Chatterjee, Sonar](https://www.youtube.com/watch?v=03l29gJXpCE) |
| Published | 2026-08-09 |
| Ingested upstream | 2026-08-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

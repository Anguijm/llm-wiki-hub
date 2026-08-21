# Implement inner-loop vs outer-loop agent quality checks with a PR-attached evidence table to build reviewer confidence in autonomous diffs

> Back to [[experiments-index]]

Source: **[Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](https://www.youtube.com/watch?v=17-YSUHo6Lk)** · aie · 2026-08-21

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we separate fast lightweight checks (smaller model static analysis, visual screenshot vs Figma diff, integration smoke test) into an inner loop that runs before commit, and reserve deep reasoning code review for the outer loop CI stage, then autonomous PRs will arrive at human review already self-improved and with an attached evidence table of which checks passed, reducing review friction and the rate of CI failures requiring human intervention, because reviewers can trust the diff has already gone through a structured self-healing process.

## What they did

Uber's engineering team (thousands of engineers, 70%+ of PRs now touched by local or cloud agents, 2x lines of code per engineer YoY, 250+ automated migrations covering 9M lines) described a six-building-block agentic SDLC: model gateway (PII redaction, attribution, spend guardrails, <100ms overhead), MCP gateway (Omni MCP + CLI projection to cut token tax, 40% fleet-wide token savings), pre-provisioned Kubernetes agent sandboxes with snapshotted repos, an inner/outer loop quality framework, self-healing CI, and scheduled maintenance skills (feature flag cleanup, etc.). The inner loop runs a smaller/medium model for fast checks; the outer loop uses a powerful reasoning model for deep review. Every autonomous PR gets an attached table listing every check it passed (including simulator screenshots vs Figma specs). Maintenance loops are managed centrally with rate limits on Monday diff volume to avoid overwhelming engineers.

## Relevance to YOLO loop

The inner/outer loop split and the PR evidence table are directly applicable to our YOLO loop: we can add a post-generation checklist step that runs cheap fast checks (lint, type check, unit tests, screenshot diff) before surfacing output for review, and append a structured summary of what passed to every agent-produced diff, increasing trust and reducing manual re-checking.

## Notes

Most actionable near-term takeaway: the PR evidence table (listing checks the agent ran on its own output) is a low-effort addition to our current loop output format. The Omni MCP pattern (one install point that discovers and invokes all downstream MCPs) and CLI projection to avoid context-window token tax are also worth prototyping separately.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-21 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-21-uber-agentic-sdlc-inner-outer-loop` |
| Channel | aie |
| Video | [Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](https://www.youtube.com/watch?v=17-YSUHo6Lk) |
| Published | 2026-08-21 |
| Ingested upstream | 2026-08-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

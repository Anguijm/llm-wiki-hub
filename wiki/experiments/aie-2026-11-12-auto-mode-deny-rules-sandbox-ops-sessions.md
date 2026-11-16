# Trial auto mode with deny rules and OS sandbox on one ops session

> Back to [[experiments-index]]

Source: **[Rethinking Claude Code Best Practices — Lydia Hallie, Anthropic](https://www.youtube.com/watch?v=vlfCjWuv4es)** · aie · 2026-11-12

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we switch one always-on Claude Code ops session from manual approvals to auto mode with plain-English trust rules, explicit deny rules for irreversible actions (such as reading .env) and an OS-enforced sandbox, then we will see fewer approval interruptions without dangerous commands getting through, because the safety guarantee moves into the harness and sandbox instead of relying on a human approving each step.

## What they did

Lydia Hallie described moving a session from manual mode to auto mode. The steps were: write trust rules in plain English in settings for deploy repos and buckets; keep explicit deny rules for irreversible actions; run local shell commands inside an OS sandbox that limits file reads, writes and hosts, or use isolated cloud sessions with domain allowlists; and trim CLAUDE.md to non-obvious context with a doctor prompt audit. She cited an Anthropic August study in which auto mode blocked about 89% of clearly dangerous commands versus about 14% caught by humans, with about 1 in 10 still getting through. She also noted that the sandbox covers only shell commands and child processes, not Claude's own files, MCP servers or hooks.

## Relevance to YOLO loop

high: Auto mode with plain-English trust rules, harness-level deny rules and an OS sandbox as a replacement for manual approvals is not among the existing practices, which cover gates, reviewers and scheduled jobs but not the permission model.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-15 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-11-12-auto-mode-deny-rules-sandbox-ops-sessions` |
| Channel | aie |
| Video | [Rethinking Claude Code Best Practices — Lydia Hallie, Anthropic](https://www.youtube.com/watch?v=vlfCjWuv4es) |
| Published | 2026-11-12 |
| Ingested upstream | 2026-11-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

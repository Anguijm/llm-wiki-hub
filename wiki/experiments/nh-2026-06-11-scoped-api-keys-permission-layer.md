# Implement scoped API keys per integration to enforce a read-only permission layer for Claude Code connections

> Back to [[experiments-index]]

Source: **[I Turned Claude Fable Into The Ultimate Second Brain](https://www.youtube.com/watch?v=8QQ_INxAhRs)** · nh · 2026-06-11

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we issue scoped API keys that restrict Claude Code integrations to specific read-only endpoints (e.g., Fireflies transcripts read-only, ClickUp tasks read-only), then we reduce the blast radius of agent mistakes because even if Claude Code acts incorrectly on a live connection it cannot delete, modify, or exfiltrate data beyond the scope of that key.

## What they did

Speaker described using scoped API keys as a practical permission layer for live connections in his AI OS. Example: a Fireflies API key scoped only to reading meeting transcripts—it cannot edit, delete, or interact with team data. He walked through the pattern of searching for API documentation, giving it to Claude Code, and asking Claude to identify the exact endpoints needed and what permissions are required. He framed this as the answer to 'what can your Claude Code physically do, not just prompt-wise' and recommended it as a safety practice before enabling any live data connection.

## Relevance to YOLO loop

Immediately applicable to any live API connection we add to our dev loop. Before connecting Claude Code to any service (GitHub, Notion, CI/CD), issue a scoped read-only key and document the permission boundary in our claude.md.

## Notes

Backlog triage 2026-06-24 (owner-preference model). Least-privilege scoped keys — security/guardrail match; low effort.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-06-11-scoped-api-keys-permission-layer` |
| Channel | nh |
| Video | [I Turned Claude Fable Into The Ultimate Second Brain](https://www.youtube.com/watch?v=8QQ_INxAhRs) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

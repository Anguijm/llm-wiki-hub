# Implement pre-tool-call hooks that programmatically block dangerous agent commands

> Back to [[experiments-index]]

Source: **[I open-sourced my Agent Skills repo (it went viral)](https://www.youtube.com/watch?v=clrUbBtD2j4)** · do · 2026-08-02

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we add a pre-tool-call hook shell script that pattern-matches and blocks dangerous commands (recursive deletes, remote Git history rewrites, piping internet to shell, fork bombs) before execution, then YOLO-mode agent runs will be significantly safer without requiring per-command human approval because the block happens at the OS level before the tool call completes, not just in the system prompt.

## What they did

David described his #1 skill from his viral 42-skill GitHub repo: global agent guardrails implemented as pre-tool-call hooks (not just system prompt instructions). The hooks are shell scripts that run before every tool call and deny execution if the command matches a blocklist of dangerous patterns including rm -rf on root/home, disk destroyers, admin-powered deletes, fork bombs, piping internet to shell, rewriting remote Git history, and deleting remote branches/tags. He emphasized that system-prompt-only safety instructions are insufficient for YOLO mode; only programmatic hooks that intercept before execution provide real protection. The repo is at github.com/davidandr/skills.

## Relevance to YOLO loop

YOLO loop runs agents with auto-approval. This hook pattern is the missing safety layer — it converts a trust-based safety model into an enforcement-based one, directly applicable to any Claude Code or Codex YOLO session.

## Notes

Repo: github.com/davidandr/skills — hooks directory contains the pre-tool-call shell scripts referenced.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-08-02-global-agent-guardrails-hooks` |
| Channel | do |
| Video | [I open-sourced my Agent Skills repo (it went viral)](https://www.youtube.com/watch?v=clrUbBtD2j4) |
| Published | 2026-08-02 |
| Ingested upstream | 2026-08-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

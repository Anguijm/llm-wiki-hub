# Add secret-leak guard hook and test agent key echo

> Back to [[experiments-index]]

Source: **[Black October Isn't Just A PHP Bug. Attackers Want Your AI Keys.](https://www.youtube.com/watch?v=qDYe2eTl_D4)** · nb · 2026-10-24

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we add a PreToolUse/PostToolUse hook that scans agent output, logs and outbound URLs for API keys and personal identifiers, then Claude Code sessions will stop echoing secrets into logs or URLs because the leak path is blocked deterministically instead of relying on prompt instructions.

## What they did

The speaker described websites prompting web-browsing agents to declare their identity, which caused agents to leak user email addresses inside URLs. He recommended prompt hygiene so coding agents don't echo API keys or personal identifiers into public logs or modified URLs. He also said defensive models should inspect ephemeral CI/CD build histories and not stop at clean git repos, and that dead unauthenticated code paths should be pruned.

## Relevance to YOLO loop

high: Directly applicable to Claude Code hooks and verification loops, since a secret-scanning hook is a concrete harness safeguard.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-27 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-10-24-agent-secret-hygiene` |
| Channel | nb |
| Video | [Black October Isn't Just A PHP Bug. Attackers Want Your AI Keys.](https://www.youtube.com/watch?v=qDYe2eTl_D4) |
| Published | 2026-10-24 |
| Ingested upstream | 2026-10-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

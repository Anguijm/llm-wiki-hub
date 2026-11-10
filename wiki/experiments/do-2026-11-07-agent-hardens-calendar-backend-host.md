# Have Claude Code harden a cloned calendar-backend host

> Back to [[experiments-index]]

Source: **[The Ultimate Linux Tutorial for AI Agents (watch before 2027)](https://www.youtube.com/watch?v=us6SRuWuqWc)** · do · 2026-11-07

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we let Claude Code harden a disposable clone of the family calendar app's self-hosted backend host (UFW, key-only SSH, fail2ban) over SSH, then we get a reviewed, repeatable hardening checklist in under an hour because the speaker's agent secured a raw Ubuntu server in about 2.5 minutes from plain-English instructions.

## What they did

David Ondrej connected Claude Code to a fresh Ubuntu VPS over an SSH key. He prompted it in plain English to configure the UFW firewall, disable password authentication and install fail2ban, which took about 2.5 minutes. He then had it deploy a 4-service app (Caddy, Node.js, Postgres, ClickHouse) in about 3.5 minutes. He warned that root access risks destructive commands such as rm -rf / unless the environment is sandboxed.

## Relevance to YOLO loop

medium: Delegating server hardening to an agent is a new use, but it mostly applies existing sandboxing and human-review practices.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-09 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-11-07-agent-hardens-calendar-backend-host` |
| Channel | do |
| Video | [The Ultimate Linux Tutorial for AI Agents (watch before 2027)](https://www.youtube.com/watch?v=us6SRuWuqWc) |
| Published | 2026-11-07 |
| Ingested upstream | 2026-11-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

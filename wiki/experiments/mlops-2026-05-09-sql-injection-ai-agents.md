# Add input sanitization and query allowlisting to agent database tools

> Back to [[experiments-index]]

Source: **[Stop AI Agents From SQL Injecting Your Database](https://www.youtube.com/watch?v=jDxAtxGv3fI)** · MLOps · 2026-05-09

**Status:** `deferred` · **Effort:** `medium`

---

## Hypothesis

If we sanitize and constrain the SQL an AI agent can generate before execution, then we will prevent prompt-injection and SQL injection attacks on the database because agents that construct queries from untrusted user input are vulnerable without explicit guardrails.

## What they did

Inferred from title: the video covers techniques to prevent AI agents from being manipulated into executing malicious SQL queries against a database, likely covering parameterization, allowlisted query patterns, or sandboxed read-only access.

## Relevance to YOLO loop

Directly relevant if our dev loop agents have database write access; adding query constraints or a review gate before execution reduces risk of agent-induced data corruption.

## Notes

Deferred 2026-05-10: security-flavored topic worth flagging in the security angle's prompt, but no current YOLO project handles SQL agents. Park; promote if a tick uses SQL tools.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-09 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-05-09-sql-injection-ai-agents` |
| Channel | MLOps |
| Video | [Stop AI Agents From SQL Injecting Your Database](https://www.youtube.com/watch?v=jDxAtxGv3fI) |
| Published | 2026-05-09 |
| Ingested upstream | 2026-05-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

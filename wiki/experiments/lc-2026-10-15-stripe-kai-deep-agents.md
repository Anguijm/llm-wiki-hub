# Structure agent skills so each skill declares its own allowed tool subset to avoid context overflow at scale

> Back to [[experiments-index]]

Source: **[How Stripe Built Kai](https://www.youtube.com/watch?v=rduH9wnXto8)** · lc · 2026-10-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If each agent skill carries its own list of allowed tools so that selecting a skill decides which tools load into context, then a single agent can expose 500+ tools without context overflow because at any moment only a handful of tools are active, and foundational skills remain pinned to preserve core policies.

## What they did

Stripe built 'Kai', an internal assistant with 1000+ skills and 500 tools using LangChain's Deep Agents harness. Rather than loading all tools into one system prompt, each skill declares its allowed tools so context stays small. Foundational skills are always pinned. Code is written outside a sandbox but executed inside one for safety. State is persisted via a virtual file system backed by S3. One engineer built the first working version in one week; adoption grew 16x in a month to 60,000 sessions/week.

## Relevance to YOLO loop

high: the skill-scoped tool-loading pattern directly addresses context management in Claude Code agent workflows—maps to skills and harness design in the operator's agent council/hooks architecture.

## Notes

Deep Agents is open-source. Key architectural decisions: skill = tool allowlist, foundational skills always pinned, S3-backed virtual filesystem for cross-turn persistence, sandbox for code execution. 'Solves all the non-Stripey problems so the team focuses on Stripe problems.'

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `lc-2026-10-15-stripe-kai-deep-agents` |
| Channel | lc |
| Video | [How Stripe Built Kai](https://www.youtube.com/watch?v=rduH9wnXto8) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

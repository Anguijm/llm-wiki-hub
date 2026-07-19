# Implement fine-grained, principal-bound, time-limited auth scopes for agents instead of reusing human OAuth credentials

> Back to [[experiments-index]]

Source: **[You Didn't Ship a Bug. You Just Wrote It for a Human. - Ravi Madabhushi, Scalekit](https://www.youtube.com/watch?v=lMCxVorb9wM)** · aie · 2026-07-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we give agents their own distinct identity with fine-grained attribute-level, context-level, and principal-level scopes that are time-limited to the duration of the task, then agents will be prevented from taking unintended destructive actions (e.g. deleting production databases), because broad OAuth scopes combined with non-deterministic agent behavior create an attack surface that cannot be audited by code review the way deterministic programs can.

## What they did

Speaker observed that agents hitting their identity platform were updating 'last seen' timestamps 60x faster than humans, causing unnecessary DB write pressure — a symptom of human-designed auth being misapplied to agent actors. He argued that existing auth primitives (human sessions, API keys, service accounts, OAuth) all assume the authenticating principal equals the acting principal and that behavior is deterministic and inspectable. Agents break both assumptions: they are non-deterministic and probabilistic. He found that most customer agents have far more permissions than their actual job requires. His prescription: agents must have their own identity (not delegated human credentials), scopes must be attribute-level (e.g. 'send email only to these recipients'), time-bounded to task duration, and every action must be logged with who authorized it, when, and for how long. He cited ref.tools as a customer that built their entire product around agent-native OAuth scoping.

## Relevance to YOLO loop

Directly relevant to any YOLO loop that makes tool calls on behalf of users or accesses external APIs. The loop should be audited for over-provisioned scopes; implement just-in-time authorization requests for elevated permissions rather than running with standing broad credentials.

## Notes

Speaker is co-founder of Scalekit (identity/auth infrastructure). Core checklist for agent auth audit: (1) Does the agent have its own identity? (2) Are scopes attribute-level not role-level? (3) Are credentials time-limited to task duration? (4) Is every action logged with authorizer, timestamp, and scope granted?

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-19-agent-auth-least-privilege` |
| Channel | aie |
| Video | [You Didn't Ship a Bug. You Just Wrote It for a Human. - Ravi Madabhushi, Scalekit](https://www.youtube.com/watch?v=lMCxVorb9wM) |
| Published | 2026-07-19 |
| Ingested upstream | 2026-07-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

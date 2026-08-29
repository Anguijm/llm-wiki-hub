# Use a capped Codex subscription to build internal SaaS clones and measure real token cost vs. subscription value

> Back to [[experiments-index]]

Source: **[I Cloned Calendly and Now It's Free Forever](https://www.youtube.com/watch?v=PYjbeY8sGLs)** · nh · 2026-08-29

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we use a $200/month Codex plan with parallel sub-agents to build internal tool clones of paid SaaS products, then we can replace recurring subscription fees with a one-time build cost at roughly $14,000 of inference value per plan cycle, because Codex's subscription pricing provides ~$6,000 more inference than Claude Code at the same price tier.

## What they did

Nate built a full Calendly clone (called Snag Time) over ~5 working days using OpenAI Codex with parallel sub-agents. The system consumed 32 billion input tokens and 47 million output tokens, with a market-rate inference cost of ~$15,000, but Nate paid only ~$200 (plan) plus ~$150 in overage credits. He used swarm-style verification loops (50+ agents simultaneously clicking around to break the app), spun up 76 unique sub-agents totalling 334 aggregate agent-hours, and delivered Google Calendar sync, Stripe payments, multi-member workspaces, and custom event types. He explicitly compared Codex vs. Claude Code subscription value and noted ongoing maintenance is a few prompts per month.

## Relevance to YOLO loop

Directly tests the YOLO loop at scale: a long-running multi-agent swarm with verification loops is exactly the pattern the loop is designed to support; the cost and token data provide a concrete benchmark for budgeting similar internal builds.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-29-codex-saas-clone-cost-analysis` |
| Channel | nh |
| Video | [I Cloned Calendly and Now It's Free Forever](https://www.youtube.com/watch?v=PYjbeY8sGLs) |
| Published | 2026-08-29 |
| Ingested upstream | 2026-08-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Replace per-tool MCP servers with role-based gateway servers that model business operations

> Back to [[experiments-index]]

Source: **[What We Learned from Dozens of Enterprise MCP Deployments](https://www.youtube.com/watch?v=t2RknZh8U9I)** · mlops · 2026-08-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we replace thin API-wrapper MCP servers with role-based MCP servers that expose business-meaningful operations (e.g., a 'get_revenue' function defined per our business logic rather than a generic Salesforce API call), then agents will make fewer errors and require less prompt engineering to use correctly, because the tool surface matches how the business actually thinks about operations rather than how the underlying API is structured.

## What they did

JQ (MintMCP co-founder, formerly Coursera/Google Brain) shared findings from monitoring 1.8M+ MCP agent calls per week across enterprise customers. Key findings: the most-used MCP connectors are everyday business tools (Gmail, Calendar, Slack, Figma, HubSpot) not engineering tools, meaning non-technical users are now the primary MCP consumers. First-party MCP servers are mostly thin API wrappers that don't reflect business semantics, causing agents to misuse them. He recommended enterprises build custom MCP servers encoding business-specific operations, use a gateway layer for auth/routing/security (buy, not build), move from local execution to managed cloud hosting to reduce supply-chain risk, and adopt OAuth short-lived tokens (away from pasted credentials). 25% of AI usage at Coursera now comes from non-technical staff.

## Relevance to YOLO loop

Directly shapes how we design MCP tool surfaces for our agents: building role-based servers that match our domain model rather than wrapping raw APIs will reduce the agent reasoning overhead in every YOLO loop step that involves external data or actions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-08-19-enterprise-mcp-role-based-gateway` |
| Channel | mlops |
| Video | [What We Learned from Dozens of Enterprise MCP Deployments](https://www.youtube.com/watch?v=t2RknZh8U9I) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

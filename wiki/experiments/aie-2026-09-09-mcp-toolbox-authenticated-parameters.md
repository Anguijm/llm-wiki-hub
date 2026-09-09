# Use MCP Toolbox authenticated parameters to bind user identity to DB tools without exposing PII to the agent

> Back to [[experiments-index]]

Source: **[Build-Time vs. Run-Time: Why Dev Tools Fail in Production — Averi Kitsch & Prerna Kakkar, Google](https://www.youtube.com/watch?v=9R--1tg45Jg)** · aie · 2026-09-09

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we configure MCP database tools with authenticated parameters that extract user claims from a validated JWT rather than accepting user_id as an agent-controlled input, then agents will be unable to impersonate other users or access unauthorized data, because the identity binding happens server-side at the tool layer before the SQL query is constructed, removing PII entirely from the agent's control plane.

## What they did

Averi Kitsch and Prerna Kakkar (Google Cloud) presented MCP Toolbox for Databases (15.7K GitHub stars, 132+ contributors, 40+ databases, 20M tool calls last month). They distinguished build-time tools (NL2SQL, control-plane/admin — require human-in-loop, flexible but dangerous) from runtime/production tools (structured SQL with predefined parameterized queries, no SQL injection risk, lower hallucination). They demonstrated a chatbot (Symbolair) where an attacker tried to book a flight as a different user — the agent correctly rejected it because user identity was extracted from a validated OIDC token, never passed by the agent. Two binding mechanisms: (1) bounded parameters — application authenticates user and binds the value before the tool is called; (2) authenticated parameters — tool itself validates a signed JWT, extracts claims (user_id, email, issuer), and binds them, so the agent only needs to pass non-sensitive inputs like 'date'. Best practices surfaced: outcome-focused tool descriptions, separate read vs. write tools (auto-approve reads, confirm writes), actionable error messages so agents can self-retry, flat simple input structures.

## Relevance to YOLO loop

Applies to any production agent in our loop that touches user data or databases. Authenticated parameters let us move from permissive dev-time DB access to zero-trust production access without restructuring the agent's reasoning — only the tool configuration changes.

## Notes

MCP Toolbox is open-source and self-hosted; Google also offers a fully managed hosted version. EvalBench (also from Google) is their evaluation framework for MCP tools and skills — worth evaluating alongside Toolbox. Key anti-pattern highlighted: returning generic HTTP 404 errors instead of actionable retry-able errors wastes agent cycles.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-09-mcp-toolbox-authenticated-parameters` |
| Channel | aie |
| Video | [Build-Time vs. Run-Time: Why Dev Tools Fail in Production — Averi Kitsch & Prerna Kakkar, Google](https://www.youtube.com/watch?v=9R--1tg45Jg) |
| Published | 2026-09-09 |
| Ingested upstream | 2026-09-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

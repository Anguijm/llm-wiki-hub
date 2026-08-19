# Add AST-based taint-flow static analysis to CI/CD pipeline for MCP server code

> Back to [[experiments-index]]

Source: **[Before the Agent Calls: Source-level Findings from 100 MCP Servers](https://www.youtube.com/watch?v=2D5hLEwmC_M)** · mlops · 2026-08-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we gate MCP server deployments on an AST-based static scanner that traces taint flow from tool input parameters through to sink functions (exec, shell, file write, network calls) without sanitization, then we will catch command injection and input validation vulnerabilities before they ship, because a scan of 100 production MCP servers found 35 critical and 41 high vulnerabilities dominated by exactly these classes—all of which are detectable statically.

## What they did

Akash (Site Software, Agentic AI Foundation Ambassador) scanned 100 production TypeScript MCP servers using abstract syntax tree taint analysis, finding 445 total findings (35 critical, 41 high, 69 medium) across 11 servers for all critical issues. The dominant vulnerability class was input validation failures leading to command injection—the same pattern behind a real CVE on an NPM package with 437k+ downloads and the MCP Inspector incident. He demonstrated a CI/CD gate using his open-source tool that fails builds when taint flows from any tool parameter to an unsanitized sink, and noted this is a first gate only—dynamic attacks (prompt injection, tool poisoning, supply chain) require additional layers.

## Relevance to YOLO loop

Directly applicable to our MCP server CI pipeline: adding this gate before deployment ensures AI-generated MCP server code (which frequently contains unsanitized shell calls) doesn't introduce critical vulnerabilities into the agentic infrastructure our loop depends on.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-08-19-mcp-security-static-scan-cicd` |
| Channel | mlops |
| Video | [Before the Agent Calls: Source-level Findings from 100 MCP Servers](https://www.youtube.com/watch?v=2D5hLEwmC_M) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Replace direct MCP tool exposure with three meta-tools (search, get-schema, execute) to scale to 1,300+ tools without context overload

> Back to [[experiments-index]]

Source: **[500 Skills, Zero Fine-Tuning: LinkedIn's Playbook for AI Agents — Ajay Prakash, LinkedIn](https://www.youtube.com/watch?v=9wZpvF3QleU)** · aie · 2026-09-09

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we expose a search meta-tool, a get-schema meta-tool, and an execute meta-tool instead of listing all tools directly in the MCP context, then agents can dynamically discover and invoke the right tool from a library of thousands without degrading LLM performance, because MCP context degrades beyond 30-40 direct tools but keyword/tag search over an indexed catalog does not consume fixed context budget.

## What they did

AJ Prakash (LinkedIn) described the Contextual Agent Playbooks and Tools system built at LinkedIn. Engineers found coding agents hallucinated or stalled because they lacked context about LinkedIn's internal frameworks, databases, and infra. LinkedIn built an internal MCP server pre-installed on all laptops (auto-updated hourly) exposing: code search across 1,000+ repos, docs, Jira, Slack, and internal data platforms. They then hit the 30-40 tool MCP ceiling and solved it with three meta-tools: (1) search — find relevant playbooks/tools by keyword+tag; (2) get-schema — fetch full spec for a specific tool; (3) execute — run it. Playbooks are split into central (cross-repo) and local (repo-specific, checked in with the repo). The system includes a self-improving flywheel: agents are instructed to identify gaps and open PRs to update playbooks. Scale reached: 8,000 daily active users, 1,300+ tools, 600+ playbooks, used by engineers, PMs, designers, and TPMs.

## Relevance to YOLO loop

Directly solves the tool-scaling problem in our dev loop. As we add more MCP tools, the three-meta-tool pattern lets us grow the library without hitting context limits or forcing the model to reason over a huge flat tool list on every call. The local-vs-central playbook split also maps cleanly to our repo-specific vs. cross-project agent configurations.

## Notes

System instruction preconfigures every coding agent on how to use the three meta-tools efficiently. Self-learning flywheel: agents discover missing or incorrect playbooks and open PRs to fix them automatically. Pattern is model-agnostic — works with Cursor, Claude Code, GitHub Copilot. Key design principle: quality and reliability were first-class requirements from day one, not retrofitted.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-09-linkedin-contextual-agent-playbooks` |
| Channel | aie |
| Video | [500 Skills, Zero Fine-Tuning: LinkedIn's Playbook for AI Agents — Ajay Prakash, LinkedIn](https://www.youtube.com/watch?v=9wZpvF3QleU) |
| Published | 2026-09-09 |
| Ingested upstream | 2026-09-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

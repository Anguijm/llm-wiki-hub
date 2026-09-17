# Query the Aura Directory for Agent-Ready MCP and API Resources Instead of Relying on Web Search

> Back to [[experiments-index]]

Source: **[Rebuilding the web for agents — Liad Yosef, MCP Apps](https://www.youtube.com/watch?v=waI44NP1abk)** · aie · 2026-09-16

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we query the Aura agentic resource directory (which exposes ai-catalog.json files per domain and is AARD-compliant) to discover MCP servers and APIs for a given service, then our agents will find structured, agent-optimized integration endpoints faster and more reliably than scraping websites or using web search, because the directory is purpose-built for agent consumption.

## What they did

Liad Yosef (MCP Apps co-creator) described the shift from human-browsable websites to agent-accessible resources. He introduced MCP Apps as the spec enabling services to push UI components into chat interfaces (used by Claude, ChatGPT, Copilot, GitHub). He then described the discovery problem: agents need to find MCP servers and APIs, but web search (human SEO), custom registries (closed), and central registries (governance problems) are all insufficient. Aura built a directory that scans domains, generates ai-catalog.json files exposing MCP server URLs and API endpoints per domain (e.g., monday.com's MCP server), and exposes the directory itself as an AARD-compliant queryable endpoint so agents can discover resources for any domain via a natural language or structured query.

## Relevance to YOLO loop

When our dev loop agents need to integrate with external services (project management, CI/CD, data providers), querying an agent-ready directory first could replace manual MCP server discovery and reduce setup friction for new integrations.

## Notes

Aura directory is live and publicly queryable. ai-catalog.json is a standard by Anthropic, OpenAI, Google, MCP, A2A. Gemini does not yet support MCP Apps (as of talk date). Accessibility for agents mirrors accessibility for humans with vision disabilities — improving one improves the other.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-16-mcp-apps-agentic-web` |
| Channel | aie |
| Video | [Rebuilding the web for agents — Liad Yosef, MCP Apps](https://www.youtube.com/watch?v=waI44NP1abk) |
| Published | 2026-09-16 |
| Ingested upstream | 2026-09-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

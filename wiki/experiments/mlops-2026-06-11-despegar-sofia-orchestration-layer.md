# Keep an explicit orchestration layer (Chappie) above domain agents to prevent tool-routing failures as agent count grows

> Back to [[experiments-index]]

Source: **[Building MCP Before MCP Existed: Inside Despegar's Sofia Agent](https://www.youtube.com/watch?v=bowPBo0SNPQ)** · mlops · 2026-06-11

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we maintain a dedicated orchestration agent above specialized domain agents rather than letting the LLM route directly to all tools, then the system will be more reliable and debuggable because tool ambiguity (e.g., a new tool attracting all prompts incorrectly) can be caught and corrected at the orchestration layer without retraining every domain agent.

## What they did

Despegar described Sofia, a conversational travel agent with a brain called Chappie that routes to specialized category agents (flights, hotels, activities, cars, after-sales). They built a proprietary MCP-like protocol in 2024 before MCP existed to connect Chappie to agent tools. When they added a new tool with vague examples, Chappie started routing everything to it incorrectly—catching this was straightforward because the orchestration layer made routing observable. They are now layering standard MCP on top for new external connections while keeping their existing protocol. They acknowledged the orchestration layer may become unnecessary as models improve but consider it essential now for separation of concerns across very different use-case domains.

## Relevance to YOLO loop

Directly relevant to our multi-agent architecture decisions. The pattern of a routing orchestrator above specialized agents, with MCP for new external connections, is a concrete reference architecture we can validate.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-06-11-despegar-sofia-orchestration-layer` |
| Channel | mlops |
| Video | [Building MCP Before MCP Existed: Inside Despegar's Sofia Agent](https://www.youtube.com/watch?v=bowPBo0SNPQ) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

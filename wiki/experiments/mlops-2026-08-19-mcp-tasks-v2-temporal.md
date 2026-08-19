# Implement MCP Tasks v2 server-side durability using Temporal workflows

> Back to [[experiments-index]]

Source: **[Stateless, Yet Durable: MCP Tasks v2](https://www.youtube.com/watch?v=dGU0ibFPo9M)** · mlops · 2026-08-19

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we back MCP Tasks v2 long-running tool calls with Temporal workflows (using signals for elicitations and queries for status polling), then we can achieve durable, resumable agentic tasks that consume zero resources while idle, because Temporal's execution model persists workflow state externally and only activates compute when work is actually ready to proceed.

## What they did

Cornelia Davis (Temporal) implemented both client and server sides of the MCP Tasks v2 protocol using a purchase-order processing scenario. The invoice workflow was a Temporal workflow; elicitations were satisfied via workflow signals; status polling used workflow queries. She demonstrated that the stateless MCP Tasks v2 protocol maps cleanly onto Temporal's durable execution model, enabling long-running multi-step processes (seconds to weeks) with no resource consumption during idle periods. She also flagged that push-based notifications (vs. polling) are the next frontier and plan to present on that at MCPcon in October.

## Relevance to YOLO loop

Directly relevant to any YOLO loop step that involves long-running agent tasks: using Temporal as the durability layer means our agent orchestration survives restarts, scales horizontally, and only pays compute costs when actively processing.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-08-19-mcp-tasks-v2-temporal` |
| Channel | mlops |
| Video | [Stateless, Yet Durable: MCP Tasks v2](https://www.youtube.com/watch?v=dGU0ibFPo9M) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

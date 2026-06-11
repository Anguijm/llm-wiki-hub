# Let domain teams own and iterate their own agent flows on top of a central scaffold

> Back to [[experiments-index]]

Source: **[Building MCP Before MCP Existed: Inside Despegar's Sofia Agent](https://www.youtube.com/watch?v=bowPBo0SNPQ)** · mlops · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we provide a central agent scaffold with base flows and then delegate ownership of each domain flow to the team with domain expertise, then agent quality per domain will improve faster because domain experts encode tacit knowledge that a central AI team cannot replicate, while the scaffold ensures consistency.

## What they did

Despegar organized Sofia development so a small central team builds the initial version of each category flow (flights, hotels, cars, etc.) and then hands ownership to the corresponding product squad (which includes product, engineering, and UX). The hotels team owns the hotels flow and can modify it independently. Anyone in the company with supervision can create a new flow. This federated model meant Sofia scaled horizontally to cover nearly all categories quickly, with each squad deepening their vertical over time.

## Relevance to YOLO loop

Applicable when our team grows or when we want subject-matter experts to own specific agent capabilities. Defines the interface between a platform team (scaffold, orchestration, MCP) and feature teams (domain flows).

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-06-11-despegar-federated-agent-development` |
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

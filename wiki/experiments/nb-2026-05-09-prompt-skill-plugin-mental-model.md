# Audit workflows and classify each as prompt, skill, plugin, or MCP

> Back to [[experiments-index]]

Source: **[You're Wasting 40% Of Your AI Time On Something Fixable](https://www.youtube.com/watch?v=647pSnX5H_Y)** · NateBJones · 2026-05-09

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we audit repeated AI tasks and reclassify them from ad-hoc prompts into skills, plugins, or MCP connectors based on their reuse and tooling needs, then we will reduce wasted effort and build more stable agentic systems because prompts alone cannot carry permissions, tools, or repeatable structure.

## What they did

Speaker laid out a decision framework distinguishing four scaffold layers: prompts (one-off tasks), skills (reusable process docs in markdown), plugins (packaged workflows with tools and assets that need to travel), and MCP/connectors (access to external systems). He argued most people over-index on prompts and waste hours weekly that could be saved by promoting repeated work to skills or plugins. He also described hooks and scripts as deterministic verification layers that should not be replaced by the LLM.

## Relevance to YOLO loop

Directly applicable: we can audit our current YOLO loop prompts and CLAUDE.md conventions, promote stable patterns to skill files, package multi-tool flows as plugins, and add deterministic scripts for verification steps.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-05-09-prompt-skill-plugin-mental-model` |
| Channel | NateBJones |
| Video | [You're Wasting 40% Of Your AI Time On Something Fixable](https://www.youtube.com/watch?v=647pSnX5H_Y) |
| Published | 2026-05-09 |
| Ingested upstream | 2026-05-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

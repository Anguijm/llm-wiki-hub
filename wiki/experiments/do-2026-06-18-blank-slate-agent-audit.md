# Strip Agent Config to Zero and Rebuild Only What Is Missed

> Back to [[experiments-index]]

Source: **[Matt Pocock's Agentic Engineering Workflow (just copy him)](https://www.youtube.com/watch?v=nQwJVHCtDDY)** · do · 2026-06-18

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we delete all MCP servers, skills, plugins, and CLAUDE.md instructions and observe the bare agent, then we will identify which additions genuinely improve output versus which ones bloat the context window and degrade performance, because most practitioners over-configure and never measure the counterfactual.

## What they did

Matt Pocock's top actionable recommendation was to delete every skill, plugin, MCP server, CLAUDE.md, and agents.md file — returning to a completely blank configuration — then observe what the agent does in that baseline state. From there, layer additions back one at a time, prioritizing procedure skills over ability skills, and only restoring something if its absence is genuinely felt. He also advocated running agents AFK (away from keyboard) once the harness is stable.

## Relevance to YOLO loop

Our loop likely has accumulated config debt. This experiment gives us a fast, low-cost way to audit what is actually load-bearing in our agent setup versus what is noise, directly improving token efficiency and output consistency.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-06-18-blank-slate-agent-audit` |
| Channel | do |
| Video | [Matt Pocock's Agentic Engineering Workflow (just copy him)](https://www.youtube.com/watch?v=nQwJVHCtDDY) |
| Published | 2026-06-18 |
| Ingested upstream | 2026-06-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

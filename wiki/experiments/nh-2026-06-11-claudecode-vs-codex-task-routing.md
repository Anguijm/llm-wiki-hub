# Route tasks between Claude Code and Codex based on creative vs execution phase to improve output quality

> Back to [[experiments-index]]

Source: **[100 Hours Testing Claude Code vs ChatGPT Codex (honest results)](https://www.youtube.com/watch?v=RLjaUES9P8A)** · nh · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use Claude Code for planning, brainstorming, and problem-framing phases and Codex for execution, code review, and bug-finding phases, then overall project quality improves compared to using a single tool throughout, because Claude Code pushes back and surfaces edge cases while Codex obeys instructions precisely and excels at finding gaps in existing code.

## What they did

Nate spent 100+ hours testing both tools and built a feature/price comparison. He identified that both tools now share the same core feature set (local file edit, desktop app, VS Code extension, terminal, MCP support, YAML skill files, hooks, sub-agents, cloud delegation, plugin marketplace). Key differentiators: Claude Code feels more creative/opinionated/pushes back; Codex feels more obedient and sharp at code review. He recommended a hybrid workflow: Claude Code for planning → Codex for execution/review. He noted project portability (same GitHub repo works in both; swap CLAUDE.md → agents.md) and warned that the comparison was accurate as of mid-May 2026 and will drift.

## Relevance to YOLO loop

Introduces a two-tool routing strategy for the YOLO loop: Claude Code as the thinking/orchestration layer, Codex as the execution/review layer, with the same repo as the shared substrate.

## Notes

Codex included free in all ChatGPT plans. Claude Code requires paid plan. Both support YAML front-matter skill files. Migration: rename CLAUDE.md to agents.md, agent handles the rest. Review is dated mid-May 2026.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-06-11-claudecode-vs-codex-task-routing` |
| Channel | nh |
| Video | [100 Hours Testing Claude Code vs ChatGPT Codex (honest results)](https://www.youtube.com/watch?v=RLjaUES9P8A) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

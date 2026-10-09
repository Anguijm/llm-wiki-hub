# Run /doctor audit then delete 80%+ of Claude system prompt and CLAUDE.md rules

> Back to [[experiments-index]]

Source: **[Anthropic Engineers Just 10x'd Everyone's Claude Code](https://www.youtube.com/watch?v=oz2CwrPV2Rg)** · nh · 2026-10-09

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we strip accumulated rules from our CLAUDE.md and system prompt down to only the minimal context needed for current model generations, then task performance and eval scores will hold or improve because modern Claude models internalize many behaviors that older explicit rules were compensating for, and excess context degrades reasoning.

## What they did

Anthropic engineer Thoric published findings that removing over 80% of Claude Code's system prompt produced no measurable loss on evals for Opus 5, Claude 5, and 5.1. Nate replicated this by running /doctor to audit his own setup, identifying stale/duplicate rules accumulated from model-version-specific workarounds, and cleaning them. He also tested loading MCP tool definitions only on-demand, reporting an 85% token reduction and MCP eval score improvement from 49% to 74% (Opus 4) and 79.5% to 88.1% (Opus 4.5). He additionally used a constrained audit prompt ('find the smallest change, cite files, do not edit') to have Claude analyze his YouTube scripting workflow, revealing a missing sources.md handoff between outline and script skills.

## Relevance to YOLO loop

Directly actionable in our YOLO loop: run /doctor on our agent harness instructions, delete redundant rules, switch to lazy MCP loading, and re-run evals to confirm parity.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-10-09-minimal-context-claude` |
| Channel | nh |
| Video | [Anthropic Engineers Just 10x'd Everyone's Claude Code](https://www.youtube.com/watch?v=oz2CwrPV2Rg) |
| Published | 2026-10-09 |
| Ingested upstream | 2026-10-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

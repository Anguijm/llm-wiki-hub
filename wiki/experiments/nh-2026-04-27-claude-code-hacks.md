# Adopt a Structured CLAUDE.md + Slash Command Library for YOLO Loop Sessions

> Back to [[experiments-index]]

Source: **[32 Claude Code Hacks in 16 Mins](https://www.youtube.com/watch?v=jqoFP9QapXI)** · NateHerk · 2026-04-27

**Status:** `in_progress` · **Effort:** `low`

---

## Hypothesis

If we maintain a versioned CLAUDE.md project config and a curated set of custom slash commands for common YOLO loop operations (e.g., /plan, /review, /test-gen), then Claude Code sessions will produce more consistent, on-rails output with less prompt re-engineering per session, because Claude Code reads CLAUDE.md at session start and slash commands reduce instruction drift.

## What they did

Speaker ran through 32 Claude Code productivity tips including: using CLAUDE.md for persistent project context, defining custom slash commands for repeated workflows, using ultrathink prompting for complex reasoning, piping CLI output directly into Claude, using headless mode for scripted automation, and structuring multi-agent subagent calls within a single session.

## Relevance to YOLO loop

Directly improves the prompt layer of the YOLO loop. A well-tuned CLAUDE.md acts as the loop's system prompt equivalent, and slash commands standardize the most frequent loop operations without rebuilding context each time.

## Notes

[2026-04-29T08:05:00Z] Implemented at experiments/claude-code-hacks/. Adapters degrade to deterministic stubs without API keys, so the scaffold is runnable end-to-end. Promotion to tick queue is the next step.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-27 | `backlog` | Extracted from YouTube RSS |
|  | `` | Implemented as research-spike scaffold at experiments/claude-code-hacks/. See README.md for design and usage. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-04-27-claude-code-hacks` |
| Channel | NateHerk |
| Video | [32 Claude Code Hacks in 16 Mins](https://www.youtube.com/watch?v=jqoFP9QapXI) |
| Published | 2026-04-27 |
| Ingested upstream | 2026-04-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

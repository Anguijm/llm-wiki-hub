# Adopt Codex-as-planner + Claude Code-as-executor 3-phase build cycle

> Back to [[experiments-index]]

Source: **[Codex Just 10x’d Claude Code Projects](https://www.youtube.com/@NateHerk)** · nh · 2026-03-30

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we use Codex to generate a structured plan (iterating clarifying questions until 95% confidence) before handing to Claude Code for execution, then we reduce mid-build architectural rework because ambiguity is resolved upfront rather than surfaced in Gemini review after code is written.

## What they did

NateHerk demonstrated a 3-phase workflow with the official Codex plugin for Claude Code: (1) Planning — use Codex to ask clarifying questions iteratively until 95% confidence in a complete plan before any implementation begins. (2) Execution — copy the plan into Claude Code which implements systematically with full context. (3) Review — take the git diff back to Codex to verify implementation matches plan and catch missed edge cases. Benchmarks showed Opus 4.6 for deep implementation and GPT models for structured analysis.

## Relevance to YOLO loop

The YOLO loop goes from Gemini brainstorm directly to Claude build. Inserting a Codex planning step before execution could catch architectural issues before they become Gemini review bugs, directly reducing the Dark Factory retry loop count.

## Outcome

Implemented as 3-phase pipeline in cron: Phase 1 PLAN (idea filter + vertical outline + Gemini critique), Phase 2 BUILD (code from validated plan), Phase 3 REVIEW (6-angle council). Gemini validates the plan before any code is written — catches data model issues and missing edge cases.

## Notes

Partially overlaps with mlops-2026-03-27-specialized-agent-team (abstract specialized roles). This card is the concrete tool-specific implementation: Codex plan → Claude Code execute → Codex diff review.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `done` | Integrated into cron 3-phase pipeline |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-03-30-codex-plan-claude-execute` |
| Channel | nh |
| Video | [Codex Just 10x’d Claude Code Projects](https://www.youtube.com/@NateHerk) |
| Published | 2026-03-30 |
| Ingested upstream | 2026-04-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

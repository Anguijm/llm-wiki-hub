# Use /goal with a rubric file to continuously self-optimize the agentic OS skill and rule set

> Back to [[experiments-index]]

Source: **[How to Use /goal to Build a Self-Improving OS](https://www.youtube.com/watch?v=5xrjO38WUYY)** · mk · 2026-06-11

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we run /goal pointed at our .claude skill and rule folders with explicit cleanup, sharpening, and maintenance criteria in a rubric.md file, then our agentic OS will self-optimize by archiving stale skills, resolving rule contradictions, and improving skill quality against measurable criteria, because /goal's built-in judge agent operates from a separate model context and provides unbiased evaluation until the terminal condition is met.

## What they did

Mark demonstrated five /goal use cases for agentic OS maintenance. Clean: pointed /goal at a folder with 47 skills and 7 rule files; it reduced to 17 skills (30 archived) and 4 rules (3 contradictions resolved) in under 3 minutes. Sharpen: provided a rubric.md with evaluation criteria, then /goal iteratively rewrote a skill until all rubric criteria were met, using sub-agents to simulate the skill and score outputs. Revive: used /goal to detect half-built projects from transcripts and auto-generate missing skills (identified 3: Excalidraw canvas skill, LinkedIn post skill, content audit skill). Forge: /goal inferred missing skills from observed patterns (e.g., seeing LinkedIn transcripts with no associated skill). Maintain: combined /loop (every 30 min) + /goal to create a background cron job that continuously archives stale skills, checks rule relevance, and writes a maintenance log — all while the terminal session stays open.

## Relevance to YOLO loop

Directly applicable for keeping the YOLO loop's own skill library lean and current. The /loop + /goal combination for background maintenance is especially relevant for long-running projects where skill bloat accumulates silently and degrades agent performance.

## Notes

Backlog triage 2026-06-24 (owner-preference model). Self-optimizing skill/rule maintenance — matches the self-improving loop + skill audits.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-06-11-slash-goal-agentic-os-maintenance` |
| Channel | mk |
| Video | [How to Use /goal to Build a Self-Improving OS](https://www.youtube.com/watch?v=5xrjO38WUYY) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

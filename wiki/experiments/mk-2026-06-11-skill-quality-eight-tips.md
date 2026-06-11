# Audit skill library with eight quality heuristics and the Claude Code guide agent to eliminate dead weight

> Back to [[experiments-index]]

Source: **[Why 90% of Your Claude Skills Are Dead Weight](https://www.youtube.com/watch?v=cgWZcFKx2lQ)** · mk · 2026-06-11

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we apply eight skill-quality heuristics (cold-run test, description budget check, ask-user-input baked in, tonality rules, session rating prompt, reverse meta-prompting, wrong-primitive check, Claude Code guide agent audit) to our existing skill library, then we will reduce context window bloat, improve trigger reliability, and increase task completion rates because most skill failures stem from description truncation, naming collisions, and wrong primitive choice rather than model capability.

## What they did

Mark argued that most users accumulate dead-weight skills that (a) add 69–150 tokens each to every session context, (b) have descriptions truncated past a character limit so trigger conditions are invisible to Claude, (c) overlap with other skills causing wrong-skill-firing, and (d) should instead be rules, ClaudeMD entries, or CLI automations. He prescribed eight tips: 1) Run-cold test — invoke with a vague prompt to confirm the right skill fires without explicit naming. 2) Budget the description — keep it lean enough to not be truncated but specific enough to trigger correctly. 3) Bake in ask-user-input tool for prerequisite information gathering. 4) Hardcode anti-sycophancy and tonality rules for copy-related skills. 5) End sessions by asking the skill to rate itself out of 10 and explain the gap. 6) Reverse meta-prompting — after a messy successful session, ask Claude to distill the critical path into an updated skill. 7) Wrong-primitive check — decide if the task deserves a skill vs. rule vs. ClaudeMD vs. CLI hook. 8) Tag the Claude Code guide agent in an audit prompt to review any underperforming skill against current Anthropic best practices.

## Relevance to YOLO loop

Immediately actionable for auditing existing YOLO loop skills. The wrong-primitive heuristic and description-budget check are especially high-value for reducing silent context degradation that makes agents seem 'dumb' over long sessions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-06-11-skill-quality-eight-tips` |
| Channel | mk |
| Video | [Why 90% of Your Claude Skills Are Dead Weight](https://www.youtube.com/watch?v=cgWZcFKx2lQ) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

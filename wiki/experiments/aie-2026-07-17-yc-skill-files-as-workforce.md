# Encode Every Repeatable Workflow as a Skill File and Build a Compounding Organizational Library

> Back to [[experiments-index]]

Source: **[The New Physics of Business — Garry Tan, Y Combinator](https://www.youtube.com/watch?v=eBUyTS7SzV4)** · aie · 2026-07-17

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we treat every repeatable workflow as a skill file (one capability, one job, written clearly enough for an agent to execute) and accumulate these into a growing organizational library with a resolver/orchestrator layer, then each new task will leverage prior institutional knowledge automatically and output quality will compound over time, because the library acts as persistent organizational memory that prevents re-solving solved problems.

## What they did

Garry Tan (YC CEO) presented a framework mapping AI-native company architecture to traditional org structures: skill files = employees (one capability each), resolver tables = org charts (route tasks to the right skill), filing rules = internal process compliance, trigger evals = performance reviews. He reported a personal 400x productivity increase (conservative floor 8x after discounting verbosity) measured against his 14 usable lines/day baseline from 2013. He cited YC Winter 2025 batch data: 25% of companies had 95%+ AI-generated codebases; that batch became YC's fastest-growing and most profitable. He emphasized that the 2x vs. 100x difference between users of identical models comes entirely from how they 'wire the work'—not model quality. He introduced GBrain (open-source, MIT licensed) as a personal/company memory layer and described the library-plus-librarian architecture: a library of skill files, and a librarian agent that selects the right 3 files for any given task. He advocated never doing one-off work: every output should be 'skillified' before moving on.

## Relevance to YOLO loop

This is the canonical description of the YOLO loop's skill library architecture. Skill files, resolver tables, filing rules, and evals map directly to our loop primitives. The 'never do one-off work / always skillify' discipline is the key habit that makes the library compound. GBrain is worth evaluating as a memory layer.

## Notes

Garry explicitly said Claude Code is the Ferrari but Codex is a Honda that does 90% of it—use whatever, the concepts transfer. GBrain is open source at github. The 'founder still in the code library' point suggests the lead engineer should be the primary curator of the skill library, not delegating curation entirely. Key companies cited: Emergence AI (public launch to 9 figures ARR in 8 months, 15 people at $15M ARR), Retool ($60M ARR, ~40 people).

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-17 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-17-yc-skill-files-as-workforce` |
| Channel | aie |
| Video | [The New Physics of Business — Garry Tan, Y Combinator](https://www.youtube.com/watch?v=eBUyTS7SzV4) |
| Published | 2026-07-17 |
| Ingested upstream | 2026-07-17 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

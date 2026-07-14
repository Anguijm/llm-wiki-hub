# Write Eval Test Cases for Every Agent Skill Before Deploying It

> Back to [[experiments-index]]

Source: **[Don't Ship Skills Without Evals — Philipp Schmid, Google DeepMind](https://www.youtube.com/watch?v=0vphxNt4wyk)** · aie · 2026-07-14

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we write at least 5–20 eval prompts per skill (including negative tests) and run them as an ablation against the skill loaded vs. not loaded, then we will catch skills that hurt rather than help agent performance, because SkillBench data shows AI-generated skills can negatively impact performance and human-written skills above 500 lines degrade quality.

## What they did

Philipp Schmid (Google DeepMind) presented SkillBench findings: skills on average improve agent performance ~15%, but AI-auto-generated skills can hurt performance, and skills over 500 lines are problematic. He distinguished capability skills (temporary, retire when model improves) from preference skills (durable, encode team-specific workflows). He recommended: test outcomes not paths, use isolated runs to prevent agents cheating from prior context, run 3–6 trials per case due to non-determinism, test across multiple harnesses and models, and keep eval suites even after retiring a skill so you can detect when model regressions require reintroducing it. The eval harness is a simple JSON/YAML file plus a Python script.

## Relevance to YOLO loop

Our loop likely uses or generates skills/CLAUDE.md instructions. Before adding any new skill to the harness, running a small eval suite ensures we're not accidentally degrading the agent's baseline performance — critical for a loop that runs autonomously overnight.

## Notes

Philipp recommended Matt's 'Writing Great Skills' guide on GitHub as a companion resource.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-14-skill-evals-before-ship` |
| Channel | aie |
| Video | [Don't Ship Skills Without Evals — Philipp Schmid, Google DeepMind](https://www.youtube.com/watch?v=0vphxNt4wyk) |
| Published | 2026-07-14 |
| Ingested upstream | 2026-07-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

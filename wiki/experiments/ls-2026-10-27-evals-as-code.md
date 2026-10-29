# Turn harness requirements into evals-as-code with a golden set

> Back to [[experiments-index]]

Source: **[How Anthropic ships the #1 LLM in the World — with Katelyn Lesse and Angela Jiang](https://www.youtube.com/watch?v=MRQTlwcW-aQ)** · ls · 2026-10-27

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we formalize each Claude Code skill or hook requirement as an automated eval backed by a small human-reviewed golden dataset, then regressions and benchmark drift will be caught earlier, because requirements become executable tests.

## What they did

The guests described treating AI product engineering as empirical research. Feature requirements become automated eval benchmarks, and frontier models generate synthetic test cases. Human reviewers give binary preference scores that produce Elo ratings, which Claude uses to update system prompts. Human-reviewed golden datasets are kept to catch subtle benchmark drift. They also described using effort control, defaulting Claude Code to medium and toggling high for complex multi-file work.

## Relevance to YOLO loop

high: Evals-as-code and golden sets are a verification-loop pattern that could harden skills, hooks and councils.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-28 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `ls-2026-10-27-evals-as-code` |
| Channel | ls |
| Video | [How Anthropic ships the #1 LLM in the World — with Katelyn Lesse and Angela Jiang](https://www.youtube.com/watch?v=MRQTlwcW-aQ) |
| Published | 2026-10-27 |
| Ingested upstream | 2026-10-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

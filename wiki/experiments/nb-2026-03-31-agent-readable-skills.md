# Restructure program.md as agent-readable skill files

> Back to [[experiments-index]]

Source: **[Anthropic, OpenAI, and Microsoft Just Agreed on One File Format. It Changes Everything.](https://www.youtube.com/watch?v=0cVuMHaYEHE)** · nb · 2026-03-31

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we decompose program.md into discrete, focused skill files (build-skill.md, review-skill.md, test-skill.md) with specific descriptions and methodology sections, then the builder agent produces higher quality output because each skill provides focused context instead of one monolithic prompt.

## What they did

Nate described skills as markdown files with a Description (tells agent when to trigger) and Methodology (instructions + reasoning). Best practices: specific descriptions with trigger phrases, under 150 lines per skill, reasoning over steps, lean design with 80% effort on description. Agent-first design means hundreds of skill calls per run.

## Actionable steps

- Audit program.md for distinct skill boundaries (brainstorm, build, test, review, log)
- Extract each into a separate .md skill file with description + methodology
- Keep each under 150 lines
- Test: does the agent trigger the right skill at the right time?

## Success metric

Builder agent autonomously selects and chains the correct skill for each phase without human prompting.

## Relevance to YOLO loop

program.md is already ~200 lines and growing. Decomposing into skills would make each phase more focused and allow the Tick-Tock system to load only the relevant skill.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

Created skills/ directory with 6 skill files: 00-bootstrap (session init + routing), 10-tick (YOLO build), 11-tock (Deck flagship), 20-review (Gemini code review), 30-phase4 (YouTube pipeline), 40-refine (project refinement). Each under 150 lines with Description, Methodology, Input/Output contracts. program.md updated to reference skills system.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-03-31 | `in_progress` | Decomposing program.md into skill files + harness runner |
| 2026-03-31 | `done` | 6 skill files created, program.md updated |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-03-31-agent-readable-skills` |
| Channel | nb |
| Video | [Anthropic, OpenAI, and Microsoft Just Agreed on One File Format. It Changes Everything.](https://www.youtube.com/watch?v=0cVuMHaYEHE) |
| Published | 2026-03-31 |
| Ingested upstream | 2026-03-31 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

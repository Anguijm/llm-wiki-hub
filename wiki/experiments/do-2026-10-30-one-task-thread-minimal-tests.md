# Trial one-task-per-thread, repro-first bugfixes, and regression-only tests

> Back to [[experiments-index]]

Source: **[High-Level Agentic Engineering with David Ondrej](https://www.youtube.com/watch?v=F8rc-ULd4_4)** · do · 2026-10-30

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we enforce one task per agent thread, require end-to-end bug reproduction before any fix, and allow tests only for recurring regression classes, then agent output will be cleaner and builds faster because context stays uncontaminated and the repo avoids test bloat.

## What they did

Ondrej runs each agent thread in an isolated cloud sandbox with a strict one-task-per-thread policy. Agents reproduce reported bugs by simulation before writing code, then implement the fix, run type checks, and produce UI screenshots before committing. He forbids bloated unit test suites, claiming over 90% of agent-written tests are useless, and reserves tests for recurring regression classes. He also runs scheduled background loops that audit recent commits for unintended side effects.

## Relevance to YOLO loop

high: Gives concrete harness rules (thread isolation, repro-first, test policy, scheduled commit audits) for Claude Code practice.

## Notes

Claim that over 90% of agent tests are useless is the speaker's assertion; measure on our own repos.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-30 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-10-30-one-task-thread-minimal-tests` |
| Channel | do |
| Video | [High-Level Agentic Engineering with David Ondrej](https://www.youtube.com/watch?v=F8rc-ULd4_4) |
| Published | 2026-10-30 |
| Ingested upstream | 2026-10-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

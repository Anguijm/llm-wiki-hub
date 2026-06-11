# Add automatic post-build reflection that writes back to agent memory

> Back to [[experiments-index]]

Source: **[How to Fix Your Agent's Amnesia: Lessons from Building a Self-learning Agent]()** · mlops · 2026-04-02

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If the build agent automatically reflects after each build (what went well, what went wrong, what to do differently) and writes structured entries to its memory, then the memory grows organically without human curation because the agent maintains its own knowledge base.

## What they did

The self-learning agent approach implies a write-back loop: agent acts, evaluates outcome, writes learnings to persistent memory, retrieves them in future sessions.

## Actionable steps

- Add a post-build reflection step to program.md: after tests pass, agent writes 2-3 learnings
- Structure the write-back format: [project] [pattern] [outcome] [recommendation]
- Store in a machine-readable format (JSON or tagged markdown) for retrieval
- After 10 builds, review whether auto-generated learnings are useful or noisy

## Success metric

Agent auto-generates useful learnings entries after 80% of builds; at least 3 entries get referenced in future builds.

## Relevance to YOLO loop

Currently learnings.md is human-curated. Automating the write-back loop would make the system truly self-learning.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

Added mandatory Phase 4: REFLECT step to cron. Every tick build appends structured reflection to learnings.md (KEEP/IMPROVE/INSIGHT/COUNCIL scores). Compounds learning automatically.

## Notes

Title-only inference. Companion to self-learning-agent-memory — this is the write side, that is the read side.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `backlog` | Ingested from Phase 4 YouTube pipeline — title-only inference |
| 2026-04-04 | `done` | REFLECT step added to cron prompt |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-04-03-self-learning-feedback-loop` |
| Channel | mlops |
| Published | 2026-04-02 |
| Ingested upstream | 2026-04-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

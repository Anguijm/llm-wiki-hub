# Build a skill-audit skill that finds and resolves conflicts across your existing skill set

> Back to [[experiments-index]]

Source: **[I Stopped Installing Claude Skills. Here's What I Do Instead.](https://www.youtube.com/watch?v=up0Bsf3f0Xc)** · nb · 2026-08-02

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we create a dedicated meta-skill that audits all installed agent skills for conflicts, overlaps, and vague descriptions, then overall agent output quality will improve because the AI currently averages across conflicting instructions, producing dull results that worsen as the skill set grows.

## What they did

Nate argued that most people treat skills like Pokémon cards — additive collection without understanding interactions. He explained that skills load lazily (name/description first, full content only when the task matches), so vague descriptions cause skills to misfire or never fire. He distinguished skills from apps: no trust certificate, no guaranteed interoperability. His solution was to stop randomly installing skills and instead: (1) write skills explicitly for agents as the primary audience while keeping them human-readable, (2) use a meta-skill that audits the full skill inventory, identifies conflicts, and surfaces resolution options for the human to decide. He framed unresolved skill conflicts as the root cause of degrading AI performance over time.

## Relevance to YOLO loop

The YOLO loop accumulates CLAUDE.md entries, custom instructions, and tool definitions over time. This experiment directly addresses skill/instruction bloat and conflict — running an audit skill before each major loop iteration could prevent compounding instruction debt.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-08-02-skill-audit-conflict-resolution` |
| Channel | nb |
| Video | [I Stopped Installing Claude Skills. Here's What I Do Instead.](https://www.youtube.com/watch?v=up0Bsf3f0Xc) |
| Published | 2026-08-02 |
| Ingested upstream | 2026-08-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

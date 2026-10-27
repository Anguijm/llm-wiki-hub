# Audit and prune installed Claude skills

> Back to [[experiments-index]]

Source: **[Anthropic Just Donated Claude Skills. Here's What to Delete.](https://www.youtube.com/watch?v=2IPR6F3cQ_I)** · mk · 2026-10-23

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run a read-only audit of all registered Claude skills and delete or compress the redundant ones, then session context bloat and wrong-skill selection drop because fewer overlapping instructions are loaded.

## What they did

Mark Kashef ran a read-only audit prompt over all registered skills that generated an interactive single-file HTML report with heat maps, the top 10 used skills and merge/delete candidates. His secondary Mac mini had 374 skills, 70 flagged for deletion and 46 mergeable into 6 compound skills. He compressed the 330-word /grill-me skill into one line in AGENTS.md. He moves rarely used skills to an inactive directory for just-in-time loading. He keeps permanent skills only for deterministic code, private context, and complex APIs without a native MCP. He warns that over 50 skills bloats every session's context.

## Relevance to YOLO loop

high: Pruning skills and context bloat applies directly to the YOLO loop's skill and memory setup.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-26 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-10-23-skills-audit-prune` |
| Channel | mk |
| Video | [Anthropic Just Donated Claude Skills. Here's What to Delete.](https://www.youtube.com/watch?v=2IPR6F3cQ_I) |
| Published | 2026-10-23 |
| Ingested upstream | 2026-10-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

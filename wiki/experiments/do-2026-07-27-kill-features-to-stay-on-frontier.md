# Audit and prune agent tooling features that model capability improvements have made redundant

> Back to [[experiments-index]]

Source: **[Agentic Engineering, explained by a 10x developer](https://www.youtube.com/watch?v=FU5_kpTAVDo)** · do · 2026-07-27

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we periodically audit our agent scaffolding and remove features that newer model capabilities now handle natively, then the system becomes simpler and faster to iterate on because accumulated scaffolding complexity compounds maintenance cost and slows adaptation to model frontier shifts.

## What they did

Torsten described AMP's explicit policy of killing features when the frontier moves past them — they removed their VS Code extension when editor-centric workflows became obsolete, and continuously delete features visible on amcode.com/news. He frames this as optimizing the company, codebase, and product to shed weight quickly rather than accumulating technical debt from legacy UX assumptions.

## Relevance to YOLO loop

Applies directly to our dev loop scaffolding: we should schedule a recurring review of prompt engineering workarounds, custom parsers, and tool wrappers that exist only because an older model needed them — and remove them when a current model handles the case natively.

## Notes

Torsten's framing: retaining legacy features keeps users who resist change, creating an echo chamber that slows frontier adoption. The cost of deletion is short-term churn; the benefit is long-term agility.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-07-27-kill-features-to-stay-on-frontier` |
| Channel | do |
| Video | [Agentic Engineering, explained by a 10x developer](https://www.youtube.com/watch?v=FU5_kpTAVDo) |
| Published | 2026-07-27 |
| Ingested upstream | 2026-07-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

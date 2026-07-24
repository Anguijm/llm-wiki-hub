# Split AIOS context into expertise (stable) and situational (project-specific) layers to reduce bloat

> Back to [[experiments-index]]

Source: **[5 Hacks to Instantly Level Up Your AI OS](https://www.youtube.com/watch?v=Ek1NBfnnTH0)** · nh · 2026-07-24

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we physically separate stable expertise knowledge (how we work, our processes, our frameworks) from situational context (active client projects, current engagement details), then agent retrieval accuracy improves and bloat-induced failures decrease because the agent can load only the situational layer for task execution while keeping the expertise layer as a standing background.

## What they did

Described a two-layer context architecture: 'expertise context' holds evergreen knowledge about how the business operates (methodologies, templates, general rules) while 'situational context' holds time-bound engagement data (contract dates, project scope, deliverables for a specific client). For a client project, internal knowledge (discovery calls, pricing, contract date) lives in the main AIOS, but actual deliverables the client would see are kept in a separate, segmented repo that the AIOS still has context awareness of but doesn't own entirely. Argued this prevents bloat as the AIOS scales because situational data stays bounded per engagement.

## Relevance to YOLO loop

As the YOLO loop accumulates client projects and skills, a flat context structure will hit the bloat failure mode. Implementing a two-layer split (a stable skills/wiki layer + a per-engagement situational layer loaded dynamically) would let the agent scale to many concurrent projects without degrading retrieval quality.

## Notes

Pairs naturally with the audit skill experiment—the audit should specifically check whether situational data has leaked into the expertise layer or vice versa. Speaker notes this is unsolved at team/department sync level; single-user implementation is the prerequisite.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-07-24-expertise-vs-situational-context-split` |
| Channel | nh |
| Video | [5 Hacks to Instantly Level Up Your AI OS](https://www.youtube.com/watch?v=Ek1NBfnnTH0) |
| Published | 2026-07-24 |
| Ingested upstream | 2026-07-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

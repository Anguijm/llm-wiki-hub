# Precompute user context profiles offline before agent queries

> Back to [[experiments-index]]

Source: **[From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com](https://www.youtube.com/watch?v=Btk8wDUVs74)** · aie · 2026-07-23

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we build user/project context profiles offline and ahead of time (rather than assembling context at query time), then agent responses to open-ended prioritization questions will be more accurate and grounded because the semantic relationships and patterns between data points are computed when time is not a constraint, not under latency pressure at serve time.

## What they did

Monday.com's Sidekick team built a two-layer offline processing pipeline ('fast' and 'slow') that ingests breadcrumbs from all connected sources (boards, emails, Slack, calendar, meeting transcripts, action items) and precomputes a structured user profile (role, active projects, work patterns, hours per day) plus a short-window action-item layer (recent commitments, unanswered emails). At serve time, only a thin slice of logic reruns against live data to verify recency; the rest falls back to the last verified snapshot. This means the agent receives a pre-reasoned context model rather than raw records, enabling it to answer 'what should I focus on right now?' with grounded, personalized output.

## Relevance to YOLO loop

In our dev loop the agent currently assembles context at query time from raw files and git state. This pattern suggests we should add an offline indexing step that precomputes a developer context profile (active branches, open PRs, recent decisions, outstanding TODOs, meeting notes) so the agent starts each session with a pre-reasoned snapshot rather than reconstructing meaning from scratch on every invocation.

## Notes

Key architectural insight: isolate sources so a bad feed cannot corrupt the whole model; degrade gracefully rather than fail hard. The 'slow' layer builds durable profile signals; the 'fast' layer covers the recent activity window. Both run offline. This maps directly to separating our long-term project memory from the short-term session context in the YOLO loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-23-offline-context-precomputation` |
| Channel | aie |
| Video | [From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com](https://www.youtube.com/watch?v=Btk8wDUVs74) |
| Published | 2026-07-23 |
| Ingested upstream | 2026-07-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

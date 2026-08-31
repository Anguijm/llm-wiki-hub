# Run a four-stage AI adoption audit (Foundation → Activation → Adoption → Expansion) before adding new agent capabilities

> Back to [[experiments-index]]

Source: **[Where $10M-$150M Companies Get Stuck with AI (and how to fix it)](https://www.youtube.com/watch?v=-kGPKdX7gZ8)** · st · 2026-08-30

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we gate new agent feature work behind a structured four-stage readiness audit, then we will avoid the common failure mode of jumping straight to agent expansion before people actually use existing tools habitually, because skipping stages forces teams to restart from scratch after 6+ months of wasted effort.

## What they did

Talebi ran 44 AI workshops across 14 mid-size companies ($10M–$150M revenue) and identified four sequential bottlenecks. Stage 1 Foundation: no company-managed AI tool exists and no single person owns the rollout—shadow AI proliferates and there is zero visibility. Fix: pick one vendor, name one owner. Stage 2 Activation: access exists but nobody has actually used the tool; people lack a first concrete skill. Fix: run a live hands-on session where every employee builds one personally useful prompt or workflow. Stage 3 Adoption: one-time use doesn't become habit; time savings are not reclaimed. Fix: track reclaimed hours per person (target 5–20 h/week), share wins publicly, remove busy-work so strategic thinking fills the gap. Stage 4 Expansion: agents can't reach necessary systems, SOPs haven't been rewritten, and human-review throughput can't keep up with agent volume. Fix: build or swap to agent-friendly connectors (e.g. switching SharePoint to Google Drive so Claude can write files), redesign SOPs, and codify judgment into automated evals to reduce mandatory human-in-the-loop review. He also provided a free 10-question AI scorecard that outputs a company score, top blocker, and 1–3 next steps.

## Relevance to YOLO loop

Maps directly to our dev loop's prioritization gate: before building new agent integrations (Expansion work), confirm the team is genuinely at Stage 3 adoption. If daily active usage and reclaimed-hour metrics are flat, fix that first rather than adding complexity. The connector-compatibility check (can the agent read AND write to our systems?) is an immediate pre-build checklist item.

## Notes

Talebi specifically calls out SharePoint→Google Drive migration as a practical example of changing systems to unblock agent write-access. Also notes that as agent output volume scales, automated evals become the critical scaling mechanism for human review—aligns with NateBJones card on passing conditions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-30 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `st-2026-08-30-four-stage-ai-adoption-roadmap` |
| Channel | st |
| Video | [Where $10M-$150M Companies Get Stuck with AI (and how to fix it)](https://www.youtube.com/watch?v=-kGPKdX7gZ8) |
| Published | 2026-08-30 |
| Ingested upstream | 2026-08-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

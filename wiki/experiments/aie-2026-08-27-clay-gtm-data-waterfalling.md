# Implement waterfall data enrichment across multiple providers to maximize field coverage for agent context

> Back to [[experiments-index]]

Source: **[GTM Engineering: The Technical Bits — Everett Berry, Clay](https://www.youtube.com/watch?v=UhCY231d0FQ)** · aie · 2026-08-27

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we layer multiple data providers sequentially (waterfall) rather than relying on a single enrichment source, then agents will have more complete account and contact records to reason over, because Clay's analysis shows no single vendor provides complete coverage — e.g., using only one provider for phone numbers yields ~50% coverage vs. near-complete coverage when waterfalling across multiple providers.

## What they did

Speaker (Clay GTM engineering lead) described four pillars of GTM engineering: data (creating a perfect virtual copy of the market), enrichment (waterfalling across multiple third-party providers to fill gaps, with evals to compare provider accuracy), personalization (LLM-powered research and copy generation per account), and execution (agent-driven sequencing with domain reputation management and multi-channel coordination). He emphasized that accounts exist in constant state of change and require selective, event-driven data refresh rather than full periodic updates due to cost.

## Relevance to YOLO loop

Applicable to how we enrich context for our agents. When agents need external information (package docs, API specs, company data), implementing a waterfall — try source A, if missing try source B — reduces null context failures without requiring a single comprehensive source.

## Notes

Hardest problem identified: interface between human and agent — rep may not know what agent did, or may disagree. Design explicit handoff notifications into any automation.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-27-clay-gtm-data-waterfalling` |
| Channel | aie |
| Video | [GTM Engineering: The Technical Bits — Everett Berry, Clay](https://www.youtube.com/watch?v=UhCY231d0FQ) |
| Published | 2026-08-27 |
| Ingested upstream | 2026-08-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

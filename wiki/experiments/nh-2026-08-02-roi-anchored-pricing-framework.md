# Price AI builds as ~10-13% of annualized cost savings before quoting any number

> Back to [[experiments-index]]

Source: **[18 Months of Pricing AI Automations in 21 Mins](https://www.youtube.com/watch?v=Lg5TYWPSg6M)** · nh · 2026-08-02

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we calculate the client's annualized cost of the problem being solved (hours × wage × 52) and price the build at 10-13% of that number before any negotiation, then close rates and client satisfaction will improve because the client's own arithmetic justifies the price as a ~7-10x ROI, making it hard to decline.

## What they did

Nate walked through a real appointment-setting agent sale: 20 leads/week × 1 hour each × $40/hour × 52 weeks = $41,600 annualized cost. He priced the build at ~13% of that ($5,500), giving the client a 7.5x return. He targets 10x as the 'golden rule' and accounts for the gap via projected volume increases. He separates the build fee from a flat $400/month maintenance retainer (covering only keeping existing functionality working, not new features), and always puts API/token costs on the client's card with an estimated monthly run cost in the proposal. He also recommends capturing baseline metrics upfront and following up at 1, 2, and 3 months to prove transformation — which he admits he failed to do on this project, costing him upsell leverage.

## Relevance to YOLO loop

When scoping YOLO loop automation projects for clients or internal stakeholders, this framework provides a defensible, arithmetic-based price anchor that replaces gut-feel quoting.

## Notes

Key formula: annualized_cost = weekly_hours × hourly_rate × 52; build_price = annualized_cost × 0.10-0.13. Maintenance retainer is separate and flat. Testing costs (~$1-3k) baked into build price.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-02-roi-anchored-pricing-framework` |
| Channel | nh |
| Video | [18 Months of Pricing AI Automations in 21 Mins](https://www.youtube.com/watch?v=Lg5TYWPSg6M) |
| Published | 2026-08-02 |
| Ingested upstream | 2026-08-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

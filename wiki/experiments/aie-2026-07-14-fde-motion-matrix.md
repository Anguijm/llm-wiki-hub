# Use a Digital-Maturity × Product-Customization Matrix to Scope FDE Engagements

> Back to [[experiments-index]]

Source: **[Forward Deployed Engineering at Cursor — Pauline Brunet](https://www.youtube.com/watch?v=APqXGyCoGW4)** · aie · 2026-07-14

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we map each customer engagement on a 2×2 of (customer digital maturity) × (product configurability) before deploying FDE resources, then we will focus high-cost FDE effort only where it creates maximum leverage (low-maturity + high-customization), because self-service documentation covers high-maturity/low-customization customers and wastes FDE capacity on traditional SaaS deployments.

## What they did

Pauline Brunet (Cursor, global FDE lead) described building Cursor's forward deployed engineering function. She presented a 2×2 matrix: low maturity + low customization = traditional SaaS deploy (not FDE); high maturity + low customization = self-service + docs; high maturity + high customization = FDE as accelerator/adviser; low maturity + high customization = embedded transformation (core FDE). She recommended keeping engagement scope directional rather than fixed (e.g., '6 weeks to automate X process') to allow pivoting as customer systems are discovered, always measuring ROI as revenue increase / cost decrease / risk mitigation, and leaving documentation artifacts behind. She also stressed hiring only A-players for FDE because B-players hire C-players.

## Relevance to YOLO loop

Relevant if we are deploying agent loop infrastructure for external teams or clients — the matrix helps us decide when to hand off a self-service template vs. embed and customise.

## Notes

Primarily an org/go-to-market framework; lower technical experiment value unless we are doing client deployments.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-14-fde-motion-matrix` |
| Channel | aie |
| Video | [Forward Deployed Engineering at Cursor — Pauline Brunet](https://www.youtube.com/watch?v=APqXGyCoGW4) |
| Published | 2026-07-14 |
| Ingested upstream | 2026-07-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

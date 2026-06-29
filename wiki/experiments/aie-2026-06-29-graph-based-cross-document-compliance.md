# Replace document-level validation with graph-based cross-document entity correlation for anomaly detection

> Back to [[experiments-index]]

Source: **[AI-Driven Multi-Document Correlation for Financial Compliance - Varsha Shah, Independent](https://www.youtube.com/watch?v=Iwe_RY-fYgI)** · aie · 2026-06-29

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we build an entity correlation engine that connects records across multiple document types (payroll, tax, procurement, transactions) into a unified graph and runs a probabilistic risk model over the connected data rather than validating each document independently, then we will surface fraud patterns and compliance risks that are invisible in per-document analysis, because sophisticated fraud exploits subtle inconsistencies across systems that only become apparent when relationships between documents are visible.

## What they did

Varsha Shah (TCS/Microsoft) presented a three-component framework evaluated on ~3 million financial records across four jurisdictions: (1) Entity Correlation Engine — links entities across payroll, tax, procurement, and financial systems into a unified relationship graph; (2) Adaptive Probabilistic Risk Model — scores connected patterns using multiple risk signals rather than single-rule alerts, learns from audit outcomes (confirmed fraud strengthens detection patterns, false positives refine scoring); (3) Cross-Jurisdictional Normalization Layer — standardizes currencies, tax structures, and reporting standards so risk is evaluated consistently across regions. The framework includes a continuous learning cycle where each completed audit improves future detection accuracy, shifting compliance from reactive (post-audit) to proactive (predictive risk identification).

## Relevance to YOLO loop

If our loop generates artifacts across multiple systems (code, tests, docs, deployment configs, monitoring alerts), the same cross-artifact correlation pattern could surface inconsistencies — e.g. a test that passes but contradicts a spec that contradicts a deployment config. The probabilistic risk scoring and continuous learning pattern is broadly applicable to any multi-document consistency problem.

## Notes

Framework uses synthetic data for the public benchmark; production validation is the stated next step. The core insight — risk lives between documents, not within them — applies beyond finance to any domain with multiple interdependent artifact types. The adaptive learning loop (audit outcomes feed back into risk scoring) is what makes this scale without manual rule updates.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-29-graph-based-cross-document-compliance` |
| Channel | aie |
| Video | [AI-Driven Multi-Document Correlation for Financial Compliance - Varsha Shah, Independent](https://www.youtube.com/watch?v=Iwe_RY-fYgI) |
| Published | 2026-06-29 |
| Ingested upstream | 2026-06-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Map agent capabilities to specific SDLC stages rather than deploying generically

> Back to [[experiments-index]]

Source: **[How Forward Deployed Engineering is done at Cognition — Jia Wu](https://www.youtube.com/watch?v=RVxym6mmIns)** · aie · 2026-07-28

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we explicitly map which agent capabilities address which SDLC stages (feature building, testing, code review, deployment, maintenance) rather than deploying agents as general-purpose tools, then we will see higher PR acceptance rates and measurable ROI per stage, because coding is only ~20% of the problem and the real value is in test, review, and maintenance automation.

## What they did

Jia Wu described Cognition's FDE motion as explicitly mapping Devin's capabilities to customer problem stages in the SDLC. She noted that coding itself is 'mostly solved' and represents only ~20% of the problem — the harder parts are testing, reviewing, deploying, and maintaining code. Cognition deployed Devin for targeted migrations (e.g., ETL migration at Nubank with 50 engineers cut to 1/3 timeline, COBOL tax ID system migration at a Latin American bank with half the effort, and 10x weekly PR output at Built card).

## Relevance to YOLO loop

Our YOLO loop should be decomposed by SDLC stage with per-stage evals. This framing suggests we should measure agent contribution at test generation, PR review, and maintenance separately rather than only at code generation.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-28-cognition-sdlc-capability-mapping` |
| Channel | aie |
| Video | [How Forward Deployed Engineering is done at Cognition — Jia Wu](https://www.youtube.com/watch?v=RVxym6mmIns) |
| Published | 2026-07-28 |
| Ingested upstream | 2026-07-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

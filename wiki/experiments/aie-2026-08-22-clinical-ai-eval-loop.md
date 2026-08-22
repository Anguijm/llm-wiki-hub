# Build an evolving per-output judge that assembles context from expert corrections rather than a static rubric

> Back to [[experiments-index]]

Source: **[Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](https://www.youtube.com/watch?v=yqF6XhzbWBk)** · aie · 2026-08-22

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we replace a static rubric judge with one that dynamically assembles per-output context (nearest judged examples, applicable expert corrections, relevant guidelines) and continuously feeds new failure modes back into the judge, then eval catch rates improve dramatically because the judge develops domain taste rather than guessing generic criteria.

## What they did

Seb showed that 1-in-20 production clinical AI notes contain serious errors, mostly silent omissions rather than hallucinations, and that off-the-shelf rubric judges miss most of them. His solution: a 'Discovery' module that surfaces new failure modes from real outputs, an expert correction capture loop, and a per-output judge that pulls nearest-case memory, applicable corrections, and guidelines at inference time. Benchmarked on the same note set, this loop-based judge substantially outperformed both a frontier rubric judge and a deeper static system.

## Relevance to YOLO loop

Directly applicable to our eval pipeline: instead of freezing one eval rubric, we should capture free-form expert comments on real outputs, cluster them into failure modes, and feed those back as context for each new eval call. Start with free-form comments — that's the raw material.

## Notes

Company is Composo. Key starting action: have experts leave free-form comments on real outputs rather than scoring against a predefined rubric. Evaluation must be continuous, not a one-time artifact.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-22-clinical-ai-eval-loop` |
| Channel | aie |
| Video | [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](https://www.youtube.com/watch?v=yqF6XhzbWBk) |
| Published | 2026-08-22 |
| Ingested upstream | 2026-08-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

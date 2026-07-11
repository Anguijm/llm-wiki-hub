# Add explicit boundary contracts (voice, verification, deduplication, schema) at each agent handoff to block polished-but-wrong artifacts

> Back to [[experiments-index]]

Source: **[Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD - Sumaiya Shrabony](https://www.youtube.com/watch?v=WLXxTaPagA8)** · aie · 2026-07-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we implement named gate contracts at each inter-agent handoff that check output shape, domain voice compliance, claim verification trails, and deduplication against a history vault — and make gates hard-block (not warn) before artifacts advance — then we catch the dangerous class of failures (outputs that look correct but violate constraints) before they propagate downstream, because polished-looking bad outputs are harder to catch than obvious errors.

## What they did

Sumaiya runs a 19-skill Claude Code agent content system with 7 handoffs (scheduler → command → research → content → production → verifier → reviewer → output). She identified five CI/CD primitives she had independently reinvented: regression testing (output shape checks), CI monitoring (scheduled task alerts), contract testing (schema boundary validation), staging environments (pre-publish checkpoints), and audit trails (per-gate failure logs). She demoed three failure modes — voice drift (generic AI language), missing verification (unverified statistics), and hook duplication (recycled opening angles) — showing that a 'knife mode' (no gates) saves all three while 'guarded mode' (gates active) blocks all three. Each gate writes an audit record with which contract failed and why, critical for diagnosing 2am scheduled run failures.

## Relevance to YOLO loop

Directly hardens the YOLO loop's output validation layer — prevents confident-sounding but wrong outputs from being treated as done, which is the primary failure mode in autonomous multi-step pipelines.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-11-agent-output-gate-contracts` |
| Channel | aie |
| Video | [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD - Sumaiya Shrabony](https://www.youtube.com/watch?v=WLXxTaPagA8) |
| Published | 2026-07-11 |
| Ingested upstream | 2026-07-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

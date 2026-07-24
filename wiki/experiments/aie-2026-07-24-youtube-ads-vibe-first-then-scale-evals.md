# Start evals with manual vibing on small golden sets before investing in scaled rater infrastructure

> Back to [[experiments-index]]

Source: **[How Evals and Prompts Shape Agent Behavior — Preetika Bhateja & Daniel Bump, YouTube Ads](https://www.youtube.com/watch?v=xyL2Ltkh-SA)** · aie · 2026-07-24

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we begin eval development with intuition-based manual review of a small curated set rather than immediately building scaled automated raters, then we iterate faster in early development because failure patterns are obvious at small scale, prompt tweaks have larger gains, and the learnings directly inform a more accurate scaled eval rubric later.

## What they did

Described YouTube Ads team's eval maturity progression: start with 'vibing' (non-scalable manual inspection of outputs) to quickly identify obvious failure modes and make radical architecture changes without eval infrastructure fighting back; then transition to small golden sets covering primary task categories (including negative cases—checking the model didn't do something bad is as important as checking it did the task); then scale to automated raters only once the agent architecture is stable. Warned that jumping to scaled raters too early causes large oscillations as you simultaneously calibrate the eval and change the model. Also emphasized: highly curated golden sets that evolve with use cases, rater training with rubrics and clear examples, and defining launch criteria (precision/recall threshold or task-specific metric) before starting AB diffs.

## Relevance to YOLO loop

When building new skills, we tend to either skip evals entirely or over-engineer them upfront. This framework gives a concrete progression: vibe → small golden set with negatives → scaled eval. Immediately applicable to any new skill development cycle.

## Notes

Key actionable: always include negative test cases (did model correctly NOT do X) from the start of the golden set. Also: define the launch gate metric (what number constitutes 'good enough to ship') before running any AB experiment, not after seeing the results.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-24-youtube-ads-vibe-first-then-scale-evals` |
| Channel | aie |
| Video | [How Evals and Prompts Shape Agent Behavior — Preetika Bhateja & Daniel Bump, YouTube Ads](https://www.youtube.com/watch?v=xyL2Ltkh-SA) |
| Published | 2026-07-24 |
| Ingested upstream | 2026-07-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

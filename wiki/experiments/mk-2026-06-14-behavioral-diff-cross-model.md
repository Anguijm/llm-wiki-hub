# Automate cross-model behavioral diff to quantify agent capability gaps

> Back to [[experiments-index]]

Source: **[Make ANY Model Think Like Fable in Minutes](https://www.youtube.com/watch?v=B95cu7seTm8)** · mk · 2026-06-14

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we script a structured behavioral diff between two models using the same JSONL corpus (turn count, tool-call cadence, reads-before-edits ratio, test-after-edit rate), then we can quantify the capability gap numerically and target specific behaviors to elicit via prompting, because the diff surfaces which habits are prompt-addressable vs weight-dependent.

## What they did

After generating lightweight transcripts from JSONL files, speaker asked Claude Code to run the same behavioral analysis script against two different model filters and output a side-by-side comparison table. Metrics included number of turns per task, tool-call ordering patterns, frequency of self-testing after edits, and planning verbosity. The output distinguished behaviors that could be elicited (longer thinking, more planning) from those intrinsic to model weights.

## Relevance to YOLO loop

Gives us an empirical method to evaluate model swap decisions in the YOLO loop: before switching frontier models, run the diff to know which workflow behaviors will degrade and which system-prompt patches can compensate.

## Notes

Low effort because the scripting work can itself be delegated to Claude Code. Output is reusable across future model transitions, not just Fable vs Opus.

Backlog triage 2026-06-24 (owner-preference model). Quantified cross-model behavioral diff — model-regression/eval discipline; cheap.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-14 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-06-14-behavioral-diff-cross-model` |
| Channel | mk |
| Video | [Make ANY Model Think Like Fable in Minutes](https://www.youtube.com/watch?v=B95cu7seTm8) |
| Published | 2026-06-14 |
| Ingested upstream | 2026-06-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

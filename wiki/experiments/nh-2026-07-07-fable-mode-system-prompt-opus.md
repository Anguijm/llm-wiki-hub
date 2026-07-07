# Inject a 'Fable-mode' system prompt into Opus to replicate Fable-5 reasoning patterns

> Back to [[experiments-index]]

Source: **[How I Make Opus Think Like Fable (5 easy steps)](https://www.youtube.com/watch?v=XTBWVVcF3Pk)** · nh · 2026-07-07

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we extract the key epistemic and process behaviors from the leaked Claude Fable-5 system prompt and encode them into a structured system prompt given to Opus 4.8, then Opus will produce outputs qualitatively closer to Fable-5 at significantly lower cost, because the model's behavior is heavily shaped by explicit process instructions (verify before asserting, scope before working, reason adversarially, calibrate effort) rather than raw parameter count alone.

## What they did

Nate read through the leaked Claude Fable-5 system prompt and had Fable-5 itself help extract the key behavioral principles: (1) partial training recognition ≠ current knowledge — verify facts; (2) check that referenced files actually exist; (3) address ambiguous queries before asking for clarification, then ask one question max; (4) acknowledge errors and stay on task; (5) calibrate effort to task size (1 citation for simple facts, 3-5 for medium, 5-10 for deep research). He packaged these into a reusable system prompt he calls 'Fable mode' and gave it to Opus 4.8. He then ran dynamic multi-agent workflows where Opus (with this prompt) orchestrated Haiku sub-agents and found results comparable to all-Fable runs at ~3x lower cost. He also described a model routing table approach where the orchestrator selects sub-agents by cost/intelligence/taste scores per task.

## Relevance to YOLO loop

Immediately applicable: drop the 5-gate process prompt into our orchestrator system prompt to improve planning and verification quality without upgrading to a more expensive model. The model routing table is a lightweight way to formalize agent selection logic in our loop.

## Notes

The 5 gates mentioned: scope before work, evidence before reasoning, reason adversarially, verify before declaring done, calibrate effort. Nate says he has a shareable file with the full prompt. The effort-level tuning insight (higher effort ≠ always better; overthinking degrades output) is independently worth testing on our own tasks.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-07 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-07-07-fable-mode-system-prompt-opus` |
| Channel | nh |
| Video | [How I Make Opus Think Like Fable (5 easy steps)](https://www.youtube.com/watch?v=XTBWVVcF3Pk) |
| Published | 2026-07-07 |
| Ingested upstream | 2026-07-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

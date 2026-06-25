# Audit workflows for Fable 5 upgrade window before June 22 paywall

> Back to [[experiments-index]]

Source: **[Claude Mythos is Finally Here.](https://www.youtube.com/watch?v=dYrrEKXtttk)** · nh · 2026-06-11

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `low`

---

## Hypothesis

If we systematically run our most demanding knowledge-work and agentic-coding tasks through Claude Fable 5 before June 22nd, then we can benchmark its real-world improvement over Opus 4.8 at no extra subscription cost, because Fable 5 is included in Pro Max/Team plans only until June 22nd after which it requires usage credits.

## What they did

Nate reviewed the Anthropic launch blog for Claude Fable 5 (a 'Mythos-class' model made safe for general use), noted it is available free on Pro Max/Team/Enterprise until June 22nd, walked through benchmark comparisons versus Opus 4.8 and GPT 5.5 across knowledge work, agentic coding, legal reasoning, and vision, and highlighted that effort levels (low/medium/high/x-high/max) map roughly such that Fable 5 on low ≈ Opus 4.8 on x-high.

## Relevance to YOLO loop

Directly impacts model selection in the dev loop; swapping the base model in Claude Code to Fable 5 during the free window gives free signal on whether to budget for it post-June 22.

## Notes

Time-sensitive: free access window closes June 22. Effort levels: ultra code = x-high + workflows. Mythos 5 remains restricted to Glasswing/US gov partners only.

Backlog triage 2026-06-24 (owner-preference model). Time-boxed 'before June 22 paywall' — window has passed; stale.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-06-11-fable5-model-tier-awareness` |
| Channel | nh |
| Video | [Claude Mythos is Finally Here.](https://www.youtube.com/watch?v=dYrrEKXtttk) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

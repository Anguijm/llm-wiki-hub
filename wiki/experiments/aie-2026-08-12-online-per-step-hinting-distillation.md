# Apply Per-Step Online Hinting to Correct Persistent Agent Behavior Errors

> Back to [[experiments-index]]

Source: **[Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute](https://www.youtube.com/watch?v=ZTA0GwpAUak)** · aie · 2026-08-12

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we use a judge to identify the specific step in an agent rollout where a systematic error occurs and inject a targeted hint at that step (rather than prepending a generic correction at the start of every rollout), then the agent will correct the specific behavior more reliably because the learning signal is concentrated at the causal moment rather than diluted across the whole sequence.

## What they did

Samuel Denton from Applied Compute presented a 2x2 distillation spectrum (offline/online rollouts × offline/online hints) and showed empirical results. For a coding agent with a hyperlink formatting error, offline hinting (same hint prepended to every rollout regardless of whether that rollout had the error) improved correct formatting from ~15% to ~40%. Online per-step hinting—where a judge identifies which step the error occurred and injects a rollout-specific hint at that moment, then distills only the next 1-3 steps—improved correct formatting from ~15% to ~80%. He also described relevance mask self-distillation: using an LLM judge to select which tokens to learn from in the teacher output, avoiding picking up irrelevant stylistic preferences while better learning the target behavior.

## Relevance to YOLO loop

If our agents have persistent systematic errors (formatting, tool call patterns, output structure), per-step hinting offers a more surgical correction mechanism than global system prompt edits. Relevance masking is an advanced follow-on once basic per-step hinting is validated.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-12-online-per-step-hinting-distillation` |
| Channel | aie |
| Video | [Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute](https://www.youtube.com/watch?v=ZTA0GwpAUak) |
| Published | 2026-08-12 |
| Ingested upstream | 2026-08-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

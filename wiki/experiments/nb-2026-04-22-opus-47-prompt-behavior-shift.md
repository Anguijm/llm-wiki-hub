# Audit Existing Prompts Against Opus 4.7 Behavioral Changes

> Back to [[experiments-index]]

Source: **[Your Prompts Didn't Change. Opus 4.7 Did.](https://www.youtube.com/watch?v=tJB_8mfRgCo)** · NateBJones · 2026-04-22

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `low`

---

## Hypothesis

If we run our existing prompt suite unchanged against Opus 4.7 and compare outputs to our prior Claude baseline, then we will surface regressions or unexpected improvements, because model updates silently shift instruction-following behavior even when prompts are identical.

## What they did

Speaker demonstrated that Opus 4.7 exhibits meaningfully different behavior on the same prompts compared to prior versions, implying that any production system relying on Claude needs active regression testing after model updates rather than assuming prompt stability.

## Relevance to YOLO loop

The YOLO loop uses Claude as a core reasoning engine; if Opus 4.7 changed how it interprets system prompts or tool-use instructions, our loop may be producing subtly different outputs without triggering any existing alerts.

## Notes

[2026-05-06T19:43:19Z] DISCARD: Aged out — Opus 4.7 has been live 2+ weeks; behavioral regressions would have surfaced by now via the existing council pipeline.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-22 | `backlog` | Extracted from YouTube RSS |
|  | `` | Triage 2026-05-05: Aged out — Opus 4.7 has been live 2+ weeks; behavioral regressions would have surfaced by now via the existing council pipeline. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-04-22-opus-47-prompt-behavior-shift` |
| Channel | NateBJones |
| Video | [Your Prompts Didn't Change. Opus 4.7 Did.](https://www.youtube.com/watch?v=tJB_8mfRgCo) |
| Published | 2026-04-22 |
| Ingested upstream | 2026-04-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

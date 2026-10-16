# Route agent output through an independent external judge before accepting it

> Back to [[experiments-index]]

Source: **[Stop giving AI tasks. Give it the goal behind the goal.](https://www.youtube.com/watch?v=Gj_GlrTxIWQ)** · eh · 2026-10-15

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we pipe agent-produced artifacts through a separate evaluator model or tool (e.g., a speech-to-text model reviewing audio, a linter reviewing code) rather than letting the producing model self-evaluate, then error detection will improve because self-evaluation has a structural blind spot—the model cannot perceive what it cannot generate.

## What they did

The speaker described using Whisper (a speech-to-text model) as an independent judge on a finished video mix. Whisper misheard 'bolt on' as 'hold on' because the music was masking the word onset. No amount of re-reading the script would have caught this. Claude then adjusted the music dip timing by 100ms and re-ran Whisper to confirm. He generalized this as Felix's principle: never let a model grade its own work—bring in an outside judge.

## Relevance to YOLO loop

Directly maps to our eval pipeline: adding an independent judge step (a different model, a static analyzer, or a domain-specific tool) after each agent output would catch errors the producing agent is structurally unable to self-detect.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `eh-2026-10-15-external-judge-for-model-output` |
| Channel | eh |
| Video | [Stop giving AI tasks. Give it the goal behind the goal.](https://www.youtube.com/watch?v=Gj_GlrTxIWQ) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

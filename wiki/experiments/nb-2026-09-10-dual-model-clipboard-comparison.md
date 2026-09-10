# Run Identical Prompts Across Two Models to Surface Divergent Design Solutions

> Back to [[experiments-index]]

Source: **[I Asked Fable 5.1 and GPT-6 Astra to Get Me Out of Copy Paste Hell. The Results Surprised Me.](https://www.youtube.com/watch?v=n5bZHETCiJA)** · nb · 2026-09-10

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we give the same feature prompt to two frontier models simultaneously, then we will discover a richer solution space and clarify unstated requirements faster because each model's independent design choices reveal preferences we couldn't have articulated upfront.

## What they did

Nate gave Claude (Fable 5.1) and ChatGPT (GPT-6 Astra) the exact same five-line prompt to build a native Mac clipboard manager. Claude produced 'Ledge' (narrow right-side panel, command+shift+V hotkey, precise color swatches) while Astra produced 'Shelf' (wide bottom bar, ctrl+shift+space hotkey, card previews). He then used both apps daily, comparing second-round iteration quality, hotkey ergonomics, visual design, and setup friction across their respective harnesses (Claude Co-work vs Codex). He concluded Astra was faster and more usable day-to-day, while Claude showed more design thoughtfulness and asked clarifying questions. He also sketched a multi-agent pattern where Claude designs/coordinates and a cheaper model (Luna) executes.

## Relevance to YOLO loop

Directly applicable as a prompt-level experiment: run any new feature spec through two models in parallel before committing to one implementation path. The divergent outputs act as a cheap requirements-clarification step before entering the full dev loop.

## Notes

Hotkey ergonomics emerged as a surprisingly important usability differentiator. Consider encoding hotkey conventions in the initial prompt to reduce iteration rounds.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-09-10-dual-model-clipboard-comparison` |
| Channel | nb |
| Video | [I Asked Fable 5.1 and GPT-6 Astra to Get Me Out of Copy Paste Hell. The Results Surprised Me.](https://www.youtube.com/watch?v=n5bZHETCiJA) |
| Published | 2026-09-10 |
| Ingested upstream | 2026-09-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

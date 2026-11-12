# Add explicit cost lines to sub-agent tool descriptions and measure delegation

> Back to [[experiments-index]]

Source: **[Fable 5.2 updated prompting guide](https://www.youtube.com/watch?v=nuSvNEV9fRk)** · eh · 2026-11-10

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we state the dollar or token cost of each helper sub-agent inside its tool description in the ops session's setup, then unnecessary delegation will drop by roughly a third with no loss in task success, because the model follows written cost trade-offs literally.

## What they did

Ekko summarized Anthropic's Fable 5.2 prompting guide. Documenting the financial cost of helper agents inside tool descriptions cut unnecessary sub-agent delegation by about one-third without reducing task success. The same guide reports that stating the difference between ordinary errors and deliberate blockers halved premature halts at medium effort. It also reports that one legacy 'never retry' memory note made the model abandon busy tools in 6 of 10 attempts. The guide flags that ownership statements raise output tokens about 1.5x.

## Relevance to YOLO loop

high: Putting explicit cost trade-offs into sub-agent tool descriptions to steer delegation is not among the existing practices, and it can be tested by replaying a few recorded sessions with and without the line.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-11 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `eh-2026-11-10-subagent-cost-lines` |
| Channel | eh |
| Video | [Fable 5.2 updated prompting guide](https://www.youtube.com/watch?v=nuSvNEV9fRk) |
| Published | 2026-11-10 |
| Ingested upstream | 2026-11-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

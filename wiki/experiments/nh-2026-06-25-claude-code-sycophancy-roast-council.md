# Add a multi-persona 'Roast Council' prompt to stress-test ideas before building

> Back to [[experiments-index]]

Source: **[I asked Claude Code to make me as much money as possible](https://www.youtube.com/watch?v=iTY8Q449YNQ)** · nh · 2026-06-25

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we prompt Claude Code to spin up a council of adversarial personas (contrarian, expansionist, first-principles thinker, deep researcher, buyer, judge) before approving any plan, then we will catch fatal flaws and bad assumptions earlier because the model is tuned by default to agree with the user and will not push back ~88% of the time without explicit instruction.

## What they did

Nate built a skill called 'roast' that pulls Claude out of agreement mode by instantiating five personas that attack a business idea from different angles. The judge persona produces a green-light / reshape / kill verdict plus the single cheapest 48-hour test to validate the idea. He demoed it live on a $9/month YouTube-transcript-to-LinkedIn-posts SaaS idea.

## Relevance to YOLO loop

Directly applicable as a pre-build gate in our loop: run the roast council against any new feature idea or architecture decision before writing code, preventing us from building well-executed wrong things.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-25 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-06-25-claude-code-sycophancy-roast-council` |
| Channel | nh |
| Video | [I asked Claude Code to make me as much money as possible](https://www.youtube.com/watch?v=iTY8Q449YNQ) |
| Published | 2026-06-25 |
| Ingested upstream | 2026-06-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

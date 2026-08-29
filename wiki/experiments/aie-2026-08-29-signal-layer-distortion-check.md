# Add a signal-distortion check before any AI-generated external communication is published

> Back to [[experiments-index]]

Source: **[The Signal Layer: What to Build When Anything Can Be Built — Lena Hall, Akamai](https://www.youtube.com/watch?v=1KOdiGgMtpY)** · aie · 2026-08-29

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we require AI-generated launch copy, documentation, or marketing content to pass a 'read-back' test (give the output to someone unfamiliar with the project and ask them to describe what the product does), then we will catch distortion between intended and received signal before it is broadcast, because AI remix and summarization systematically strips scope-limiting clauses that keep claims honest.

## What they did

Lena argued that AI acts as a convergence machine that makes all outputs identical and strips nuance when remixing content into tweets, decks, and one-pagers. She proposed a 'signal layer': a thin, deliberate function that ensures what customers receive matches what was built. Concrete steps: write the core claim in one sentence with the limit welded in, ensure the limit cannot be edited out in the product itself, and before scaling give a README to someone unfamiliar with the project and ask them to describe the product back—the gap between their description and the intended message is the distortion about to be broadcast.

## Relevance to YOLO loop

Maps to the output-validation step of the YOLO loop: any agent-generated content (READMEs, PR descriptions, changelogs, external docs) should pass a read-back distortion check before being merged or published.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-29-signal-layer-distortion-check` |
| Channel | aie |
| Video | [The Signal Layer: What to Build When Anything Can Be Built — Lena Hall, Akamai](https://www.youtube.com/watch?v=1KOdiGgMtpY) |
| Published | 2026-08-29 |
| Ingested upstream | 2026-08-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

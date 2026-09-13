# Embed Multi-Persona Sub-Agent Review Loop Inside Skills Before Output Surfaces to Human

> Back to [[experiments-index]]

Source: **[Anthropic Engineer Explains: What to Build Instead of AI Agents](https://www.youtube.com/watch?v=HIRDzMtuWFk)** · nh · 2026-09-13

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we embed a multi-persona verification step (e.g., beginner agent, skeptical buyer agent, target audience agent) as the final stage of a skill before returning output, then the human's first look will be a significantly improved draft because the AI catches its own obvious errors and weak spots through adversarial self-review.

## What they did

Nate described adding structured verification into skills: for slide decks, render each slide as an image and inspect screenshots; for research, open primary sources and match claims to evidence; for subjective content, spawn multiple sub-agent personas (beginner, skeptical buyer, target audience member) that each critique the draft, identify recurring issues, make the strongest revisions, and re-run the review. The skill returns output only after it meets defined acceptance criteria, with a summary of what was checked and what remains unverified.

## Relevance to YOLO loop

Applicable to any output-producing step in the dev loop (code, docs, tests, PR descriptions) — embedding a lightweight adversarial review sub-loop before output surfaces reduces the human review burden and tightens the feedback cycle without adding manual steps.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-13-skill-self-verification-personas` |
| Channel | nh |
| Video | [Anthropic Engineer Explains: What to Build Instead of AI Agents](https://www.youtube.com/watch?v=HIRDzMtuWFk) |
| Published | 2026-09-13 |
| Ingested upstream | 2026-09-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

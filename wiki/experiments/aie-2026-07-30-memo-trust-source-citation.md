# Attach inline source receipts with trust levels to every agent-generated claim rather than end-of-document citations

> Back to [[experiments-index]]

Source: **[Build for the Memo, Not the Demo — Shawn Chan, China Resources Holdings](https://www.youtube.com/watch?v=tJFjeMBKbIY)** · aie · 2026-07-30

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If every sentence or claim produced by an agent output is linked inline to its exact source paragraph with a trust level label (verified fact vs. estimate), then downstream human reviewers will trust the output enough to act on it without re-verification, because the one-click provenance check replaces the seven-tab manual verification workflow that currently breaks trust in high-stakes review settings.

## What they did

Shawn Chan, drawing on 15 years of investment committee experience and 200+ deal reviews, described six trust-breaking failure modes in AI finance products: conflicting sources, number disagreements, hidden contradictions, blurred fact/estimate boundaries, non-provable claims, and absent human accountability. His five prescribed fixes were: (1) every claim comes with an inline receipt linking to the exact source paragraph with trust level attached — not a citation tab at the end; (2) facts and estimates are visually separated at a glance; (3) the system refuses to emit a memo where figures don't internally agree; (4) contradictions between sources are surfaced explicitly rather than smoothed over; (5) a logged human approval gate identifies who reviewed what and when. He illustrated with the Google Bard demo error ($100B market cap loss from one unchecked sentence) and a lawyer who filed AI-hallucinated case citations that were verified as real by the same AI that invented them.

## Relevance to YOLO loop

We can apply this pattern immediately to any agent in our loop that produces reports, summaries, or recommendations. Adding inline source linking and a fact/estimate visual distinction to our agent output schema is a low-overhead change that significantly raises the actionability of outputs. The system-level number-consistency check is also automatable as a pre-emit validation step.

## Notes

The speaker's core framing: 'the click-through is a product, everything else is well-written packaging.' The human approval gate with audit log is non-negotiable for high-stakes outputs — you cannot outsource accountability to software. Consider this a checklist for our agent output schema: source receipt, trust level, fact/estimate flag, contradiction surfacing, internal number consistency, named human approver.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-30 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-30-memo-trust-source-citation` |
| Channel | aie |
| Video | [Build for the Memo, Not the Demo — Shawn Chan, China Resources Holdings](https://www.youtube.com/watch?v=tJFjeMBKbIY) |
| Published | 2026-07-30 |
| Ingested upstream | 2026-07-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

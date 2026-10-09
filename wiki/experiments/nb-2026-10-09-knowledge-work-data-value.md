# Audit agent outputs to distinguish real work from performance of work

> Back to [[experiments-index]]

Source: **[Google Has More Data Than Almost Anyone. So Why Is It Bidding $10 Million On Old Emails?](https://www.youtube.com/watch?v=wep2EQ9Y_Tc)** · nb · 2026-10-09

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we instrument our agent loop to tag outputs by whether they drove a verifiable outcome (e.g., state change, artifact produced, decision unblocked) versus coordination overhead (status updates, scheduling messages), then we will get a cleaner signal on where agents actually add value because the raw message/trace volume conflates meaningful work with noise.

## What they did

Speaker argued that corporate communication archives being sold to AI labs (Slack, email, Zoom transcripts) capture both real work and the performance of work—status updates, meeting scheduling, visibility signaling—and that buyers/models cannot distinguish between them. He used an invoice-reconciliation scenario to show that 30 messages and 3 meetings may contain only one genuinely valuable intervention. He warned that agents trained or evaluated on this undifferentiated data will learn to simulate work rather than do it. He recommended structuring data so agents can consume truth records, and praised teams that invest in good markdown files and evals as a foundation.

## Relevance to YOLO loop

Directly applicable to eval design in the YOLO loop: we should label agent trace steps as outcome-driving vs. overhead before using them as training signal or for measuring agent quality.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-10-09-knowledge-work-data-value` |
| Channel | nb |
| Video | [Google Has More Data Than Almost Anyone. So Why Is It Bidding $10 Million On Old Emails?](https://www.youtube.com/watch?v=wep2EQ9Y_Tc) |
| Published | 2026-10-09 |
| Ingested upstream | 2026-10-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

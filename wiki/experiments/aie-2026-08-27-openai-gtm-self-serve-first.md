# Launch agent-powered self-serve capability before building the sales team to identify real bottlenecks

> Back to [[experiments-index]]

Source: **[Reverse-Engineering the AI Buyer — Aliisa Rosenthal, Acrew Capital](https://www.youtube.com/watch?v=wdTRsfw0KG0)** · aie · 2026-08-27

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we automate as much of the GTM motion as possible before hiring humans to fill gaps, then we will identify the true bottlenecks that require human judgment rather than assuming which tasks need humans, because OpenAI's experience showed self-serve launched 4 months after enterprise grew faster and cannibalized heavy sales motion — most buyers prefer not to talk to a salesperson.

## What they did

Speaker (former OpenAI enterprise sales lead, now Acrew Capital) described OpenAI's mistake of launching enterprise-first with heavy sales process, then launching self-serve 4 months later and seeing it immediately outgrow enterprise. Her prescriptive advice: build the automated machine first, find where it breaks, then add humans at those specific bottlenecks. She also described regretting not collecting richer signup form data (phone numbers, use case details) during the inbound surge, and not sending automated acknowledgment emails to the 10,000 daily inbound leads.

## Relevance to YOLO loop

Relevant to how we approach adding human review steps to our loop. Rather than inserting human checkpoints by assumption, we should run the loop fully automated on low-stakes tasks, observe where it fails, and add human gates only at proven failure points.

## Notes

Tactical tip: capture rich context at agent task intake (equivalent to signup form fields) because you may need it later for follow-up or debugging and won't be able to reconstruct it.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-27-openai-gtm-self-serve-first` |
| Channel | aie |
| Video | [Reverse-Engineering the AI Buyer — Aliisa Rosenthal, Acrew Capital](https://www.youtube.com/watch?v=wdTRsfw0KG0) |
| Published | 2026-08-27 |
| Ingested upstream | 2026-08-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

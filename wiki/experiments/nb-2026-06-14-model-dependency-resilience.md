# Build and warm-test a fallback model routing layer for critical workflows

> Back to [[experiments-index]]

Source: **[The End of Unrestricted AI: Why Claude Fable 5 Was Just Forced Offline](https://www.youtube.com/watch?v=b3jlsjOIOzs)** · nb · 2026-06-14

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we implement explicit fallback routing in our agent workflows so that any task currently assigned to a frontier model can be re-routed to an alternate model with a pre-validated prompt adapter, then a single-model access outage will not halt critical work, because the Fable 5 forced takedown demonstrated that frontier model access can disappear without notice due to regulatory action.

## What they did

Speaker (filming from a plane during the Fable 5 shutdown) argued that any workflow with a single-model dependency now has a demonstrated operational risk. He recommended keeping alternative models 'warm', understanding what each model is used for, and not building critical work on the assumption frontier tier access will always be available on yesterday's terms. He framed this as a practical operational response to the precedent set by the US government order forcing Anthropic to take Fable offline.

## Relevance to YOLO loop

Directly relevant to YOLO loop resilience: we should have routing logic that can failover from Fable/Opus to GPT-4.5 or an open-source model, with pre-tested prompt adapters so the loop does not break on vendor access events.

## Notes

Complements the mk-2026-06-14-behavioral-diff card: the diff output tells us what degrades on fallback; this card is about building the routing infrastructure to execute the fallback.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-06-14-model-dependency-resilience` |
| Channel | nb |
| Video | [The End of Unrestricted AI: Why Claude Fable 5 Was Just Forced Offline](https://www.youtube.com/watch?v=b3jlsjOIOzs) |
| Published | 2026-06-14 |
| Ingested upstream | 2026-06-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

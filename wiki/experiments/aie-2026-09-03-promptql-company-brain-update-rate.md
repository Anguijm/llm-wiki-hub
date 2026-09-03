# Track daily update rate of your shared knowledge base as a health metric

> Back to [[experiments-index]]

Source: **[Your company brain will leak secrets: how we stopped it for big banks — Tanmai Gopal, PromptQL](https://www.youtube.com/watch?v=0uC6u0lJJl4)** · aie · 2026-09-03

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we instrument our shared skills/knowledge repo to emit a daily update-count metric and plot it over time, then we will be able to detect whether our company brain is healthy (gently increasing curve) vs. abandoned (sharp drop after initial enthusiasm), because Tanmai found that a working company brain sees continuously increasing updates as agents and humans teach it progressively more skills.

## What they did

Tanmai plotted the daily number of updates to PromptQL's own internal company brain (a 5,000-page wiki) and found a gently but continuously increasing curve rather than a spike-and-decay pattern. He concluded that a healthy company brain attracts more teaching over time because each working skill unlocks adjacent skills users want to add, creating a compounding loop.

## Relevance to YOLO loop

We can apply this to our own prompt library, system-prompt repo, or shared agent context files. Tracking commit/update frequency per day gives us an early signal of whether our shared knowledge infrastructure is being actively maintained or silently rotting.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-03-promptql-company-brain-update-rate` |
| Channel | aie |
| Video | [Your company brain will leak secrets: how we stopped it for big banks — Tanmai Gopal, PromptQL](https://www.youtube.com/watch?v=0uC6u0lJJl4) |
| Published | 2026-09-03 |
| Ingested upstream | 2026-09-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

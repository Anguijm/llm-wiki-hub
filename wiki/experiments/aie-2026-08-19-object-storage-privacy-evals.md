# Run Production Evals Inside Customer Environment via Orchestration-Adjacent Object Storage

> Back to [[experiments-index]]

Source: **[Why Your Enterprise Tech Stack Isn't Ready for AI Agents — Christopher Lovejoy & Saul Howard](https://www.youtube.com/watch?v=mav15aW9lLM)** · aie · 2026-08-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we store sensitive data in object storage inside the customer's environment and pass only references to the orchestration layer, then we can run evals on real production data without that data ever leaving the customer boundary, because the agent retrieves objects by reference rather than receiving raw data in transit.

## What they did

Anterior placed object storage adjacent to their orchestration layer but inside the customer's data perimeter. Agents receive references (URIs/pointers) rather than raw PHI. This pattern allows eval runs to execute against real production data — including re-running historical cases from the immutable ledger — without sensitive data passing through external systems. Combined with human-agent equivalency, this yields privacy-preserving offline evals almost as a byproduct of the base architecture.

## Relevance to YOLO loop

Solves the chicken-and-egg problem of evaluating on real data without exfiltrating it. For our loop, this pattern enables us to run evals against customer or sensitive data stores without pulling raw data into our eval harness.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-19-object-storage-privacy-evals` |
| Channel | aie |
| Video | [Why Your Enterprise Tech Stack Isn't Ready for AI Agents — Christopher Lovejoy & Saul Howard](https://www.youtube.com/watch?v=mav15aW9lLM) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

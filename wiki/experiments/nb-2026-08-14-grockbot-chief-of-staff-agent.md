# Deploy a Chief-of-Staff Coordinator Bot to Manage a Multi-Agent Swarm

> Back to [[experiments-index]]

Source: **[Grok Bot Is The First AI Agent You Just Install. Is It Worth $200?](https://www.youtube.com/watch?v=LM7Ft7g8qJw)** · nb · 2026-08-14

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we designate one agent as a chief-of-staff coordinator that routes tasks to specialized sub-agents, then overall cognitive load drops and throughput increases because the human only manages one interface while parallel agents handle execution.

## What they did

The speaker set up a 'chief of staff' bot in Grockbot as the first agent, whose job was to coordinate a dozen or more specialized bots running in parallel on a shared cloud Linux machine. Because all agents share one computer and one authorization perimeter, messages and context flow between bots transparently without re-authorization, and the human only needs to interact with the coordinator.

## Relevance to YOLO loop

Directly maps to the orchestration layer of the YOLO loop: a coordinator agent can triage incoming tasks, delegate to coding/testing/research sub-agents, and surface results, reducing the number of manual handoffs a developer must manage.

## Notes

Speaker recommends two starter bots: chief-of-staff coordinator and a 'business in a box' revenue-generating bot. Shared auth perimeter means one OAuth grant propagates to all agents — worth replicating in local harness via shared credential store.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-08-14-grockbot-chief-of-staff-agent` |
| Channel | nb |
| Video | [Grok Bot Is The First AI Agent You Just Install. Is It Worth $200?](https://www.youtube.com/watch?v=LM7Ft7g8qJw) |
| Published | 2026-08-14 |
| Ingested upstream | 2026-08-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

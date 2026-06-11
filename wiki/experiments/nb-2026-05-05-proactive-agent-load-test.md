# Run 3-4 Agents in Parallel for a Month to Measure Proactivity Progress

> Back to [[experiments-index]]

Source: **[Consumer AI Has a Problem Nobody's Naming.](https://www.youtube.com/watch?v=Z0HizICooiw)** · nb · 2026-05-05

**Status:** `deferred` · **Effort:** `medium`

---

## Hypothesis

If we run multiple consumer AI agents simultaneously over several months and track how often each one proactively lifts a task without being prompted, then we can objectively measure which products are trending toward genuine proactivity versus staying stuck in reactive chatbot mode, because the signal is the ratio of unsolicited helpful actions to total interactions over time.

## What they did

Nate described deliberately running three to four different AI agents at the same time as a multi-month personal experiment. His evaluation metric is not feature lists but the felt sense of 'load being lifted off my shoulders' — moments when the agent notices something he hasn't and acts or asks permission before he has to think about it. He checks back roughly monthly, after each agent has had a chance to update, and specifically watches model release notes for language about long-running agentic intent with memory for consumers as an early-warning signal that proactivity is maturing.

## Relevance to YOLO loop

Directly applicable as a structured evaluation harness for the YOLO loop: instead of benchmarking on synthetic tasks, this frames agents as month-long proactivity monitors against real personal context (calendars, inboxes, threads), giving us a human-attention-cost metric to complement code-quality metrics.

## Notes

Deferred 2026-05-10: load-testing only earns its slot after we have a deployed agent service. We don't yet. Park until then.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-05 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-05-05-proactive-agent-load-test` |
| Channel | nb |
| Video | [Consumer AI Has a Problem Nobody's Naming.](https://www.youtube.com/watch?v=Z0HizICooiw) |
| Published | 2026-05-05 |
| Ingested upstream | 2026-05-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Promote a persistent manager agent to own the inner execution loop while the developer controls only the outer steering loop

> Back to [[experiments-index]]

Source: **[The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI](https://www.youtube.com/watch?v=pMggiOb18tc)** · aie · 2026-07-09

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we configure a long-running manager agent with persistent context, delegation authority, and event-based triggers, then developer attention becomes the only true bottleneck, because the agent handles scheduling, routing, and memory that developers previously performed manually by polling terminal windows.

## What they did

Peter Steinberger described his evolution from running 10 terminal windows (polling each manually) to talking to a single long-running manager agent that delegates to worker agents. Three enablers: (1) server-side context compaction making long sessions reliable, (2) coordination letting one thread spawn and steer sub-projects, (3) automation triggers that wake the manager on events. The manager returns a PR, original issue, proposed diff, optional video, and a running VNC build. The developer reviews once, leaves a note, and the loop continues. He noted constraints shifted from tokens → compute → attention, and that attention cannot be scaled by adding more of it.

## Relevance to YOLO loop

This is the architectural north star for the yolo loop: replace the human as inner-loop scheduler with a persistent manager agent, and reserve human attention exclusively for outer-loop direction-setting and approval. The trigger/wake pattern (e.g. every 10 minutes on GitHub events) is directly implementable today.

## Notes

Paul's 'chief of staff' pattern mentioned: agent pinned and waking every 10 minutes, coordinating GitHub work, creating sidebar threads for human steering. Start with a cron-triggered manager on a single repo as a minimal version of this.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-09-manager-agent-outer-loop` |
| Channel | aie |
| Video | [The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI](https://www.youtube.com/watch?v=pMggiOb18tc) |
| Published | 2026-07-09 |
| Ingested upstream | 2026-07-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

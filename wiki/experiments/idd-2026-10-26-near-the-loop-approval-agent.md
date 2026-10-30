# Build an event-triggered near-the-loop agent with narrow tools

> Back to [[experiments-index]]

Source: **[ELITE Agentic Engineers Are LEAVING THE LOOP... Here’s why](https://www.youtube.com/watch?v=52JX83rGPLc)** · idd · 2026-10-26

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we trigger an agent from an event stream (webhook, cron or log feed), give it narrow tools instead of general bash, and require one-click human approval for the final action, then we cut manual prompting safely because the human only approves rather than drives.

## What they did

IndyDevDan showed durable agents in isolated sandboxes with persistent memory, including an incident response agent that detects a log anomaly, triages, drafts a patch and waits for one-click approval, and a news curation agent that ran for 1.5 weeks on an M4 Mac mini. He recommends removing general-purpose bash from autonomous agents and moving through in-the-loop, near-the-loop and out-of-the-loop stages in order.

## Relevance to YOLO loop

high: It describes a staged-autonomy harness with event triggers, approval gates and restricted tools.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-29 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `idd-2026-10-26-near-the-loop-approval-agent` |
| Channel | idd |
| Video | [ELITE Agentic Engineers Are LEAVING THE LOOP... Here’s why](https://www.youtube.com/watch?v=52JX83rGPLc) |
| Published | 2026-10-26 |
| Ingested upstream | 2026-10-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

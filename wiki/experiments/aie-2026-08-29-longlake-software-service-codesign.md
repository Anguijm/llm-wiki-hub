# Embed AI Agents Natively Into Existing Operator Workflows to Drive Adoption

> Back to [[experiments-index]]

Source: **[How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](https://www.youtube.com/watch?v=B0fjR3yaZFU)** · aie · 2026-08-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we co-design AI agent tooling to appear inside the tools operators already use (ERP systems, Excel, Outlook, Slack) rather than asking them to switch to a new interface, then adoption rates will increase and the learning loop will compound faster, because the energy required for enablement stays low and usage drives continual improvement.

## What they did

Varun Shenoy described Long Lake's model of acquiring and operating real services businesses (35 companies across HOA, property management, HR, architecture) and deploying AI from within rather than selling it as a vendor. He outlined a spectrum from co-pilot → synchronous agent → asynchronous agent → long-running agent → AI co-worker, and argued that the bottleneck is not model capability but adoption. Key tactic: 'extreme software-service co-design' — embedding products natively into Excel, ERP systems, Outlook, or meeting people physically. He also described a learning loop where usage drives continual learning, which improves the agent, which drives more usage, and argued enablement and continual learning must be treated as the same loop rather than owned by separate teams.

## Relevance to YOLO loop

Maps to the human-in-the-loop and adoption layer of any dev loop: if agents are only triggered from a dedicated UI, adoption stalls. Integrating async agent triggers into Slack threads or existing tools (GitHub PR comments, Jira) reduces friction and increases the feedback data needed to improve the loop.

## Notes

Actionable near-term experiment: add a Slack-taggable agent that can close a loop on a task in-thread, then measure whether usage of the agent increases organically versus a standalone UI approach.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-29-longlake-software-service-codesign` |
| Channel | aie |
| Video | [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](https://www.youtube.com/watch?v=B0fjR3yaZFU) |
| Published | 2026-08-29 |
| Ingested upstream | 2026-08-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

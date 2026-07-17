# Implement an Agent Optimizer Loop That Hill-Climbs Agent Instructions from Trace Data

> Back to [[experiments-index]]

Source: **[On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft](https://www.youtube.com/watch?v=RGSFUqzqErE)** · aie · 2026-07-17

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run an automated hill-climbing optimization loop over agent instructions using real user-interaction traces as the eval signal, then we will produce better-performing agents without hand-tuning prompts, because the optimizer can discover non-obvious instruction combinations that improve task adherence based on actual behavioral evidence rather than developer intuition.

## What they did

Pablo Castro (Microsoft CVP for AI Knowledge) presented Microsoft Foundry's Agent Optimizer component. The workflow is: (1) externalize all agent configuration—instructions, tool definitions, skills—into swappable config files; (2) optionally auto-generate a task-adherence evaluation dataset from existing traces and instructions using 'eval generate'; (3) run 'optimize' which performs a JAIR-style hill-climbing loop over candidate instruction sets, evaluating each against the rubric; (4) when a superior candidate is found, apply it by swapping the config. He demonstrated this live in VS Code with the Foundry toolkit, showing that optimized instructions emerged from the process rather than being hand-written, and that the baseline vs. optimized performance delta was measurable. He framed this as a 'real learning loop materialized in practice' that compounds organizational knowledge into the agent over time.

## Relevance to YOLO loop

The agent optimizer pattern is directly applicable to improving our own loop agents: externalize CLAUDE.md / system prompts as swappable configs, generate evals from traces, run hill-climbing, deploy the winner. This closes the feedback loop between agent behavior in production and agent configuration.

## Notes

Key architectural requirement: agent configuration must be externalized (not baked into code) for the optimizer to swap it. Pablo showed this takes ~45 minutes to run for a simple agent. Available today at ai.azure.com via Microsoft Foundry. The broader knowledge taxonomy he presented (intrinsic/extrinsic/learned) is a useful mental model for reasoning about what agents know and how to extend it.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-17 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-17-microsoft-iq-company-grounding` |
| Channel | aie |
| Video | [On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft](https://www.youtube.com/watch?v=RGSFUqzqErE) |
| Published | 2026-07-17 |
| Ingested upstream | 2026-07-17 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

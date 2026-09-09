# Run a fully offline multi-agent loop using Frontier Agent + 35B open weights model

> Back to [[experiments-index]]

Source: **[Run a $10,000 AI Model at Home, Here's How](https://www.youtube.com/watch?v=mgPj252Dek8)** · do · 2026-09-09

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we deploy the Apex open-sourced Frontier Agent framework with its 35B open-weights model locally, then we can execute multi-agent research and coding tasks with full privacy and zero API cost because the model fits on consumer hardware (e.g., MacBook) and the framework handles planning, code execution, and cross-agent verification natively.

## What they did

The host ran Apex's Frontier Agent (open-sourced framework + 35B open-weights model) entirely offline on a MacBook. He gave it a research task: chart how quickly new open models receive quantized versions over the last 2 years. A group of agents fetched data from HuggingFace, a second group cross-checked accuracy, a third created and reviewed the chart, and the final output included sources and verifications for every claim. The same system can run on Appex.ai for users without sufficient local compute.

## Relevance to YOLO loop

Directly maps to the agent execution layer of our dev loop — we can substitute or augment cloud-API-dependent agent runs with a fully local, private pipeline for tasks that don't require frontier-model capability, reducing latency and cost while keeping the same planning-execute-verify structure.

## Notes

Frontier Agent repo on GitHub; 35B model on HuggingFace. Fireworks AI (guest's company) also offers serverless open-weights inference and a Fireworks Nexus intelligent routing layer as cloud fallback options worth evaluating alongside local deployment.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-09-09-run-open-weights-agent-offline` |
| Channel | do |
| Video | [Run a $10,000 AI Model at Home, Here's How](https://www.youtube.com/watch?v=mgPj252Dek8) |
| Published | 2026-09-09 |
| Ingested upstream | 2026-09-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

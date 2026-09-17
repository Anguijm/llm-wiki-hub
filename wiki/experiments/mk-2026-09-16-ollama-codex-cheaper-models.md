# Route Routine Codex Tasks to Local or Cheap Cloud Models via Ollama to Reduce Token Spend

> Back to [[experiments-index]]

Source: **[Ollama + Codex = WAY CHEAPER](https://www.youtube.com/watch?v=575v0WYJQsE)** · mk · 2026-09-16

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we integrate Ollama into Codex and route grunt-work tasks (skill execution, drafting, summarization) to local or cheap cloud models (e.g., GLM, Gemma) while reserving GPT-6 Astra for deep agentic coding, then we can reduce token costs by 10-20x while maintaining acceptable output quality for 80% of daily tasks.

## What they did

Mark showed how to add Ollama to Codex via a one-click plugin (Settings > Apps > Add to Codex), which adds cloud-based Ollama models to the model picker. To also enable local models, he used a Codex prompt that inspects the machine's RAM, GPU, and disk space, selects a tool-capable local model that fits comfortably, downloads it if needed, and connects it via the Ollama integration while preserving existing cloud model configs. He then demonstrated a multi-tier agent workflow: Astra plans the task, GLM (cloud, ~10-15x cheaper) does research, a local Gemma model shortlists results, and Astra synthesizes the final output as a diagram. He compared costs: GPT-6 Astra at $10/$50 per M tokens vs GLM at 10-20x cheaper, and noted $20 on Ollama cloud can stretch to the equivalent of $100-200 of Codex spend.

## Relevance to YOLO loop

Directly applicable: we can tier our dev loop so that expensive frontier model calls are reserved for novel reasoning steps, while cheaper/local models handle repetitive code generation, summarization, or skill execution, significantly extending our effective budget.

## Notes

Prompt for auto-configuring local model available in video description. Local models must support tool calling to work within Codex harness. Cloud Ollama models available out of the box with one-click plugin; local models require the extra prompt step.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-09-16-ollama-codex-cheaper-models` |
| Channel | mk |
| Video | [Ollama + Codex = WAY CHEAPER](https://www.youtube.com/watch?v=575v0WYJQsE) |
| Published | 2026-09-16 |
| Ingested upstream | 2026-09-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

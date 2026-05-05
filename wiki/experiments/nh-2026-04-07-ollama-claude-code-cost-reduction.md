# Route Low-Stakes Claude Code Subtasks to Local Ollama Models to Cut Loop Cost

> Back to [[experiments-index]]

Source: **[Ollama + Claude Code = 99% CHEAPER](https://www.youtube.com/watch?v=O2k_qwZA8HU)** · NateHerk · 2026-04-07

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we configure Claude Code to route boilerplate-heavy or low-complexity subtasks (file scaffolding, docstring generation, simple refactors) to a local Ollama model while reserving Claude API calls for reasoning-intensive steps, then we can reduce per-loop API spend by a significant margin without measurable quality regression, because the video demonstrates a configuration achieving ~99% cost reduction on suitable tasks.

## What they did

Speaker walked through configuring Claude Code to use a locally running Ollama model as the backend for code generation tasks, bypassing the Anthropic API. Demonstrated the setup with a config file change, ran benchmark tasks comparing output quality, and showed cost tracking confirming near-zero spend for the Ollama-routed tasks. Noted that quality held for straightforward tasks but degraded on complex reasoning.

## Relevance to YOLO loop

Cost is a real constraint on YOLO loop iteration frequency. A tiered routing strategy—local model for cheap passes, Claude API for eval and hard reasoning—could make the loop economically sustainable at higher iteration rates.

## Notes

Discarded 2026-04-08 as REPEAT of nh-2026-04-03-ollama-claude-code-cost (discarded 2026-04-07). Same channel (@NateHerk), same author, same Ollama-as-cost-reduction theme. Local-model policy decision = NO (cost is not currently a constraint, operational overhead does not earn its slot). The @NateHerk channel is producing recurring Ollama-routing experiments — consider channel-policy mechanism to auto-skip these at ingestion in future.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-07 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-04-07-ollama-claude-code-cost-reduction` |
| Channel | NateHerk |
| Video | [Ollama + Claude Code = 99% CHEAPER](https://www.youtube.com/watch?v=O2k_qwZA8HU) |
| Published | 2026-04-07 |
| Ingested upstream | 2026-04-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

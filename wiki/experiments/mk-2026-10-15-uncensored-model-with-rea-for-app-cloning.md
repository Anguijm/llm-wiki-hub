# Substitute an uncensored model in the REA harness to reduce guardrail friction on app decompilation tasks

> Back to [[experiments-index]]

Source: **[Uncensored AI + REA Can Reverse Engineer Anything](https://www.youtube.com/watch?v=ScSDVV5xhww)** · mk · 2026-10-15

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `low`

---

## Hypothesis

If we route REA (Reverse Engineer Anything) tasks through an uncensored or less-restricted model (e.g., GLM uncensored via Obliteration AI) instead of a frontier model with content guardrails, then the agent will complete more of the decompilation and reconstruction workflow without refusals because frontier models sometimes decline to execute certain reverse-engineering steps that uncensored models will attempt.

## What they did

Mark used the DeepSeek harness (open-source, model-agnostic workbench) with GLM 5.2 uncensored (via Obliteration AI cloud endpoint) plus the REA MCP server backed by Ghidra. He targeted QuickTime Player, wanting a clone with continuous speed control. GLM one-shotted roughly 80% of the app including a new name and icon; additional prompts added font, export formats, and UI polish. Total cost was ~$9-10. He noted that frontier models (Claude, Codex, Gemini) sometimes push back on reverse-engineering certain app types, whereas uncensored models proceed without friction.

## Relevance to YOLO loop

Relevant to our agent harness model-selection strategy: for internal tooling cloning or competitive analysis tasks where guardrails cause friction, routing through an uncensored model on a pay-as-you-go endpoint could unblock workflows at low cost.

## Notes

Backlog triage 2026-10-17 round 3 (operator: "I want you to evaluate the yolo cards"). Settled maybe, cut: Assessment: the card is about cloning a commercial app (QuickTime) with a model chosen to avoid refusals, which is a licence and legality problem, not a technique he needs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-10-15-uncensored-model-with-rea-for-app-cloning` |
| Channel | mk |
| Video | [Uncensored AI + REA Can Reverse Engineer Anything](https://www.youtube.com/watch?v=ScSDVV5xhww) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

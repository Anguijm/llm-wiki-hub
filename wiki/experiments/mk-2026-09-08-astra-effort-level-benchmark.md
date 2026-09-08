# Benchmark Astra effort levels (low/medium/high/max/ultra) on an identical multi-step research-and-build task

> Back to [[experiments-index]]

Source: **[I Tested Every GPT-6 Astra Effort Level. Here's What I'd Use](https://www.youtube.com/watch?v=OQipTxv9Qv0)** · mk · 2026-09-08

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we run the same complex prompt (market research → opportunity selection → evidence gathering → Excalidraw plan → website → working prototype) across all Astra effort levels plus Soul-high as a control, then medium effort will deliver near-equivalent output quality to high/max/ultra at a fraction of token cost and time, because the marginal quality gains above medium are cosmetic rather than structural.

## What they did

Mark sent an identical multi-part prompt to seven parallel Codex threads covering all Astra effort levels (low, medium, high, max, extra-high, ultra) plus Soul-high as a control. The task: identify a SaaS opportunity for 2–20-employee service businesses via X and Reddit research, evaluate three opportunities, pick one with a defensible moat, produce an Excalidraw JSON canvas, build a polished chatbot website explaining the plan, and deliver a working SaaS prototype. He tracked tokens consumed, wall-clock time, research breadth (Reddit/X threads checked), and qualitative output quality across business plan coherence, website polish, and prototype functionality. Key findings: medium and high produced near-identical structure and quality; ultra consumed ~20M tokens with sub-agents but added only cosmetic polish; Soul-high finished in 32 minutes using only 6M tokens with comparable research breadth. He recommends Astra medium on fast mode for daily use.

## Relevance to YOLO loop

Directly informs our model-selection and cost-management decisions in the YOLO loop: we should default Astra calls to medium effort and reserve high only for final-pass quality checks, avoiding ultra/max except for explicitly token-budget-approved tasks. Also validates using Soul-high as a cheaper alternative for well-scoped research tasks.

## Notes

Mark notes Astra's official docs confirm it is designed to ask clarifying questions rather than make assumptions — this 'laziness' is by design and is not fully mitigated by raising effort level. The trick of spinning up multiple parallel threads with the same prompt via a single dispatch is worth replicating for our own A/B model tests. Free findings doc linked in video description.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-09-08-astra-effort-level-benchmark` |
| Channel | mk |
| Video | [I Tested Every GPT-6 Astra Effort Level. Here's What I'd Use](https://www.youtube.com/watch?v=OQipTxv9Qv0) |
| Published | 2026-09-08 |
| Ingested upstream | 2026-09-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

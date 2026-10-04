# Use High-Speed Generation to Produce a Star-Map of Options, Then Apply Human Judgment to Select

> Back to [[experiments-index]]

Source: **[What if AI worked at 1.000.000 tokens per seconds?](https://www.youtube.com/watch?v=uUK06_vNyHY)** · eh · 2026-10-04

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we deliberately generate a large diverse set of candidate outputs (endings, code branches, experiment designs) rather than a single best answer, then we will make better final selections because the bottleneck shifts from generation to taste/judgment — which humans retain a comparative advantage in.

## What they did

The speaker ran a thought experiment: at 1M tokens/second, asking for a story ending yields 1,000 endings before coffee cools. Rather than scrolling a pile, the useful framing is to lay them out as a 'star map' — hopeful endings left, dark ones right, familiar in the middle, strange at edges — so the human navigates a space and picks two stars, causing 100 new endings to bloom between them. The same pattern applies to software (40 app versions tested and ranked), science (10,000 catalyst candidates proposed and filtered), and negotiation rehearsal (10,000 conversation branches, with moves that held up across most branches highlighted).

## Relevance to YOLO loop

Maps to the ideation-and-triage phase of the YOLO loop: instead of prompting for one answer, prompt for N diverse candidates, cluster or rank them, then apply human judgment only at the selection step — maximizing throughput while preserving quality control.

## Notes

Concrete implementation: for any design decision in the YOLO loop (prompt design, architecture choice, test strategy), generate 20+ variants explicitly, then evaluate rather than iterating on one. Pairs well with evals infrastructure.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `eh-2026-10-04-judgment-as-bottleneck-thought-experiment` |
| Channel | eh |
| Video | [What if AI worked at 1.000.000 tokens per seconds?](https://www.youtube.com/watch?v=uUK06_vNyHY) |
| Published | 2026-10-04 |
| Ingested upstream | 2026-10-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

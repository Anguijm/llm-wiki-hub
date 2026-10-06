# Encode Expert Teaching Rules as Mandatory Agent Behaviors to Fix AI's Explain-vs-Code Imbalance

> Back to [[experiments-index]]

Source: **[I Built Another Andrej Karpathy Using Claude](https://www.youtube.com/watch?v=bvGptCLDhyo)** · nh · 2026-10-06

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we extract an expert's explicit pedagogical rules from their own writing and encode them as hard behavioral constraints in a Claude system prompt (e.g. 'define done before touching code', 'run code before showing it', 'show a breaking version'), then the agent will explain and verify its work step-by-step rather than silently shipping untested code, because the rules override Claude's default bias toward generating code over generating understanding.

## What they did

After building the Karpathy wiki, the speaker prompted Claude to extract Karpathy's teaching principles as discrete numbered rules, each backed by a direct quote from his writing or talks. These rules (including 'build smallest version first', 'predict output before running', 'show the broken version', 'never hand over code you haven't run yourself') were then translated into agent behaviors in a system prompt. The agent was tested against a real coding task (byte-pair tokenizer) and a code-review task (a YouTube comment scraper that crashed on emoji in Windows terminals). In both cases the agent followed the rule sequence visibly and logged which rule governed each action. The speaker noted this pattern directly solves the problem Karpathy himself publicly complained about — that Claude Code 'just wants to write code' rather than teach alongside it.

## Relevance to YOLO loop

Maps to the review and verification gates in our dev loop. Encoding 'run before you show' and 'show the breaking version' as system-prompt rules could be applied to any of our coding agents to reduce silent failures and untested code reaching production or clients. The rule-logging behavior also produces an audit trail that fits naturally into our loop's output-inspection step.

## Notes

Low-cost subset experiment: the rule-encoding step alone (without the full wiki crawl) could be tested quickly by manually writing 5-7 teaching rules into a system prompt and measuring whether code-explanation quality improves on a benchmark task. This decouples the wiki-building effort from the behavioral-constraint hypothesis.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-06 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-10-06-teaching-rules-system-prompt` |
| Channel | nh |
| Video | [I Built Another Andrej Karpathy Using Claude](https://www.youtube.com/watch?v=bvGptCLDhyo) |
| Published | 2026-10-06 |
| Ingested upstream | 2026-10-06 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

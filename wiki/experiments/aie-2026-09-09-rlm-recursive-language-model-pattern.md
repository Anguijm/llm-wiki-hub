# Prototype an RLM (Recursive Language Model) pattern for long-context document processing tasks

> Back to [[experiments-index]]

Source: **[It's Tokens All The Way Down: How RLMs are Different — Kevin Madura, AlixPartners](https://www.youtube.com/watch?v=xo68uCibfm8)** · aie · 2026-09-09

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we use an RLM architecture where the main LM delegates subtasks to sub-LMs operating in a REPL/Python environment and only returns semantically relevant results upward, then we can process arbitrarily long inputs (invoices, log files, large codebases) without chunking/embedding strategies, because sub-LM context windows fill independently and the main LM context only receives distilled outputs rather than full document contents.

## What they did

Kevin Madura (AlixPartners) introduced RLMs (Recursive Language Models) — a pattern where the LM treats its context as a symbolic object in a REPL environment, can write and execute code against it, and can delegate subtasks to sub-LMs (often itself) with DSPI-specified input/output schemas. Key differentiators from standard tool calls: interaction is with a symbolic environment (Python REPL), not JSON strings; delegation is recursive and model-directed; context rot is mitigated because sub-tasks live in sub-LM contexts and only distilled results surface to the main LM. He showed benchmarks (ULong, BrowseComp) where RLMs outperform standard tool-calling approaches even at lower cost. Practical examples: consolidated inventory extraction from 200-page invoices, security vulnerability scanning of 500K-line codebases, log trace analysis for agent harness optimization (Halo project). He noted that DSPy is used to enforce schemas between main-LM and sub-LM handoffs, improving reliability on smaller/cheaper models.

## Relevance to YOLO loop

Relevant to any step in our loop where we currently struggle with large context inputs (long transcripts, big codebases, extended traces). The RLM pattern could replace our current chunking/RAG approach for document-heavy tasks and reduce the context engineering overhead that currently consumes significant dev time.

## Notes

Predict RLM is the reference implementation. Omar (DSPy creator) is an adviser. Halo project uses RLM for agent trace analysis and harness meta-optimization. Speaker flagged that post-training models to be natively RLM-aware would be a significant capability jump. DSPy schemas between LM layers improve maintainability and cheaper-model reliability.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-09-rlm-recursive-language-model-pattern` |
| Channel | aie |
| Video | [It's Tokens All The Way Down: How RLMs are Different — Kevin Madura, AlixPartners](https://www.youtube.com/watch?v=xo68uCibfm8) |
| Published | 2026-09-09 |
| Ingested upstream | 2026-09-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

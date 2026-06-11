# Use the 'build a workflow' keyword trigger to auto-generate multi-agent harnesses for large document analysis

> Back to [[experiments-index]]

Source: **[The Claude Update Everyone Missed (Dynamic Workflows)](https://www.youtube.com/watch?v=-tLlZqrXpo8)** · mk · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we prefix complex multi-document analysis prompts with 'build a workflow' in Claude Code, then the system will auto-generate an appropriate multi-agent harness with parallel document readers and cross-checking agents, reducing hours of manual analysis to 20–30 minutes because the workflow feature spawns agents with independent context windows that collaborate rather than share a single degrading context.

## What they did

Mark demonstrated generating a due diligence report on 70+ documents (contracts, leases, proposals, memos) by prompting Claude Code with 'build a workflow that reads every contract here in parallel and flags anything that could hurt the deal.' Claude Code auto-generated a workflow spec, spawned 50+ agents working in parallel with cross-validation, and produced a synthesized report in 20–30 minutes. A second deeper prompt ('hunt things a seller would rather we never find') spun up 51 agents and consumed ~3.2M tokens over 23 minutes. He showed the /workflows slash command for invocation, explained that the keyword 'workflow' triggers the multi-colored workflow UI indicator, and covered practical use cases: security audits (fan-out per file + adversarial refutation), competitor analysis (100 sites → one sheet), resume screening (score against rubric + bias check), and compliance gap analysis.

## Relevance to YOLO loop

The keyword-triggered harness generation is immediately usable in our loop for large codebase security reviews, dependency audits, or multi-file refactoring tasks where single-context approaches degrade. The prompt pattern is concrete and copyable.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-06-11-dynamic-workflows-due-diligence` |
| Channel | mk |
| Video | [The Claude Update Everyone Missed (Dynamic Workflows)](https://www.youtube.com/watch?v=-tLlZqrXpo8) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

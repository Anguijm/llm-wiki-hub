# Implement spec-driven development with markdown requirements and design docs generated before any code is written

> Back to [[experiments-index]]

Source: **[Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS](https://www.youtube.com/watch?v=IddXPepIAS4)** · aie · 2026-06-28

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we require the agent to generate structured markdown requirements and design documents (with EARS-format user stories, mermaid architecture diagrams, and property-based test specifications) before generating any implementation code, then the resulting code better matches intent and requires fewer correction cycles, because explicit upfront specifications constrain the solution space and give the agent verifiable criteria to code against rather than inferring intent from a brief prompt.

## What they did

Erik described spec-driven development as writing markdown specification files before any code is written, optimised for LLM coding assistants. He demonstrated the workflow using Kiro IDE (kiro.dev): the agent first generates a design document (mermaid sequence/architecture diagrams, property-based test stubs using fast-check), then a requirements document in EARS format (user stories with 'When/shall' structure), then a task list (including an auto-generated MVP scoping pass), and only then implements the tasks. Skills (keyword-triggered instruction files) can be activated during spec creation or implementation phases. He emphasised the Goldilocks principle for agents.md/CLAUDE.md steering files — too much context is as harmful as too little — and stressed that the human must remain in the loop reviewing every generated document before implementation proceeds.

## Relevance to YOLO loop

Spec-driven development is a meta-pattern for how the YOLO loop should be initialised for new features. Rather than jumping straight into code generation, adding a requirements-doc and design-doc phase at the start of each loop cycle gives the agent better-constrained implementation targets and makes progress reviewable at each step.

## Notes

Kiro IDE is purpose-built for this workflow but the pattern is implementable in any coding agent via a custom skill that sequences: requirements → design → tasks → implement. Property-based test generation (fast-check for TS/JS) during the spec phase is a strong addition to catch edge cases before implementation.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-28-spec-driven-development` |
| Channel | aie |
| Video | [Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS](https://www.youtube.com/watch?v=IddXPepIAS4) |
| Published | 2026-06-28 |
| Ingested upstream | 2026-06-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

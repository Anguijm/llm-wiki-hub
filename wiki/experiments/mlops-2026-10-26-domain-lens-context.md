# A/B test domain-lens framing in agent skills

> Back to [[experiments-index]]

Source: **[Building AI So Everyone Can Flourish](https://www.youtube.com/watch?v=irjFdpOtb00)** · mlops · 2026-10-26

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we inject a named domain framework (e.g. SRE toil, GTD, Eisenhower Box) or a specialist knowledge source into agent prompts and skills, then outputs will be more specific and less generic than unframed prompts because the lens focuses latent model reasoning.

## What they did

The speaker described an internal IT research agent that first recommended hiring more staff. When the query was reframed through O'Reilly's SRE MCP (Google SRE Handbook lens), it identified operational toil and advised restructuring instead. He also described 'magic word' context engineering, where structured framework terms are injected into prompts to unlock reasoning, and said unframed prompts give lowest-common-denominator advice.

## Relevance to YOLO loop

high: Tests a skill and prompt design technique (lens injection) that can be compared directly against baseline prompts in Claude Code workflows.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-27 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-10-26-domain-lens-context` |
| Channel | mlops |
| Video | [Building AI So Everyone Can Flourish](https://www.youtube.com/watch?v=irjFdpOtb00) |
| Published | 2026-10-26 |
| Ingested upstream | 2026-10-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Extract Structured Brand Constraints from a URL and Inject as Agent Context to Reduce Style Drift

> Back to [[experiments-index]]

Source: **[Training Taste — Thais Castello Branco, Taste Labs](https://www.youtube.com/watch?v=sDMGWK4wZ_w)** · aie · 2026-09-10

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we programmatically extract a brand's design system (colors, typography, tone, spacing) into structured agent context before generating any design or copy artifact, then output quality and brand fidelity will measurably improve over unconstrained generation, because agents collapse to statistical means when style constraints are absent.

## What they did

Thais Castello Branco (Taste Labs) described their Brand API: given a brand URL, it extracts brand components into structured, agent-followable specifications and also provides a judgment/verification layer to check whether agent output adheres to the brand. They showed a live example where prompting Claude to design a slide deck in a specific company's branding produced a mediocre result by default (middle image), but using the Brand API extraction as context produced a high-fidelity match to the original brand (right image). She also described a 'brand index' of pre-built cohesive brand systems that can be retrieved for users without an existing brand, avoiding the slop patterns of fully generative brand creation. She framed slop prevention as requiring three things: structured constraints as context, agent judgment during generation, and a verification gate after generation.

## Relevance to YOLO loop

Maps to our prompt construction step: adding a structured constraint extraction phase before any design or UI generation task should reduce the iteration rounds needed to get acceptable output. The verification gate pattern (separate agent checks output against extracted constraints) is a reusable quality layer we can add to our loop.

## Notes

Taste Labs Brand API in beta. Follow up on access. The baby-classifier slop-detection pattern mentioned briefly is worth investigating as a cheap pre-ship quality gate.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-10-brand-api-slop-prevention` |
| Channel | aie |
| Video | [Training Taste — Thais Castello Branco, Taste Labs](https://www.youtube.com/watch?v=sDMGWK4wZ_w) |
| Published | 2026-09-10 |
| Ingested upstream | 2026-09-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

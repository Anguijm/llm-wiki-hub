# Point a coding agent at your docs and generate an agent experience report

> Back to [[experiments-index]]

Source: **[The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](https://www.youtube.com/watch?v=Lrw0jqBNaw0)** · aie · 2026-08-27

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run a coding agent against our documentation and capture the full interaction transcript, then we will identify gaps in machine-readability and agent-unfriendly structures, because agents read docs differently than humans — they fetch rather than browse, encounter API errors differently, and make library recommendations based on doc structure quality.

## What they did

Speaker (research scientist turned agent advocate at Sourcegraph) described building CodeScaleBench to measure agent interactions with developer tools at scale, and recommended a concrete first step: point a coding agent at your docs, review the transcript, and produce an 'agent experience report' analogous to a developer experience audit. She also described GEO (Generative Engine Optimization) experiments measuring agent mentions vs. recommendations as a new GTM metric.

## Relevance to YOLO loop

Relevant to how our own tools and APIs are consumed by agents in the loop. Running this audit on our internal tool documentation would surface whether our agent can reliably discover and use the right utilities, or whether poor doc structure is causing hallucinated API calls.

## Notes

Curb-cut analogy: making docs agent-legible also improves human developer experience. Low effort, high signal audit.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-27-agent-advocate-devrel-evals` |
| Channel | aie |
| Video | [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](https://www.youtube.com/watch?v=Lrw0jqBNaw0) |
| Published | 2026-08-27 |
| Ingested upstream | 2026-08-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

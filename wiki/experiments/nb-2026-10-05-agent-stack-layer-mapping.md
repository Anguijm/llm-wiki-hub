# Map your AI workflow stack into four explicit layers: data, structured workflows, application interface, and agentic layer

> Back to [[experiments-index]]

Source: **[The end of the app era: What comes next?](https://www.youtube.com/watch?v=0j8wy4jUlsw)** · nb · 2026-10-05

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we explicitly document and map every tool in our dev loop into the four-layer stack (data provider, structured workflow, app interface, agentic harness), then we will surface hidden vendor lock-in risks and identify which layers are replaceable, because the transcript shows most teams accumulate stack complexity by accident and cannot articulate switching costs when leadership demands vendor changes.

## What they did

Nate described how knowledge workers are unknowingly vertically integrating a personal AI stack—data layer, workflow layer, application layer, and agentic layer—without documenting it. He used a real anonymized recruiting example where a worker trained an agent deeply enough that switching AI vendors would cost weeks of progress, but her manager had no visibility into this. He argues everyone must now think through their full stack and communicate it proactively.

## Relevance to YOLO loop

Directly applicable: we can audit the YOLO loop's current tool dependencies (data sources, workflow scaffolding, app interfaces, agent harness) against this four-layer model to identify which layers are sticky and which are swappable, and to document switching costs before they become a crisis.

## Notes

Nate frames this as both a seller/buyer problem and an individual worker problem. The four-layer framework (data, structured workflow, app interface, agentic layer) is the core artifact to implement.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-05 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-10-05-agent-stack-layer-mapping` |
| Channel | nb |
| Video | [The end of the app era: What comes next?](https://www.youtube.com/watch?v=0j8wy4jUlsw) |
| Published | 2026-10-05 |
| Ingested upstream | 2026-10-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

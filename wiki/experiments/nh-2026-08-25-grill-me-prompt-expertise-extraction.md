# Use a 'grill me' prompt to extract domain expertise before building an AI agent

> Back to [[experiments-index]]

Source: **[The 3 AI Agency Mistakes Keeping You From $20K/Month Retainers](https://www.youtube.com/watch?v=DoHPZf7jEQ4)** · nh · 2026-08-25

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we instruct an LLM to relentlessly interview us about a specific domain or process before building an agent for it, then the resulting agent will produce higher-quality, more nuanced outputs because the model will have captured tacit subject-matter expertise that a generic prompt would miss.

## What they did

Nate described a technique he calls the 'grill me skill': at the end of a prompt or session, you ask the AI to interview you relentlessly about the topic at hand. This pulls all the subject-matter expertise out of your head and into the context the AI uses to build the automation. He used the example of building a content-generation agent for a consultant — by having the AI grill the consultant about their sales call observations, the resulting agent encodes the consultant's unique framing rather than producing generic output.

## Relevance to YOLO loop

Can be inserted as a pre-build step in the YOLO loop whenever we are constructing an agent for a domain-specific task: run the grill-me interview first, save the transcript as context, then feed it into the system prompt or CLAUDE.md for that agent.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-25 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-25-grill-me-prompt-expertise-extraction` |
| Channel | nh |
| Video | [The 3 AI Agency Mistakes Keeping You From $20K/Month Retainers](https://www.youtube.com/watch?v=DoHPZf7jEQ4) |
| Published | 2026-08-25 |
| Ingested upstream | 2026-08-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

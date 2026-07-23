# Add a human-intent attestation step to AI-generated content pipelines

> Back to [[experiments-index]]

Source: **[The AI Slop Problem Nobody's Talking About | Substack CEO Interview](https://www.youtube.com/watch?v=m_ZyTNmCDeY)** · nb · 2026-07-23

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we require a human-authored intent statement or editorial decision before any AI-generated content is published or submitted as an agent output, then the pipeline will produce outputs with traceable human ownership because the core distinction between slop and valuable content is whether a human believed in and directed what was made.

## What they did

Substack CEO Chris Best described the dividing line between AI slop and legitimate AI-assisted content: not the tool used, but whether a human believed in what was being made. He contrasted intentional use of AI as a paintbrush (human intent + AI execution) versus 'tell Claude to make 1,000 blog posts and don't read them.' He noted Pangram's data showing ~40% of long-form LinkedIn content is fully AI-generated, and argued this functions as a denial-of-service attack on the public square. Substack is building features to surface human-authored work, with the thesis that human attention is the last non-inflationary resource.

## Relevance to YOLO loop

In our agentic dev loop, agent-generated outputs (docs, PRs, summaries, code) risk becoming internal slop — present but unowned. Adding a lightweight human-intent checkpoint (even a single sentence of editorial direction logged before generation) creates accountability and improves downstream quality by forcing the human to actually engage with the task before delegating.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-23-anti-slop-human-intent-signal` |
| Channel | nb |
| Video | [The AI Slop Problem Nobody's Talking About | Substack CEO Interview](https://www.youtube.com/watch?v=m_ZyTNmCDeY) |
| Published | 2026-07-23 |
| Ingested upstream | 2026-07-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

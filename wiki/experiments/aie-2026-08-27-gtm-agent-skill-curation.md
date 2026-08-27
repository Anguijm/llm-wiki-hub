# Build agent skill files encoding domain expertise as the foundation for agentic GTM workflows

> Back to [[experiments-index]]

Source: **[How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](https://www.youtube.com/watch?v=Qw_tC68KKes)** · aie · 2026-08-27

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we encode expert-level business knowledge into structured skill files that agents can reference during task execution, then agents will perform more consistently and predictably across different users and contexts, because Cloudflare's internal GTM agent achieved 2x efficiency gains after embedding sales process expertise, call handling patterns, and business context into curated skill definitions rather than relying on general model knowledge.

## What they did

Speaker (sales ops at Cloudflare) described a three-pillar framework for agentic GTM: scale analysis (answering data queries in 5 min vs. 2 hours), scale insight (pushing contextual stories to teams), and self-service capabilities (giving reps expert-level context on demand). The foundation he identified was 'skill curation' — embedding business knowledge into skill files that make agent behavior deterministic and consistent. He also emphasized feedback loops and iterative re-architecture over monolithic builds.

## Relevance to YOLO loop

The skill file pattern is directly applicable to our loop. We can define skill files for recurring agent tasks (e.g., 'how to write a PR description', 'how to triage a bug') that encode our team's standards, making agent output more consistent without requiring detailed prompts each time.

## Notes

Key lesson: start with quality over coverage. Better to have 50 questions answered at 95% accuracy than 100 at 70%.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-27-gtm-agent-skill-curation` |
| Channel | aie |
| Video | [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](https://www.youtube.com/watch?v=Qw_tC68KKes) |
| Published | 2026-08-27 |
| Ingested upstream | 2026-08-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

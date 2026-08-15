# Build a Pay-As-You-Go Multi-Model Creative Studio via API Aggregator

> Back to [[experiments-index]]

Source: **[This Simple AI Setup Replaces Your Higgsfield Subscription](https://www.youtube.com/watch?v=_VX6BZDKgrg)** · mk · 2026-08-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we build a thin UI wrapper over an API aggregator (e.g., fal.ai) that routes to 30+ image/video models with transparent cost tracking, then we can replace fixed SaaS creative subscriptions with a cheaper pay-as-you-go workflow because we own the routing logic, prompt refinement, and cost ledger without being locked into any single provider's credit system or feature roadmap.

## What they did

The speaker built a custom creative studio UI that connects to an API aggregator (fal.ai) exposing 37+ image and video models (including Veo 3.1, Minimax, Seed Dance, Kling, etc.). The UI accepts media uploads and vague prompts, uses a cheap workhorse model (e.g., Gemini Flash) to refine prompts against each provider's official documentation, then routes the generation request to the chosen model. A cost ledger tracks every generation transparently. He also built a local MCP so the same studio can be triggered from Claude Code, Codex, or other coding agents inline. The entire repo, MCP, and setup guide were open-sourced. No custom model training — purely API orchestration with AI-generated UI built by feeding provider API docs to a coding agent.

## Relevance to YOLO loop

Directly applicable: we can wire an API aggregator into our dev loop so any YOLO iteration that needs image/video generation calls a single internal endpoint rather than managing multiple provider SDKs. The prompt-refinement sub-call pattern (cheap model reads provider docs, rewrites the vague prompt, then hits the generation API) is a reusable primitive for any generative step in our pipeline. The transparent cost ledger pattern is useful for tracking per-experiment spend.

## Notes

Open-source repo + MCP promised in video description (second link). Key aggregator mentioned: fal.ai. Prompt-refinement pattern: feed provider's own documentation page (as markdown) to a cheap model alongside the user's vague prompt to get a model-optimized prompt before the actual generation call. Worth checking if fal.ai MCP already exists before building from scratch.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-08-15-api-aggregator-creative-studio` |
| Channel | mk |
| Video | [This Simple AI Setup Replaces Your Higgsfield Subscription](https://www.youtube.com/watch?v=_VX6BZDKgrg) |
| Published | 2026-08-15 |
| Ingested upstream | 2026-08-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

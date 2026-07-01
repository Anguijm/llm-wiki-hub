# Apply Fable 5-specific prompting rules to system prompts and skill files

> Back to [[experiments-index]]

Source: **[How Anthropic Engineers Actually Prompt Fable 5](https://www.youtube.com/watch?v=vcU85OrwuV0)** · nh · 2026-07-01

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we encode six Anthropic-recommended prompting habits (give the why, use negative prompts, omit 'explain your reasoning', prefer short directives, embed uncertainty disclosure, lead with outcome) into our agent system prompts and skill/memory files, then we will get more accurate, lower-cost Fable 5 responses and avoid silent rerouting to Opus 4.8, because Fable's stronger reasoning means it needs intent signals rather than exhaustive rules.

## What they did

Herk distilled Anthropic's official Fable 5 prompting documentation plus X/community feedback into six habits: (1) Give the 'why'/intent context so the model connects task to information rather than guessing. (2) Use explicit negative prompts — tell it what NOT to do (e.g. 'report what you find and stop, do not fix/send/edit/delete until I say go'). (3) Do NOT include standing 'explain your reasoning' lines in system prompts — this can trigger a safety reroute to Opus 4.8. (4) Instruct uncertainty disclosure ('if something isn't verified, say so plainly'). (5) Say less not more — short instructions steer as well as long rule lists for Fable 5. (6) Lead with outcome in a single line rather than numbered rule lists. He also notes Fable 5 silently routes to Opus 4.8 for safety-flagged requests (hacking, dangerous biology, revealing private reasoning) and that API callers see the model name in the response but UI users do not.

## Relevance to YOLO loop

Directly actionable for any YOLO loop system prompt or agent skill file using Fable 5. The negative-prompting and 'no explain-your-reasoning' rules are concrete changes to existing prompt templates; the silent Opus reroute behaviour is important for cost and capability tracking in the loop.

## Notes

Fable 5 pricing: $10/M input, $50/M output tokens. Promotional free-tier access (up to 50% of weekly limits) ends July 7 2026. Silent Opus 4.8 fallback is a cost and quality risk to monitor in production agent loops.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-01 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-07-01-fable5-prompting-six-habits` |
| Channel | nh |
| Video | [How Anthropic Engineers Actually Prompt Fable 5](https://www.youtube.com/watch?v=vcU85OrwuV0) |
| Published | 2026-07-01 |
| Ingested upstream | 2026-07-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

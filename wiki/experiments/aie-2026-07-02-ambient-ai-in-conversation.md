# Build an ambient AI participant that captures decisions from live conversation without explicit prompts

> Back to [[experiments-index]]

Source: **[The Prompt Is Still a Punch Card - Ted Johnson, JoinIn AI](https://www.youtube.com/watch?v=hVJOnuhFmTA)** · aie · 2026-07-02

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we deploy an AI system that passively listens to a multi-person conversation, follows context without being addressed, and surfaces relevant captures or clarifications at chosen moments, then the 'translation tax' of context briefing is eliminated because the AI already holds the shared situational context and users never need to switch modalities to engage it.

## What they did

Speaker (Ted Johnson, JoinIn AI) demonstrated a meeting scenario where an AI participant tracked a product requirements conversation, identified scope decisions in real-time (expense approvals vs. access requests, $5K vs. $10K threshold), and generated structured requirement summaries without any participant typing a prompt. The AI determined when to interject ('AI, hold that' triggered it, but it also acted on implicit cues). He framed this as moving from 'prompt as punch card' — forcing humans to encode intent for machine consumption — to AI meeting humans in their natural communication channel.

## Relevance to YOLO loop

Suggests a future direction for our loop's input layer: rather than requiring developers to write explicit prompts to capture architectural decisions or task context, an ambient listener on dev communication channels (Slack, standup transcripts, PR comments) could auto-populate the context pre-loader identified in the context-war experiment. Start with async transcript processing before attempting real-time.

## Notes

Speaker's three-concept framework (channel / expression / protocol) is useful for evaluating any new AI interface: what changed is expression (natural language), but channel (text box) and protocol (turn-taking prompt/response) are still 1960s-era. JoinIn AI is attempting to modernize all three simultaneously.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-02-ambient-ai-in-conversation` |
| Channel | aie |
| Video | [The Prompt Is Still a Punch Card - Ted Johnson, JoinIn AI](https://www.youtube.com/watch?v=hVJOnuhFmTA) |
| Published | 2026-07-02 |
| Ingested upstream | 2026-07-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

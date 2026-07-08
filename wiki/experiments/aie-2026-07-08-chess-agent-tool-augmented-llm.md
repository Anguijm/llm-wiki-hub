# Augment an LLM with domain-specific constraint tools to prevent hallucination in rule-bound domains

> Back to [[experiments-index]]

Source: **[Running a Chess YouTube Channel entirely by AI — Stephan Steinfurt, TNG](https://www.youtube.com/watch?v=BqZrTdgBaPw)** · aie · 2026-07-08

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we give an LLM agent a set of domain-constraint tools (e.g., legal-moves validator, engine evaluation, checks/captures/threats extractor, board state manager) alongside a capable base model, then the agent will produce accurate domain-specific analysis at low error rates because the tools externalize the hard constraint-checking that LLMs hallucinate on while the LLM handles natural language generation.

## What they did

Stephan's team built a fully automated chess YouTube channel. Each night, games are downloaded from Lichess, a chess engine analyzes them, then an agent (running Gemini 3 Pro which has strong chess post-training) is given tools: legal move validator, a full chessboard the agent can play moves on and retract, chess engine evaluation calls, checks/captures/threats extractor, and web search for historical context. The agent produces structured analysis output which is rendered into narrated video with diagrams. Videos are auto-uploaded nightly. Error rate is roughly 1 in 20 videos. Cost per video is ~20-30 euro cents. Channel has 500k views and 4000+ subscribers.

## Relevance to YOLO loop

Generalizable pattern: for any domain where LLMs hallucinate on hard constraints (e.g., API contracts, type systems, test assertions), wrapping the LLM with domain-specific constraint-checking tools dramatically reduces error rate. Applicable to our agent's code generation loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-08-chess-agent-tool-augmented-llm` |
| Channel | aie |
| Video | [Running a Chess YouTube Channel entirely by AI — Stephan Steinfurt, TNG](https://www.youtube.com/watch?v=BqZrTdgBaPw) |
| Published | 2026-07-08 |
| Ingested upstream | 2026-07-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

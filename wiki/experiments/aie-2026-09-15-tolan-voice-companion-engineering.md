# Implement a tone-routing classifier to dynamically select model tier per conversation turn based on emotional stakes, not cost

> Back to [[experiments-index]]

Source: **[Tolan: Voice-First AI Companion — Paula Dozsa, Tolan](https://www.youtube.com/watch?v=xLUQOqjudtA)** · aie · 2026-09-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we add a lightweight tone-routing classifier that runs on every conversation turn and routes high-stakes emotional moments to a frontier model while routing lightweight turns to a smaller/faster model, then we achieve better perceived quality at lower overall cost than using a single model for all turns, because user satisfaction is disproportionately determined by a small fraction of high-stakes turns (onboarding, emotional crises, first impressions) and wasting frontier compute on routine turns provides no measurable benefit.

## What they did

Paula Dozsa (iOS engineer, Tolan) described engineering a voice-first AI companion with 4M+ hours of voice conversation. Key finding: latency drifting from 2s to 2.5s tanked every product metric and drove user complaints. Four principles emerged: (1) Design for conversational volatility—voice users change topics mid-sentence, say 'um', interrupt; they built smart turn-taking that distinguishes real interruptions from noise, cutting bad early aborts by >50% at a cost of only 60ms extra latency. (2) Latency is the product—measure every pipeline stage separately (end-of-utterance detection, ASR, time-to-first-token, TTS first byte, playback). Moving to GPT-4.1 on the responses API cut time-to-speech by >700ms. (3) Tiered model fleet with a tone router: a cheap classifier runs on every turn and reads emotional state; high-stakes turns (first messages, onboarding, crisis/therapist tones) always get the frontier model. (4) Use AI agents internally for development: concurrent coding agents, triage bots wired to Linear/Sentry/DataDog via MCP, eval agents that run find-fix-verify rounds against production logs.

## Relevance to YOLO loop

The tone-routing pattern is directly applicable to any multi-turn agent system: classify each turn's stakes before routing to a model tier. The internal agentic development practices (triage bots, eval agents with MCP integrations) are immediately applicable to our own dev loop. The <2s total round-trip latency target and per-stage measurement discipline are good benchmarks.

## Notes

Tolan is at 4.8 stars / 162k App Store reviews with emotional safety as highest-scoring well-being dimension. The 'route based on stakes not cost' principle is the key insight. The MCP-wired triage bot that can reconstruct crashes and open PRs autonomously is worth investigating as a pattern for our own incident response.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-15-tolan-voice-companion-engineering` |
| Channel | aie |
| Video | [Tolan: Voice-First AI Companion — Paula Dozsa, Tolan](https://www.youtube.com/watch?v=xLUQOqjudtA) |
| Published | 2026-09-15 |
| Ingested upstream | 2026-09-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

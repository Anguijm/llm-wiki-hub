# Separate the code-generating agent from the security-validating agent to prevent self-review blind spots

> Back to [[experiments-index]]

Source: **[Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk](https://www.youtube.com/watch?v=1EZdpEhwmNc)** · aie · 2026-07-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we route agent-generated code through a distinct validation agent (or deterministic scanner) that was not involved in generation, then we will catch more security defects than having the same model self-review, because empirical data from Snyk's enterprise customers shows that the generator and validator being the same entity produces systematic blind spots.

## What they did

Manoj Nair presented Snyk's real-world finding from 5,000 enterprise customers that AI-generated code quality is measurably worse than human-generated code, and that the root architectural flaw is using the same LLM to both generate and validate. He demonstrated Snyk's MCP-based scanning skill that intercepts agent tool calls and flags issues like echoing authorization headers, pulling logic from third-party YAML URLs (prompt injection vector), and pulling live data from Reddit/Twitter. He framed this as the core security architecture decision: the generator and validator must be separated.

## Relevance to YOLO loop

Directly applicable: we can add a post-generation Snyk MCP scan step (or equivalent static analysis hook) in our YOLO loop before any PR is opened, implemented as a Claude Code hook or CI gate.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-20-generator-validator-separation` |
| Channel | aie |
| Video | [Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk](https://www.youtube.com/watch?v=1EZdpEhwmNc) |
| Published | 2026-07-20 |
| Ingested upstream | 2026-07-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

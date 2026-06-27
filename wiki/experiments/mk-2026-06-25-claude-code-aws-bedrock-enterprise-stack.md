# Deploy a multi-agent Claude platform inside AWS Bedrock with SOC2/HIPAA guardrails and kill switches

> Back to [[experiments-index]]

Source: **[Claude Code + AWS Bedrock = Enterprise AI](https://www.youtube.com/watch?v=T17DYl_4Z-U)** · mk · 2026-06-25

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `high`

---

## Hypothesis

If we host Claude-powered agents entirely within AWS Bedrock (no external model calls) and build a custom dashboard with per-agent kill switches, least-privilege IAM, response filtering, spend caps, and a full audit log, then enterprises with strict compliance requirements can participate in agentic AI workflows because all data stays within their own AWS environment and every action is logged and reversible.

## What they did

Mark spent 30+ days and ~10M tokens building a platform on AWS Bedrock that hosts multiple Claude agents (plus open-source models like Qwen, Meta, Mistral via the Anthropic-AWS partnership). The platform includes a custom web dashboard with usage/cost tracking, shared agent memory across Telegram and Slack, editable system prompts, session history, SOC2/HIPAA readiness scoring against live config, daily spend caps, and a Jarvis meta-agent that narrates the state of the whole system. He detailed the 2-week planning cycles before each build phase.

## Relevance to YOLO loop

Relevant if our loop needs to serve enterprise or regulated clients: provides the blueprint for wrapping our existing Claude Code workflows inside an auditable, access-controlled cloud environment rather than using the public API directly.

## Notes

Mark offers a free blueprint/slide deck + prompt guide via link in description. Premium membership gives access to the full repo.

Backlog triage 2026-06-27 (owner-preference model). Enterprise AWS Bedrock multi-agent platform (SOC2/HIPAA/IAM) — off-domain cloud infra, high effort.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-25 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-06-25-claude-code-aws-bedrock-enterprise-stack` |
| Channel | mk |
| Video | [Claude Code + AWS Bedrock = Enterprise AI](https://www.youtube.com/watch?v=T17DYl_4Z-U) |
| Published | 2026-06-25 |
| Ingested upstream | 2026-06-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

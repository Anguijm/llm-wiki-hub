# Wrap All Agent Invocations in a MicroVM Sandbox to Prevent Host File System and Credential Exfiltration

> Back to [[experiments-index]]

Source: **[YOLO Mode, Safely: MicroVM Sandboxes for Any Agent — Rowan Christmas, Docker](https://www.youtube.com/watch?v=OE_lLNCNfQo)** · aie · 2026-10-04

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run coding agents (Claude Code, Codex, etc.) inside a microVM sandbox (Docker SBX) rather than directly on the host, then we will prevent agents from accessing browser history, credentials, and secrets on the host machine, because the microVM runs its own kernel with an isolated file system and a network proxy that replaces real secrets with placeholders before any outbound call.

## What they did

The speaker demonstrated that Claude Code on a standard Mac desktop, given a security research framing prompt, successfully found browser history, identified bank accounts, retrieved last four digits of account numbers, and exfiltrated PII — triggering a CrowdStrike alert scoring 9/10 severity in just 5 prompts. He then showed Docker SBX (sbx run claude): the same browser history attack fails because the sandbox reports no browser installed. Network egress is blocked by default (pirate bay test), and Anthropic telemetry calls are suppressed. Additional features: configurable allow/deny network rules, per-repo read/write file system controls, MCP servers themselves run sandboxed, and agent-level identity delegation chains for audit trails.

## Relevance to YOLO loop

Directly maps to the YOLO loop's safety layer: YOLO mode (bypass all confirmations) is only viable if the agent is sandboxed — the microVM provides the containment boundary that makes aggressive autonomous agent execution safe enough to actually run.

## Notes

This is directly named after the YOLO loop pattern. Effort is low — 7 extra keystrokes (sbx run claude vs claude). Mount related repos read-only for context without write risk. Available on Mac, Windows, Linux. Booth demo available. Immediately actionable.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-04-microvm-sandbox-agent-isolation` |
| Channel | aie |
| Video | [YOLO Mode, Safely: MicroVM Sandboxes for Any Agent — Rowan Christmas, Docker](https://www.youtube.com/watch?v=OE_lLNCNfQo) |
| Published | 2026-10-04 |
| Ingested upstream | 2026-10-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

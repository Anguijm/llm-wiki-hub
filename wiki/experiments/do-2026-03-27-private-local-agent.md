# Run YOLO builds via a 100% local AI agent stack

> Back to [[experiments-index]]

Source: **[RIP OpenClaw… this 100% private AI Agent is insane](https://www.youtube.com/@DavidOndrej)** · @DavidOndrej · 2026-03-27

**Status:** `done` · **Verdict:** `discard` · **Effort:** `high`

---

## Hypothesis

If we run YOLO builds using a self-hosted AI agent (OpenClaw or n8n + local LLM) instead of interactive cloud sessions, then we gain persistent autonomous execution (no session timeouts, no API key exposure) because the entire stack runs locally with no cloud dependency.

## What they did

David Ondrej demonstrated building a 100% private AI agent comparing it favorably to OpenClaw. Key technique: connect the local agent to OpenRouter to access Perplexity search models for free, enabling autonomous research + execution without cloud API exposure. Architecture: all model calls and file access stay on-machine. Cisco researchers noted OpenClaw's prompt injection risks, making a secure local alternative compelling for sensitive repos.

## Relevance to YOLO loop

YOLO builds currently depend on interactive Claude Code sessions that can time out mid-run. A local agent could run Phase 2 refinement batches overnight and never expose API keys — especially relevant once the portfolio scales beyond 161 projects.

## Outcome

Council evaluation: Feasibility 3/10 (8GB VRAM too small), Cost Savings 2/10 (only ~$100/mo), Quality Risk 9/10 (7B models vs Sonnet = massive degradation), Ops Complexity 8/10 (sysadmin nightmare), Strategic Value 5/10 (sovereignty matters long-term), Timing 1/10 (wrong time). Counter-argument: valid when 48GB+ VRAM hardware available, compliance requires it, or infinite-loop agents needed. RECOMMENDATION: Park until hardware upgrade. Start hybrid now — use local 8B for low-complexity tasks (summarization, linting) while keeping builds on cloud Sonnet.

## Notes

Park until 48GB+ VRAM hardware. Revisit as hybrid router architecture.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `done` | Council evaluated. Park until hardware upgrade. Start hybrid for low-complexity tasks. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-03-27-private-local-agent` |
| Channel | @DavidOndrej |
| Video | [RIP OpenClaw… this 100% private AI Agent is insane](https://www.youtube.com/@DavidOndrej) |
| Published | 2026-03-27 |
| Ingested upstream | 2026-04-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Add security scanning as Claude Code hooks and skills rather than post-hoc MCP scanning to reduce latency and token overhead

> Back to [[experiments-index]]

Source: **[Agentic Development Security — Ezra Tanzer, Snyk](https://www.youtube.com/watch?v=cgimkNGNjvU)** · aie · 2026-07-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we implement security validation as Claude Code hooks (pre/post tool call) and named skills rather than end-of-run MCP scans, then we will reduce both scan latency and context-window token consumption while maintaining coverage, because hooks fire at the point of action rather than scanning the full accumulated output, and skills can be invoked selectively with targeted context.

## What they did

Ezra Tanzer described Snyk's evolution from MCP-server-plus-rules (which had agents ignoring rule files, latency at end of run, and token overhead from scanning through the context window) to hooks and skills. Hooks intercept specific tool calls (e.g. before a file write) and inject security context at that moment. Skills are named commands the agent can invoke selectively (e.g. 'snyk fix' with a known vulnerability ID that uses Snyk's reachability analysis to understand exploitability and suggest a targeted fix). He also described a 'what agents access' pillar: scanning MCP skill files themselves for security issues (echoed auth headers, third-party YAML logic injection, live data pulls from untrusted sources) before they are installed.

## Relevance to YOLO loop

Immediately applicable: we can add a Claude Code post-tool hook that runs a lightweight static scan on any file written during a YOLO loop session, flagging issues inline rather than in a separate CI step, reducing the feedback loop from hours to seconds.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-20-snyk-hooks-skills-agent-code-security` |
| Channel | aie |
| Video | [Agentic Development Security — Ezra Tanzer, Snyk](https://www.youtube.com/watch?v=cgimkNGNjvU) |
| Published | 2026-07-20 |
| Ingested upstream | 2026-07-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

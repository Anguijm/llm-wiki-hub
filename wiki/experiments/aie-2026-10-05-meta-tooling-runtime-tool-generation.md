# Implement meta-tooling: give an agent an editor, shell, and load-tool primitive so it can write and register new tools at runtime without restart

> Back to [[experiments-index]]

Source: **[Agents That Write Their Own Tools at Runtime — Sandhya Subramani, AWS](https://www.youtube.com/watch?v=33Oct2hqGnk)** · aie · 2026-10-05

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we equip an agent with only three primitive tools (a code editor, a shell executor, and a dynamic tool loader) plus a permissive system prompt, then it will generate the specific capability tools it needs on demand at runtime, because the demo shows the agent detecting missing capabilities, writing the tool code, loading it into its own runtime, and executing it within the same session without any restart.

## What they did

Sandhya from AWS demoed an agent built on the open-source Strands Agents framework that starts with zero domain tools. When asked to do math or count characters, it detects it lacks the capability, writes a Python tool file, loads it dynamically, and calls it—all within the running session. She described this as 'meta-tooling' and highlighted that Strands supports model swapping without rewriting architecture. She also covered required guardrails: sandboxed code execution environment, constrained permissions, observability/telemetry, and inter-agent dependency tracking. She noted Strands itself used this pattern to auto-generate its TypeScript version from its Python version.

## Relevance to YOLO loop

High relevance: the YOLO loop currently requires pre-defining all tools before an agent run. A meta-tooling layer would let agents self-extend during a run when they hit capability gaps, reducing the need for us to anticipate every tool needed upfront. The sandboxing requirement is a prerequisite we'd need to design for.

## Notes

Strands Agents is open-source from AWS. Key guardrails: sandbox the code execution environment (Strands recently launched this), constrain tool permissions, add observability for inter-agent message inspection. Speaker flagged this as the beginning of self-improving agents.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-05 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-05-meta-tooling-runtime-tool-generation` |
| Channel | aie |
| Video | [Agents That Write Their Own Tools at Runtime — Sandhya Subramani, AWS](https://www.youtube.com/watch?v=33Oct2hqGnk) |
| Published | 2026-10-05 |
| Ingested upstream | 2026-10-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

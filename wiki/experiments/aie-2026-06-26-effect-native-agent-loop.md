# Replace LangGraph with a custom Effect-native agent loop for full observability and structured concurrency

> Back to [[experiments-index]]

Source: **[Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov](https://www.youtube.com/watch?v=4uFVSLgD2Q4)** · aie · 2026-06-26

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we replace a managed agent framework (LangGraph) with a custom agent loop built on the Effect TypeScript library, then we gain fine-grained tracing, structured concurrency, and full control over complex tool-calling patterns because Effect provides built-in spans, error handling, and logging that propagate automatically through every agent step without additional instrumentation.

## What they did

OpenGov's AI agents team built OG Assist, an in-app AI assistant embedded across all their ERP products (budgeting, procurement, permitting). They started on LangGraph but migrated to a custom Effect-native agent loop when use cases scaled and required more control. The Effect loop provides: automatic span tagging for every function call (enabling drill-down traces without manual instrumentation), structured concurrency, typed error handling, and Zod-equivalent schema validation. They also built: (1) A2A protocol integration, (2) rolling summary for long-context memory management (compress old turns into a summary, keep recent turns verbatim), (3) generative UI — the agent builds forms and UI components at runtime from registered primitives based on the task, (4) sandboxing for tool execution, and (5) feedback collection loops feeding into evals. Tool definition pattern: each capability is a typed Effect tool, tools are grouped into toolkits, toolkits are registered with the LLM per session context.

## Relevance to YOLO loop

The Effect-native loop pattern is directly applicable to YOLO loop implementation: automatic tracing without instrumentation overhead, structured concurrency for parallel tool calls, and the rolling summary approach for long coding sessions that exceed context windows. The toolkit registration pattern is a clean model for how YOLO loop exposes file system, git, and test runner tools.

## Notes

Effect is a TypeScript library (effectful.ai). The rolling summary for long context is immediately adoptable without full Effect migration. Generative UI at runtime is an interesting pattern for YOLO loop status dashboards. They also use Claude + Cursor internally for developer velocity — same stack as YOLO loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-26 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-26-effect-native-agent-loop` |
| Channel | aie |
| Video | [Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov](https://www.youtube.com/watch?v=4uFVSLgD2Q4) |
| Published | 2026-06-26 |
| Ingested upstream | 2026-06-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

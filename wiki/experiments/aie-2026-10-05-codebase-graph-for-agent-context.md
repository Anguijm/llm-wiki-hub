# Build or integrate a codebase graph index as infrastructure context for coding agents operating on large repos

> Back to [[experiments-index]]

Source: **[AI Coding Agents Are Breaking Big Codebases — Dan Adler, Sourcegraph](https://www.youtube.com/watch?v=Bdrs3uAX0_M)** · aie · 2026-10-05

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we give coding agents access to a compiler-accurate graph of the codebase (cross-repo search, dependency graph, symbol resolution) rather than relying on context-window cloning, then agent-generated changes will have fewer cross-service regressions and duplicated implementations, because agents currently fail on large codebases due to inability to fit repo context into a context window and lack of awareness of existing libraries and dependencies.

## What they did

Dan Adler, CEO of Sourcegraph, argued that AI coding agents are causing large codebases to decay: different coding standards applied by different agents, duplicated code, brittle cross-service dependencies, and new vulnerabilities. He said the foundational fix is a code graph with compiler-accurate analysis and cross-repo search that can be handed to agents as infrastructure context. He demoed Sourcegraph's new agentic batch changes product (in beta) that executes a patch across hundreds/thousands of repos from a single prompt, self-heals based on CI feedback, and provides full auditability. A user at Merkari ran it against 2 known repos and it found 80 additional vulnerabilities across the rest of their codebase.

## Relevance to YOLO loop

Directly relevant if the YOLO loop operates on a multi-repo or growing codebase. The code graph as agent context layer is an architectural addition that would reduce agent errors on cross-repo tasks. The batch-changes pattern (single prompt → auditable multi-repo patch) is a model for how we could propagate standards changes across our own infrastructure.

## Notes

Dan's framing: 'Visibility is infrastructure.' The specific quote from a top-10 US bank tech leader: current agent tools don't support 5,000–500,000 repo codebases. Sourcegraph's batch changes product is in beta. Merkari case study is a concrete validation point.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-05 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-05-codebase-graph-for-agent-context` |
| Channel | aie |
| Video | [AI Coding Agents Are Breaking Big Codebases — Dan Adler, Sourcegraph](https://www.youtube.com/watch?v=Bdrs3uAX0_M) |
| Published | 2026-10-05 |
| Ingested upstream | 2026-10-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

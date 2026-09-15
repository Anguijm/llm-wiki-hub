# Build a File-Based Agent Harness with Company-Specific Domain Knowledge

> Back to [[experiments-index]]

Source: **[How We Solved Agent Building — Andrew Qu, Vercel](https://www.youtube.com/watch?v=9dYcwOkpCE8)** · aie · 2026-09-14

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we build domain agents from a simple file system of system instructions, skill files, and tool definitions (rather than complex multi-agent orchestration pipelines), then we get faster iteration, better performance, and easier debugging, because off-the-shelf chained-agent architectures accumulate fragile state whereas file-based agents remain composable and company-specific knowledge can be injected directly.

## What they did

Andrew Qu described Vercel's journey building D0 (a data science agent for internal Snowflake queries) through multiple architectural iterations: (1) a mega-prompt with manual SQL copy-paste, (2) a chained multi-agent pipeline with dedicated planning, query, execution, and reporting agents each with scoped tools, and (3) a rewrite using Eve — Vercel's open-source file-based agent framework (eve.dev). Eve uses system instruction files, skill files, and tool definitions with open-source adapters for Postgres, OpenAI responses API, Docker, etc. The rewrite simplified the convoluted D0 architecture into a small set of files. A beta customer (Aura) rebuilt their agent using Eve and saw fewer steps, better success rates, and better insights vs. off-the-shelf Claude. Vercel now runs ~20 internal agents across marketing, legal, data, and finance.

## Relevance to YOLO loop

Eve's architecture maps directly onto our loop: system instructions as files, skills as markdown, tools as connectors. The lesson that company-specific knowledge embedded in the file system outperforms generic off-the-shelf agents is directly applicable — we should encode our domain conventions into skill files rather than relying on general model knowledge.

## Notes

Eve is open source at eve.dev. Vercel also offers managed deployment with observability (agent runs, tool calls, step traces, cost estimates). The AIDK mentioned provides a single-line model provider swap interface.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-14-vercel-eve-agent-files` |
| Channel | aie |
| Video | [How We Solved Agent Building — Andrew Qu, Vercel](https://www.youtube.com/watch?v=9dYcwOkpCE8) |
| Published | 2026-09-14 |
| Ingested upstream | 2026-09-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

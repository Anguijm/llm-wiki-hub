# Redesign agent-facing CLIs to use non-interactive flags, small tool counts, and skills for progressive discovery

> Back to [[experiments-index]]

Source: **[Designing CLIs for Agents, Not Humans — Pedro Lopez, Airbyte](https://www.youtube.com/watch?v=3wj6sgbi1YA)** · aie · 2026-10-10

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we redesign CLIs intended for agent use to (1) replace interactive prompts with flags and environment variables, (2) minimize exposed tool count using progressive schema discovery, and (3) ship skills files that describe when and how to invoke the CLI, then agents will invoke CLIs reliably without getting stuck awaiting human input, and will discover capabilities without being overloaded with context upfront.

## What they did

Pedro Lopez (Airbyte) described lessons from building Airbyte's MCP and CLI for agent use. Key findings: (1) Keep tool count small — instead of one MCP tool per connector entity/action, expose just two tools (describe-connector for schema, execute for read/write/delete) and use progressive discovery; (2) Use OLAF (non-interactive) mode — CLIs built for humans wait for typed prompts, but agents can't handle that; all inputs must come via flags, env vars, or config files set out-of-band; (3) Ship skills with the CLI — without a skill file describing what the CLI does and when to invoke it, agents won't discover it; skill files should use references to sub-files to avoid bloating context; (4) Log agent mistakes as CLI contract signal — if agents repeatedly misuse a command, the CLI API is unclear and needs redesign rather than more prompting.

## Relevance to YOLO loop

Any CLI tool in our YOLO loop that agents invoke (git, test runners, linters, deployment scripts) should be audited for interactive prompts that block agent execution. Adding skills files for each tool would also improve agent discovery without manual prompt engineering.

## Notes

Trade-off table: MCPs are better for non-technical users and quick prototypes; CLIs are better for long-running tasks, large outputs, and Unix pipe composability.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-10-cli-design-for-agents-olaf-and-skills` |
| Channel | aie |
| Video | [Designing CLIs for Agents, Not Humans — Pedro Lopez, Airbyte](https://www.youtube.com/watch?v=3wj6sgbi1YA) |
| Published | 2026-10-10 |
| Ingested upstream | 2026-10-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

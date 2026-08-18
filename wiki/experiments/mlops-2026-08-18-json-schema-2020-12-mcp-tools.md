# Rewrite MCP Tool Schemas Using JSON Schema 2020-12 Conditional Keywords

> Back to [[experiments-index]]

Source: **[JSON Schema 2020-12 and the Contract for Context | ​Ola Hungerford | MCP Release Party - Seattle](https://www.youtube.com/watch?v=MGfCarfwsUk)** · mlops · 2026-08-18

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we replace prose-heavy tool descriptions with structured JSON Schema 2020-12 conditionals (allOf, if/then/else, $ref), then models will populate tool parameters more accurately because the constraints are machine-readable schema rather than natural-language instructions that must be interpreted.

## What they did

Ola Hungerford, MCP maintainer at Nordstrom, described SEP 2106 which upgraded MCP's input and output schema support to full JSON Schema 2020-12 dialect. She showed real examples from the GitHub MCP server where tool descriptions contained ALL-CAPS prose like 'ALWAYS provide this field' and 'mutually exclusive' because the old schema keywords were too limited. With 2020-12 support, those constraints can now be expressed as allOf conditions, references ($ref), and conditional keywords so the model sees structured constraints rather than freeform instructions.

## Relevance to YOLO loop

Any MCP tools we expose in the dev loop can be hardened by migrating their input schemas to 2020-12 conditionals, reducing the prompt engineering needed to make models call tools correctly and shrinking the gap between intended and actual tool invocations.

## Notes

SEP 2106 is the reference proposal. Check SDK compatibility first—Pydantic/FastMCP historically translated schemas to a limited subset, so verify the SDK version actually passes 2020-12 keywords through to the wire.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-08-18-json-schema-2020-12-mcp-tools` |
| Channel | mlops |
| Video | [JSON Schema 2020-12 and the Contract for Context | ​Ola Hungerford | MCP Release Party - Seattle](https://www.youtube.com/watch?v=MGfCarfwsUk) |
| Published | 2026-08-18 |
| Ingested upstream | 2026-08-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Structure agent customization across three explicit levers: context, tools, and automations with evals

> Back to [[experiments-index]]

Source: **[Harness Engineering Explained in 22 Minutes](https://www.youtube.com/watch?v=UmZytjgs2eo)** · st · 2026-07-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we deliberately engineer each of the three harness levers (context via claude.md and skills folders, tools via MCP and permissions, automations via evals replacing human-in-the-loop review), then agent reliability and throughput will increase because each lever removes a specific bottleneck: poor context causes wrong assumptions, missing tools cause incomplete actions, and absent evals force slow human review of every output.

## What they did

Speaker defined 'harness engineering' as customizing everything built around an AI model to make it more useful, analogized to car components around an engine. He described three levers: (1) Context — using claude.md for persistent cross-conversation instructions and skills folders (containing skill.md prompts, reference docs, assets, and executable code) with progressive disclosure so only relevant context loads; (2) Tools — giving agents access to web search, code execution, file system, and MCP servers, emphasizing matching tool permissions to actual task scope; (3) Automations — replacing human-in-the-loop review with evals (LLM-as-judge or deterministic checks) so the agent can self-iterate overnight, citing Karpathy's auto-research repo as an example where an agent optimized a train.py file better than Karpathy himself by running eval loops autonomously.

## Relevance to YOLO loop

Maps directly to the YOLO loop architecture: claude.md and skills files define the persistent context layer, tool permissions define what the loop can act on, and eval integration is the key unlock for removing the human review bottleneck and letting the loop run autonomously overnight.

## Notes

Bonus lever mentioned (truncated in transcript) is evals. Key mindset shift: instead of asking 'how do I do this task?' ask 'how do I build the harness so the agent does this reliably?' — speaker calls this 'agent empathy': put yourself in the agent's shoes and ask if you'd succeed given only what the agent has.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `st-2026-07-19-harness-engineering-levers` |
| Channel | st |
| Video | [Harness Engineering Explained in 22 Minutes](https://www.youtube.com/watch?v=UmZytjgs2eo) |
| Published | 2026-07-19 |
| Ingested upstream | 2026-07-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

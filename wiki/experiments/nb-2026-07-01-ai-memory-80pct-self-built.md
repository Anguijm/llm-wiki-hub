# Bootstrap a personal AI memory stack by prompting an agent to build it

> Back to [[experiments-index]]

Source: **[I Built My Own AI Memory by Talking to Claude. It Did 80% Itself.](https://www.youtube.com/watch?v=HgAQOkG_v8c)** · nb · 2026-07-01

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we instruct a capable agent (e.g. Claude or Codex) to build 80% of an OpenBrain-style memory stack through conversation alone, then we can stand up a personal persistent-memory system with dramatically less manual setup than in early 2026, because current models follow intent well enough to scaffold file structures, skill definitions, and context frameworks from plain-language description.

## What they did

Jones describes building his 'OpenBrain' personal memory system — a stack that includes wiki-style knowledge connections (inspired by Andrej Karpathy), 'open skills' (domain expertise files), and 'open engine' (an agent-to-agent task interaction framework) — by talking to a Claude or Codex agent. He estimates ~80% of the stack is now buildable purely through conversational prompting, with the agent generating the file structures, memory files, and orchestration layer. The key practice is: pick a recurring situation you are tired of explaining, write down the context that would change the answer, point the agent at a guide, and iterate with feedback ('no, that was wrong, change this').

## Relevance to YOLO loop

Directly maps to the YOLO loop's need for persistent context between sessions. Using the agent to self-construct the memory scaffold means the dev loop can be bootstrapped faster; the 'rent intelligence, own memory' principle also ensures the loop is model-agnostic.

## Notes

Jones references his OpenBrain framework and a linked guide. Key safety note from transcript: establish explicit policy that agent must not act (send, edit, delete) without explicit approval — inspired by the Nikita/Lemonade insurance cautionary tale.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-01 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-01-ai-memory-80pct-self-built` |
| Channel | nb |
| Video | [I Built My Own AI Memory by Talking to Claude. It Did 80% Itself.](https://www.youtube.com/watch?v=HgAQOkG_v8c) |
| Published | 2026-07-01 |
| Ingested upstream | 2026-07-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

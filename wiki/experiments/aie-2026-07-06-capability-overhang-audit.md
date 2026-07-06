# Audit tasks the agent currently fails at by adding code-execution or tool access to expose capability overhang

> Back to [[experiments-index]]

Source: **[Field Guide to Fable — Thariq Shihipar, Anthropic](https://www.youtube.com/watch?v=9fubhllmsBU)** · aie · 2026-07-06

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we systematically test tasks our agent currently fails at reasoning-only and then retry them with code execution or additional tool access enabled, then we will uncover capability overhang — tasks the model already knows how to do but cannot surface without the right tool arm.

## What they did

Thariq used the Pokémon-names-ending-in-AW example to illustrate capability overhang: a chat model fails the task despite knowing all Pokémon names, but Claude Code solves it instantly by fetching all names and writing a filter script. He framed this as the core discovery challenge with Fable — figuring out which previously-impossible tasks are now unblocked by giving the model the right tool rather than by improving the model itself.

## Relevance to YOLO loop

The YOLO loop may be hitting task ceilings that are actually tool-access gaps rather than model-capability gaps. A structured audit — listing failing tasks, hypothesising which tool would unblock them, and testing — would directly expand what the loop can accomplish without waiting for a better model.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-06 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-06-capability-overhang-audit` |
| Channel | aie |
| Video | [Field Guide to Fable — Thariq Shihipar, Anthropic](https://www.youtube.com/watch?v=9fubhllmsBU) |
| Published | 2026-07-06 |
| Ingested upstream | 2026-07-06 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

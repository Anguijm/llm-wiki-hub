# Coordinate Cross-Model Multi-Agent Work via Shared Repo and Message Board

> Back to [[experiments-index]]

Source: **[I Asked Fable 5.1 and GPT-6 Astra to Get Me Out of Copy Paste Hell. The Results Surprised Me.](https://www.youtube.com/watch?v=n5bZHETCiJA)** · nb · 2026-09-10

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we give two different model agents (e.g., Claude for design/coordination, a cheaper model for execution) shared access to a repo and a message board with explicit role definitions, then we can achieve better quality output at lower cost than single-model agentic loops because each model is used at its comparative advantage.

## What they did

Nate described an open multi-agent pattern he uses: both coordinating agents (Claude and Codex/Co-work) share a repo and a message board. Roles are explicitly specified per agent—Claude handles design thinking and coordination, a cheaper execution model (e.g., Luna) handles implementation. He referenced his 'Ringer' tool as one open collaboration point enabling this pattern. He noted this is not what he did for the clipboard app (single agent sufficed) but outlined it as a scaling pattern for more complex builds.

## Relevance to YOLO loop

Maps to the orchestration layer of the YOLO loop: introduces a lightweight coordination protocol (shared repo + message board + role manifest) that could sit above our existing single-agent coding steps for tasks that exceed one agent's context or capability.

## Notes

Luna cited as cheap + fast execution model. Validate current pricing and capability before committing to this model slot.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-09-10-open-multiagent-repo-message-board` |
| Channel | nb |
| Video | [I Asked Fable 5.1 and GPT-6 Astra to Get Me Out of Copy Paste Hell. The Results Surprised Me.](https://www.youtube.com/watch?v=n5bZHETCiJA) |
| Published | 2026-09-10 |
| Ingested upstream | 2026-09-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

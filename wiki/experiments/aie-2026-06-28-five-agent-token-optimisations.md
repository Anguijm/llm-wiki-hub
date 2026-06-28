# Apply five token-reduction techniques to agent loops: prompt caching, difficulty routing, tool-result offload, loop caps, and history trimming

> Back to [[experiments-index]]

Source: **[Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS](https://www.youtube.com/watch?v=uiP88SpCi1Q)** · aie · 2026-06-28

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we systematically apply all five techniques (cache system/tool prompts, route tasks to cheaper models by difficulty, summarise and offload large tool results, cap tool loop iterations, and use a sliding-window conversation manager), then agent token costs will drop significantly with minimal quality loss, because each technique targets a distinct source of redundant tokens that accumulates silently across multi-turn agent sessions.

## What they did

Erik presented five concrete techniques using AWS Strands Agents as the harness. (1) Prompt caching: set cache_prompt=default so the system prompt is only sent in full on the first call; subsequent calls use the cached version. (2) Difficulty routing: use a cheap model (e.g. Claude Haiku) for simple tasks, a mid-tier (Sonnet) for harder ones, and optionally use a cheap model to classify difficulty before routing. (3) Tool-result offloading: store large tool outputs externally, summarise them, and inject only the summary into subsequent loop iterations. (4) Cap tool loops: always set max_iterations to prevent runaway tool calls. Use observability tooling to audit tool call frequency and duration before deploying. (5) History trimming: use a sliding-window conversation manager (e.g. last 10 messages) and summarise older history into a compact context prefix.

## Relevance to YOLO loop

All five techniques apply directly to the YOLO loop's agent harness. The loop already accumulates tool results and conversation history across iterations — capping, caching, and windowing are low-effort wins that compound on every loop cycle.

## Notes

Lightning-talk format — no benchmark numbers given, but techniques are well-established. Difficulty routing and sliding-window history are the highest-leverage starting points for the YOLO loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-28-five-agent-token-optimisations` |
| Channel | aie |
| Video | [Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS](https://www.youtube.com/watch?v=uiP88SpCi1Q) |
| Published | 2026-06-28 |
| Ingested upstream | 2026-06-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

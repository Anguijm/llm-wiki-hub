# Build a Grokbot Router to Swap Underlying LLM Provider Per Agent

> Back to [[experiments-index]]

Source: **[How to Use ANY AI Model in GrokBot](https://www.youtube.com/watch?v=Jq3WcqtakNQ)** · mk · 2026-09-01

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we install a custom router layer inside Grokbot that intercepts outgoing messages and redirects them to a user-specified provider (Codex, Open Router, Claude SDK, free models), then we can use Grokbot's UX, file system, and agent orchestration while paying only for the cheapest or most capable model for each task, because Grokbot agents each have their own computer with a terminal that can authenticate to external provider CLIs and relay responses back into the chat.

## What they did

Mark reverse-engineered Grokbot's architecture to intercept the decision layer before it reaches Grok's own inference. He built 'Grok Router'—a free open-source repo—that adds a /provider slash command to any Grokbot chat. On install, it reads a saved providers file and routes the message to Codex, Open Router (Claude, Gemini, Kimmy, etc.), or free Open Router models. Each bot can have its own provider config. He verified spend by watching his Open Router balance drop in real time. Sub-agents still run through Grokbot; only the main synthesis step is rerouted. He published the repo with an agents.mmd architecture doc and a setup README designed to be fed to any LLM for cross-platform installation.

## Relevance to YOLO loop

Directly relevant to our model-routing problem: we need to cheaply assign the right model to each agent role in our loop. This experiment tests whether Grokbot's operating layer can serve as a stable orchestration shell while we swap inference providers without rebuilding tooling.

## Notes

Highly experimental by author's own admission; tied to a specific Grokbot version. Monitor repo for updates. Free repo linked in video description.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-01 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-09-01-grokbot-model-router` |
| Channel | mk |
| Video | [How to Use ANY AI Model in GrokBot](https://www.youtube.com/watch?v=Jq3WcqtakNQ) |
| Published | 2026-09-01 |
| Ingested upstream | 2026-09-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

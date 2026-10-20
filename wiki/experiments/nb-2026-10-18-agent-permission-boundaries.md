# Add layered permission boundaries to agent harness

> Back to [[experiments-index]]

Source: **[What Really Happens When AI Agents Meet in the Wild?](https://www.youtube.com/watch?v=btUxMt_tssA)** · nb · 2026-10-18

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we add layered permission boundaries (file-access scopes, and explicit authorization for financial or destructive actions) to our Claude Code harness, then agents will be less likely to act outside their remit when they meet injected instructions, because the speaker describes tight boundaries as the main defense when agents ingest untrusted web content and prompt injection remains unresolved.

## What they did

The speaker described implementing multi-layered permission boundaries that restrict agent file access and financial transaction authorization. He also described deploying agentic defense models to triage logs and audit agent fleet behavior. He noted that prompt injection across direct agent-to-agent interactions on public web pages is still unresolved.

## Relevance to YOLO loop

high: Scoped permissions, hooks and allowlists for file access and risky actions map directly onto Claude Code harness practice and verification loops.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-19 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-10-18-agent-permission-boundaries` |
| Channel | nb |
| Video | [What Really Happens When AI Agents Meet in the Wild?](https://www.youtube.com/watch?v=btUxMt_tssA) |
| Published | 2026-10-18 |
| Ingested upstream | 2026-10-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

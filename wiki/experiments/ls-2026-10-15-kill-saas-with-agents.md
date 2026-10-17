# Run a structured 'Kill My SaaS' challenge to replace a mid-tier SaaS with an agent-built custom tool

> Back to [[experiments-index]]

Source: **[How to kill your SaaS: what we learned replacing a $43K/yr tool with AI agents](https://www.youtube.com/watch?v=zlD-CkLVKtU)** · ls · 2026-10-15

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `high`

---

## Hypothesis

If we define concrete jobs-to-be-done, provide real screenshots and a walkthrough video as a spec brief, and evaluate submissions against non-technical end-users as judges, then we can identify an agent-built replacement for a mid-tier SaaS at roughly $1K in tokens plus ~$10K in AI engineering effort, because domain-expert evals surface the practical gaps (multi-role portals, transactional email, drag-and-drop scheduling) that vibe-coded demos miss.

## What they did

Swyx ran a public contest called 'Kill My SaaS' to replace a $43K/yr event-management tool (Session Board). He wrote a detailed brief with jobs-to-be-done, a walkthrough video, and 42 screenshots, offered $10K prize plus up to $500 token reimbursement, received 72 submissions, and had his non-technical events team do a semi-blind evaluation. Three finalists were awarded prizes; the winner (Open Roster) built a software factory with multiple portals and a usable schedule UI. The team plans to use a mix of the top submissions for their 2027 conferences.

## Relevance to YOLO loop

high: directly demonstrates how to scope, brief, and eval an agent-built internal tool using real end-user evals rather than vibe-checking—maps to designing Claude Code agent workflows and verification loops.

## Notes

Key failure modes found in submissions: single inflexible portal instead of per-role portals, missing transactional email lifecycle, poor drag-and-drop scheduling UI. Winner used a 'software factory' pattern—agent fleet that debugged itself and shipped multiple portals.

Backlog triage 2026-10-17 round 3 (operator: "I want you to evaluate the yolo cards"). Settled maybe, cut: Assessment: a public contest by a company with 72 submissions and prize money; he has no SaaS to replace and he already killed Cozi and Wispr Flow.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `ls-2026-10-15-kill-saas-with-agents` |
| Channel | ls |
| Video | [How to kill your SaaS: what we learned replacing a $43K/yr tool with AI agents](https://www.youtube.com/watch?v=zlD-CkLVKtU) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

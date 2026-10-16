# Run REA security audit on a vibe-coded app before multi-user launch to find exposed keys and client-side data leaks

> Back to [[experiments-index]]

Source: **[5 Insane Ways To Actually Use GitHub's #1 Trending Skill](https://www.youtube.com/watch?v=rw0fqnrZgNM)** · ail · 2026-10-15

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we use REA with Claude Code to run a security audit of any app built primarily by AI agents before enabling multi-user access, then we will surface exposed API keys, client-side logic errors, and unauthorized data access paths that code review alone misses, because REA traces actual network requests and execution paths rather than reasoning from static code.

## What they did

AI Labs tested five REA use cases on a demo app: (1) import features from reference apps (Obsidian graph view, Notion board view) into their own app; (2) catch behavioral bugs — REA found that prices shown in-app differed from prices charged, with two accounts seeing wrong totals, server accepting negative seat counts, and a missing billing log entry; (3) performance and layout audit across all screen sizes (found dashboard header overflowing on mobile); (4) agent-generated code security audit — found exposed OpenAI and Stripe API keys accessible without effort, plus a logic bug allowing customer data access without backend auth; (5) (implied by structure). They detailed REA's evidence system: findings tagged 'seen' (REA captured proof), 'guessed' (inferred from clues), or 'unknown' (no backing), preventing guesses from passing as facts. The billing bug was only detectable by REA because the pricing code itself looked correct — the error was only in the final summation step visible in network responses.

## Relevance to YOLO loop

high: REA security and behavioral audits are a verification loop step that should be standard in any Claude Code harness before shipping multi-user features.

## Notes

The billing price discrepancy bug (correct-looking code, wrong runtime behavior) is a compelling argument for making REA behavioral audits a standard pre-launch checklist item. Evidence tagging system (seen/guessed/unknown) is a useful pattern to adopt in other verification workflows.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `ail-2026-10-15-rea-five-use-cases` |
| Channel | ail |
| Video | [5 Insane Ways To Actually Use GitHub's #1 Trending Skill](https://www.youtube.com/watch?v=rw0fqnrZgNM) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Inject user credentials at the HTTP/SQL layer instead of storing them in the agent sandbox

> Back to [[experiments-index]]

Source: **[Your company brain will leak secrets: how we stopped it for big banks — Tanmai Gopal, PromptQL](https://www.youtube.com/watch?v=0uC6u0lJJl4)** · aie · 2026-09-03

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we never store user credentials inside the agent sandbox and instead proxy all data interactions by injecting the requesting user's credentials at the HTTP and SQL layers at runtime, then we will prevent privilege escalation and credential leakage from the company brain, because the agent will only ever be able to act with the permissions of the specific human initiating the interaction rather than with a super-credential.

## What they did

Tanmai Gopal described a two-rule architecture for preventing company-brain secret leaks: (1) never store credentials in the cloud sandbox, and (2) virtualize all interactions with real data by proxying at the HTTP/SQL layer and injecting the calling user's credentials, so the AI behaves as that human for that specific interaction. He said you can derive the entire secure architecture by working backwards from just these two rules.

## Relevance to YOLO loop

If our YOLO loop agents access databases, APIs, or internal tools, we should audit whether agent credentials are stored statically in the sandbox vs. injected per-user per-call. Implementing per-call credential injection would let us safely expand agent access without creating a single high-privilege attack surface.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-03-promptql-no-stored-credentials` |
| Channel | aie |
| Video | [Your company brain will leak secrets: how we stopped it for big banks — Tanmai Gopal, PromptQL](https://www.youtube.com/watch?v=0uC6u0lJJl4) |
| Published | 2026-09-03 |
| Ingested upstream | 2026-09-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

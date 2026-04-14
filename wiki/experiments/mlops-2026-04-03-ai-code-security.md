# Add security scanning to the YOLO build pipeline for AI-generated code

> Back to [[experiments-index]]

Source: **[Practical Security for AI-generated Code]()** · @MLOps · 2026-04-02

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we add automated security scanning (SAST, dependency audit, secrets detection) to the YOLO build pipeline, then we catch vulnerabilities introduced by AI-generated code before they ship because AI models can introduce insecure patterns (hardcoded secrets, SQL injection, XSS) that pass functional tests.

## What they did

MLOps presented practical security measures specifically for AI-generated code — addressing the unique vulnerability patterns that LLMs introduce compared to human-written code.

## Actionable steps

- Add npm audit / pip-audit as a post-build step in the YOLO test pipeline
- Integrate a secrets scanner (e.g., gitleaks, trufflehog) into pre-commit hooks
- Add OWASP top-10 check to Gemini code review prompt (SQL injection, XSS, SSRF)
- Track: how many security issues does the scanner catch per 10 builds?

## Success metric

Security scanning runs on every build; zero shipped vulnerabilities over 20 builds.

## Relevance to YOLO loop

YOLO builds ship fast with AI-generated code. Security scanning is the missing layer between Gemini code review (which focuses on quality) and deployment.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

Built security_scan.py — 22 regex patterns for secrets, XSS, injection, insecure transport, missing CSP, external deps, sensitive localStorage. Integrated into cron test step. Tested on naval-scribe: found 1 HIGH (innerHTML), 1 LOW (missing CSP).

## Notes

Title-only inference. Complements existing Gemini code review with security-specific scanning.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `backlog` | Ingested from Phase 4 YouTube pipeline — title-only inference |
| 2026-04-04 | `done` | Implemented and verified |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-04-03-ai-code-security` |
| Channel | @MLOps |
| Published | 2026-04-02 |
| Ingested upstream | 2026-04-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

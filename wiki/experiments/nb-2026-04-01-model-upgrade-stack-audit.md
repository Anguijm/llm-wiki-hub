# Run a 4-layer stack audit before every major Claude model upgrade

> Back to [[experiments-index]]

Source: **[Anthropic Just Built a Model That Breaks Everything (Claude Mythos Is Nigh)](https://natesnewsletter.substack.com/p/anthropic-just-built-a-model-that)** · @NateBJones · 2026-04-01

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we audit each layer of the YOLO build loop (system prompts, retrieval, verification, orchestration) before upgrading to a new Claude model, then we remove brittle workarounds before they break because stronger models expose — not hide — architectural debt built around weaker predecessors.

## What they did

Nate analyzed Claude Mythos (Anthropic's new capability tier above Opus) and described how production AI stacks built around model weaknesses become brittle when the model improves. He proposed a 4-question diagnostic audit (one per stack layer) and a 'simplification pattern': strip workarounds proactively because complex prompt engineering that patched around gaps in weaker models becomes noise for stronger ones. The Klarna case study showed the cost of ignoring this principle.

## Actionable steps

- Before the next major Claude model upgrade, list all workarounds in skills/, program.md, and CLAUDE.md that exist because of prior model limitations
- Map each workaround to the stack layer it patches: system prompt, retrieval, verification gates, or orchestration logic
- For each workaround, test whether it is still needed or now handled natively by the upgraded model
- Remove or simplify confirmed-obsolete workarounds before deploying to production builds

## Success metric

At least 3 obsolete workarounds identified and removed before next major model upgrade. Post-upgrade Gemini audit finds fewer bugs vs. non-audited baseline.

## Relevance to YOLO loop

skills/ and program.md contain rules written to patch around old model behaviors. As Claude 4.x capabilities improve, some of these become dead weight that confuses rather than guides. A pre-upgrade audit keeps the loop lean and avoids the Klarna anti-pattern.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

Created model-upgrade-audit.md — 4-layer checklist (prompts, retrieval, verification, orchestration) with specific files to audit, checks per layer, and post-audit validation protocol. Run before any model swap.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `done` | Audit template built and committed |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-04-01-model-upgrade-stack-audit` |
| Channel | @NateBJones |
| Video | [Anthropic Just Built a Model That Breaks Everything (Claude Mythos Is Nigh)](https://natesnewsletter.substack.com/p/anthropic-just-built-a-model-that) |
| Published | 2026-04-01 |
| Ingested upstream | 2026-04-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Draft and enforce a pre-incident AI likeness and voice policy for team outputs

> Back to [[experiments-index]]

Source: **[You Can't Tell If I'm Real Anymore. And That's Now YouTube's Problem Too.](https://www.youtube.com/watch?v=lWbtvC0Hn18)** · nb · 2026-06-20

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we define explicit policy rules before a voice or likeness cloning incident occurs (who can authorize a clone, what gets logged, what is never permitted), then we avoid reactive damage-control decisions because policy created under pressure defaults to whatever resolves the immediate mess rather than protecting long-term trust.

## What they did

Nate argued that companies should 'create the policy before the scandal,' specifying who can approve a voice clone, who can use an employee likeness, what happens when someone leaves the organization, what gets labeled, what gets logged, and what is categorically never allowed. He framed the absence of pre-defined policy not as a neutral state but as a decision to let future incidents set the rules by default.

## Relevance to YOLO loop

Our dev loop increasingly uses voice interfaces, agent personas, and synthetic narration in demos and tooling. Establishing a written policy for when and how synthetic voice or avatar representations of team members can be used in outputs, demos, or shipped features is directly actionable and prevents ambiguity as those capabilities scale.

## Notes

Low effort because the deliverable is a policy document, not a technical build. Could be combined with the trust-stack metadata card into a single governance sprint. Nate's checklist (approve, use, log, label, prohibit) provides a ready-made outline.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-06-20-voice-clone-consent-policy` |
| Channel | nb |
| Video | [You Can't Tell If I'm Real Anymore. And That's Now YouTube's Problem Too.](https://www.youtube.com/watch?v=lWbtvC0Hn18) |
| Published | 2026-06-20 |
| Ingested upstream | 2026-06-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

# Use a multi-message prompt sequence with in-thinking sampling and random selection to force Astra into diverse creative outputs

> Back to [[experiments-index]]

Source: **[How to Make Astra More Creative](https://www.youtube.com/watch?v=YmSnzMDrYsw)** · eh · 2026-09-19

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we send Astra a sequential three-prompt workflow that (1) samples 50 possibilities inside its thinking trace, picks 5 randomly, (2) generates 20 fusions/alternatives/combinations of those 5 with minimal token spelling, then picks 5 randomly, and (3) selects one and builds it with full UX detail, then we get meaningfully varied creative outputs across independent runs because random selection at each trimming step breaks the lowest-common-denominator convergence that Astra defaults to.

## What they did

The presenter ran experiments to overcome Astra's tendency to produce near-identical idea sets when asked for creative outputs. He tested multiple strategies including: asking Grok to simulate an artist's struggle to generate image prompts (which produced variability), providing a process definition alongside a sparse creative prompt, and the multi-message Astra workflow — message 1: sample 50 possibilities in thinking using minimal tokens then pick 5 randomly with no preference; message 2: generate 20 fusions/alternatives/combinations/promising tangents, consider what humans find interesting (not just 'interesting'), randomly pick 5; message 3: pick one, build it with maximum user-friendliness, distinctive visual/experiential style, establish central interaction early. He ran this 8 times and observed that all 8 HTML canvas simulation outputs were meaningfully distinct from each other, validating the approach. He noted this process is costly with Astra and can be automated by having Codex send the sequential messages to separate Astra instances.

## Relevance to YOLO loop

Directly applicable when a YOLO loop step requires genuine creative divergence rather than predictable generation — the random-trim-at-each-stage pattern is reusable for any ideation node in a pipeline to prevent mode collapse.

## Notes

Prompt sequence available on echohive.ai under Experiments > How to Make Astra Creative and on Patreon (8 levels of originality prompts). Key insight: say 'what humans find interesting' not just 'interesting' — Astra responds better to the former framing.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `eh-2026-09-19-astra-creative-prompt-sequence` |
| Channel | eh |
| Video | [How to Make Astra More Creative](https://www.youtube.com/watch?v=YmSnzMDrYsw) |
| Published | 2026-09-19 |
| Ingested upstream | 2026-09-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

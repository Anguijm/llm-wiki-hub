# Use an existing app or artifact as a living PRD instead of writing one from scratch

> Back to [[experiments-index]]

Source: **[I Tested the Viral Reverse Engineer Anything Skill. What You Need to Know.](https://www.youtube.com/watch?v=rL5tw6h78zo)** · nh · 2026-10-15

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we point a coding agent at a working app or example output and instruct it to analyze and replicate the functionality, then the resulting build will be more specific and higher quality than builds driven by a written PRD because the agent receives unambiguous, concrete specification rather than a prose description subject to interpretation.

## What they did

Nate tested the Reverse Engineer Anything (REA) GitHub repo, which uses an MCP server and Ghidra to decompile apps and extract their functional structure. He compared agent outputs with and without the REA repo and found that REA-augmented runs finished slower but produced significantly better results. He also showed prior personal examples: feeding 30 Instagram reels to an agent to extract an editing style, cloning Loom's bubble-recording functionality (not its UI), and replicating app features from SandCastle. He framed the core insight as 'the app is the PRD.'

## Relevance to YOLO loop

Directly applicable to feature scoping in our loop: instead of writing feature specs, we can feed reference implementations to the agent, reducing ambiguity and spec-writing overhead while improving output fidelity.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-10-15-reverse-engineer-existing-app-as-prd` |
| Channel | nh |
| Video | [I Tested the Viral Reverse Engineer Anything Skill. What You Need to Know.](https://www.youtube.com/watch?v=rL5tw6h78zo) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

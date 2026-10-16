# Use REA (Reverse Engineer Anything) MCP to audit and inform Claude Code harness design

> Back to [[experiments-index]]

Source: **[Your Vibe-Coded App Can Look Right And Fall Apart After Launch. REA Shows You How Real Teams Build.](https://www.youtube.com/watch?v=PseF3LyXQ04)** · nb · 2026-10-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we connect the REA MCP server to Claude Code and systematically reverse-engineer reference apps before building features, then our agent will produce implementations that match real behavior rather than visual approximations, because REA exposes the actual request/response contracts and code paths that screenshots alone miss.

## What they did

The speaker walked through REA, a 100k-star GitHub tool that plugs into Claude Code or Codex as an MCP server and lets the agent open any installed or web app, trace network requests, follow code paths, and produce annotated explanations of how features actually work. He demonstrated it on an authenticator app (TOTP algorithm), described a developer using it to investigate QuickBooks Desktop before building an independent accounting app, and outlined two usage modes: non-devs using it as an X-ray to understand what to build, and devs using it as a targeted accelerator to answer 'how did they do that?' He noted it only exposes client-side code, not server-side, and recommended telling the agent how deep to go to avoid burning tokens.

## Relevance to YOLO loop

high: REA is a Claude Code MCP extension that directly enhances the agent harness by grounding feature research in real implementations rather than speculation.

## Notes

Speaker also mentioned a forthcoming Substack post with specific 'dig points' for getting started with REA. Worth tracking.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-10-15-rea-xray-vision-workflow` |
| Channel | nb |
| Video | [Your Vibe-Coded App Can Look Right And Fall Apart After Launch. REA Shows You How Real Teams Build.](https://www.youtube.com/watch?v=PseF3LyXQ04) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

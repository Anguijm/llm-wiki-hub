# Connect Higgsfield MCP to Claude and Drive Full Brand Asset Generation from a Single Prompt

> Back to [[experiments-index]]

Source: **[Higgsfield Just Turned Claude Into a Creative Agency](https://www.youtube.com/watch?v=xn6Z5PYyAIE)** · NateHerk · 2026-05-05

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we connect the Higgsfield MCP to Claude and issue a single high-level brand-building prompt, then Claude can autonomously research, define brand identity, and generate a full suite of product photos, ad creatives, and UGC videos without manual tool-switching, because the MCP exposes Higgsfield's image and video generation models as callable tools that Claude can chain together in one context window.

## What they did

Nate walked through connecting Higgsfield to Claude via a custom MCP connector in Claude's web settings (Settings → Connectors → Add Custom Connector, paste the Higgsfield MCP command, authenticate via OAuth). He then issued a single prompt — 'build me a headphone brand from scratch: do research, build branding, build a product catalog, and for each product generate a product photo, an Instagram ad, and a UGC video' — and Claude autonomously called Higgsfield tools to produce all assets. He also demonstrated a scaling automation loop: use Claude Code routines (scheduled prompt injections) to populate a Google Sheet with 50 new video ideas every Sunday, then trigger a Monday morning routine to pick 30 blank-status rows, generate all assets, and write back URLs and job IDs — waking up to a completed batch. The pipeline can optionally chain into a posting scheduler like Publer or Meta Ads Manager.

## Relevance to YOLO loop

Shows how to wrap an external creative-generation API as an MCP tool and let Claude orchestrate multi-step asset pipelines — directly analogous to how the YOLO loop could expose code-generation or deployment tools as MCP endpoints and have Claude drive end-to-end feature delivery from a single intent prompt. The Google Sheet status-tracking pattern is a lightweight alternative to a full issue tracker for managing batched agentic work.

## Notes

Nate noted that video text rendering (e.g. album metadata on covers) is still unreliable — workaround is to use a plain logo/name overlay instead of detailed text. The routine scheduling feature in Claude Code is the key lever for the automation layer; he has a dedicated routines video linked in the description that covers gotchas.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-05 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-05-05-higgsfield-claude-mcp-creative-agency` |
| Channel | NateHerk |
| Video | [Higgsfield Just Turned Claude Into a Creative Agency](https://www.youtube.com/watch?v=xn6Z5PYyAIE) |
| Published | 2026-05-05 |
| Ingested upstream | 2026-05-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

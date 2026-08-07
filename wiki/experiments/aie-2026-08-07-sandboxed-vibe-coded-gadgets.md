# Run AI-Generated App Code in Null-Origin Iframe + Durable Object Sandbox to Eliminate XSS Risk

> Back to [[experiments-index]]

Source: **[Gadgets: Personal app vibe coding that is actually safe — Kenton Varda, Cloudflare](https://www.youtube.com/watch?v=RmS5s6Wbin4)** · aie · 2026-08-07

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we execute vibe-coded client UI inside a null-origin iframe sandbox with strict CSP and route all server calls through a sandboxed Durable Object that cannot reach external services, then XSS and injection bugs in AI-generated code become harmless, because the sandbox prevents the code from leaking data or accessing cookies regardless of what the model produced.

## What they did

Kenton Varda described Cloudflare's 'Gadgets' prototype: an AI codegen system where Claude generates both a client (SVG/HTML) and a server (Cloudflare Workers Durable Object). The client runs in a null-origin iframe with CSP that blocks all external communication; the only channel out is postMessage to the parent frame, which is wired via Cap'n Proto RPC to the Durable Object. The Durable Object itself is similarly sandboxed from the broader internet. This means any XSS or injection vulnerability in the AI-generated code cannot exfiltrate data. He ran the entire stack locally on workerd (the open-source Cloudflare Workers runtime) and demoed Home Assistant and Spotify connectors. The project was pulled back from open-source release at the last minute to become a formal Cloudflare product.

## Relevance to YOLO loop

Relevant if the dev loop needs to execute AI-generated code snippets or mini-apps for users without full security review. The iframe + Durable Object pattern could be applied to any internal tool that lets AI generate runnable artifacts, giving a safe execution sandbox without container overhead.

## Notes

Transcript truncated (6k chars elided). Full external-services safe-communication system was not described due to time. Kenton mentioned it would be open-sourced 'soon' as a formal Cloudflare product — worth watching for the repo. No transcript for 'Compression at the Edge' or 'Local Models: Trust, Control, Optimization' videos; skipped as insufficient signal without transcripts.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-07 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-07-sandboxed-vibe-coded-gadgets` |
| Channel | aie |
| Video | [Gadgets: Personal app vibe coding that is actually safe — Kenton Varda, Cloudflare](https://www.youtube.com/watch?v=RmS5s6Wbin4) |
| Published | 2026-08-07 |
| Ingested upstream | 2026-08-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

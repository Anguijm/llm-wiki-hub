# Build a domain-specific support agent using your own product's API to simultaneously dogfood the product and automate tier-1 support

> Back to [[experiments-index]]

Source: **[We Built an AI Support Agent That Resolves 80% of Tickets — AssemblyAI](https://www.youtube.com/watch?v=pyvRID_CZZU)** · aie · 2026-10-05

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we build our support/onboarding agent using the same APIs our users consume, then we achieve two outcomes simultaneously—automated resolution of high-volume repetitive tickets and a continuously updated empathy model for how our own APIs behave in production—because AssemblyAI went from 10% resolution rate with an off-the-shelf bot to 80% resolution rate by building a custom agent with full access to their system prompt, tools, and knowledge base, and the engineer who built it gained direct production experience with the voice agent API.

## What they did

Matt Lawler from AssemblyAI described going from 1,000 API signups/day with only one onboarding engineer, buying an off-the-shelf support bot (10% resolution rate), then building a custom agent called Joey using their own voice agent API. Joey handles tier-1 support questions including HIPAA BAA inquiries, with voice interaction so users simultaneously experience the product they're asking about. The rebuild gave them full control over system prompt, tools, and knowledge base. Matt's call to action: FTEs should automate themselves out of repetitive work and build using the exact same APIs their customers use.

## Relevance to YOLO loop

The dogfooding principle applies directly: any agent we build to assist with the YOLO loop should itself use the same agent infrastructure we're developing, generating real production signal. The 10%→80% resolution rate jump from gaining system prompt and tool access is a strong argument for building custom over buying off-the-shelf for domain-specific tasks.

## Notes

Key failure mode of off-the-shelf bot: no access to system prompt, tools, or iteration speed. Key success factor of custom build: full control + dogfooding the product. Joey shipped that week; Matt offered live feedback sessions at the booth. Voice interface serves as a live product demo simultaneously.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-05 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-05-support-agent-dogfood-build` |
| Channel | aie |
| Video | [We Built an AI Support Agent That Resolves 80% of Tickets — AssemblyAI](https://www.youtube.com/watch?v=pyvRID_CZZU) |
| Published | 2026-10-05 |
| Ingested upstream | 2026-10-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

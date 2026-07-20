# Store agent memory keys only on client device and attest workload integrity via a public transparency log before key sharing

> Back to [[experiments-index]]

Source: **[Privacy-Preserving Intelligence — Steve Korshakov, Bee (acq. Amazon)](https://www.youtube.com/watch?v=IvE8n-ylFYY)** · aie · 2026-07-20

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we architect a persistent agent's encryption so that the symmetric key never leaves the user's device except after a successful remote attestation of the specific server workload against a public transparency log, then no internal operator (including cloud provider employees) can access user data, because the cryptographic proof chain ties key release to a verified, auditable code hash rather than organisational trust.

## What they did

Steve Korshakov described Bee's (now Amazon) privacy architecture for a wearable AI that captures ~10M tokens/year of sensitive personal data. Key design decisions: (1) encryption key persists only on user's phone, never in backend storage; (2) backend runs in confidential compute; (3) before any key sharing, the phone runs a remote attestation pipeline that verifies the running workload hash is present in a public transparency log (using Sigstore); (4) keys have a forced 7-day expiry to limit blast radius; (5) a two-tier deployment system means no single internal team can ship code to production unilaterally — a separate privacy team's signing key is hardcoded into the client and must countersign any deployment; (6) the entire system is ~20k lines of memory-safe code to keep the auditable surface small.

## Relevance to YOLO loop

Relevant if our YOLO loop agents handle sensitive user or customer data: the transparency log + attestation pattern is the architecturally defensible answer to 'how do we prove to users that their data is private even from us.'

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-20-e2e-encryption-personal-agent` |
| Channel | aie |
| Video | [Privacy-Preserving Intelligence — Steve Korshakov, Bee (acq. Amazon)](https://www.youtube.com/watch?v=IvE8n-ylFYY) |
| Published | 2026-07-20 |
| Ingested upstream | 2026-07-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home

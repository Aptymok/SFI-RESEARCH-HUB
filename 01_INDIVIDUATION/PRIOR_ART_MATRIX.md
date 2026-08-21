# SFI-A Prior Art Matrix — 2026-08-20

Purpose: prevent SFI-A from rediscovering existing work and define the smallest defensible novelty claim.

## Existing lines and what they already cover

| Line | Representative work | What it already measures | What it does NOT by itself settle |
|---|---|---|---|
| Agent memory | STATE-Bench (Microsoft, 2026) | whether memory improves realistic agent performance | whether two transformed configurations should be treated as the same operational AI system |
| Memory-to-action | Mem2ActBench (ACL 2026) | whether long-term memory is actively used for tool/action parameterization | operational identity across changes in model, authority, tools, policy, provenance, or deployment |
| Interrupted execution continuity | ContinuityBench (OpenReview, 2026) | recovery from interrupted state and handoff fidelity | general identity relation across heterogeneous transformations |
| Behavioral continuity | ContinuityBench / behavioral drift work | stability of identity/goal/abstraction/style under adversarial interaction | whether behavioral continuity is sufficient or necessary for system identity |
| Technical identity / provenance | IETF Agent Record and related agent-identity drafts | authenticated/delegated identity, append-only history, provenance, continuity records | whether authenticated identity equals operational continuity under substantive system change |
| AI identity gap analysis | Otsuka et al. 2026 | substrate, persistence, verifiability, legal standing; structural gaps | an experimentally accountable measurement relation for SAME/DISTINCT/UNRESOLVED across transformation classes |

## SFI-A discriminant target

SFI-A does not claim that memory, provenance, behavior, authorization, or model identity are individually novel.

Its candidate contribution is narrower:

> Given two observations of an AI system under a declared observation boundary and purpose, can an explicit combination of relational continuity, boundary continuity, response continuity, lineage/provenance, authority, and trajectory history improve operational individuation over strong single-dimension and established baselines?

The admissible outputs are:
- SAME for the declared purpose;
- DISTINCT for the declared purpose;
- UNRESOLVED under available evidence.

## Strong null / reduction hypotheses

1. Identifier sufficiency: persistent technical identity or version record is enough.
2. Model sufficiency: model identity explains essentially all relevant continuity.
3. Memory sufficiency: continuity is primarily a memory/state-retention problem.
4. Behavioral sufficiency: stable behavior under stress is enough to define identity.
5. Purpose dependence: there is no transferable individuation relation; every identity decision is purpose-local.
6. Composite redundancy: any SFI-A composite score adds no information beyond the best existing dimension-specific baseline.

## Novelty survival rule

SFI-A survives as a distinct contribution only if at least one preregistered multi-dimensional operational-individuation rule provides reproducible incremental discrimination or prediction beyond the strongest matched baseline, while preserving calibrated UNRESOLVED states and purpose dependence.

If not, the manuscript must collapse into a synthesis/taxonomy or be withdrawn as a novel measurement proposal.

# SFI-A — Individuation as a Measurement Problem

## Scientific role

SFI-A treats individuation as a measurement problem for longitudinal sociotechnical and AI systems. Its primary question is whether two observations warrant treatment as the same continuing operational system, distinct systems, or unresolved under an explicitly declared observation boundary.

The canonical manuscript framing is:

**Individuation as a Measurement Problem — A formal observability framework for separating system, agent, artifact, and evidence in sociotechnical environments.**

The project must distinguish at least:
- system;
- model;
- agent/runtime instance;
- artifact;
- evidence object;
- memory/history;
- tools and external services;
- permissions/authority;
- governance/policy;
- environment and observation boundary.

## Primary validation domain

The primary domain is AI/sociotechnical operational identity across controlled changes in model, memory, tools, authority, policy, environment, provenance, and trajectory.

The primary measurement object is:

`H_id(A,B | Omega)`

using declared evidence families such as relational continuity, boundary continuity, functional-response continuity, lineage/provenance continuity, trajectory memory, scale, and characteristic time.

## Biological transfer domain

Cell-tracking work is retained as `A-TRANSFER-BIO`. It is an external adversarial transfer domain with independent lineage reference, not the primary scientific object of SFI-A. Existing CTC permission requests and runner code are preserved for this role.

## Independence constraint

The paper must remain valid if System Friction Theory is false. SFT terminology is excluded from the core definitions unless explicitly marked as later interpretation.

## Required package

- `manuscript/EN/` — canonical submission-language manuscript.
- `manuscript/ES/` — semantically aligned Spanish version.
- `protocols/` — operational definitions and test procedures.
- `instruments/` — measurement definitions and code/specification.
- `data/` — raw/processed/synthetic according to governance.
- `notebooks/` — reproducible analysis.
- `results/` — machine-readable outputs.
- `figures/` — generated figures only; source data must be traceable.

## Minimum claim chain

`observation boundary -> entity/system candidate -> state representation -> continuity evidence -> trajectory/response test -> null/baseline comparison -> identity state {same | distinct | unresolved}`

## Falsifiable alternatives

- identifier/version continuity is sufficient;
- model continuity captures essentially all useful operational identity;
- no transferable operational individuation relation exists beyond purpose-specific conventions.

## Release condition

Do not mark v1.0 until operational definitions, falsifiers, null/baseline comparison, AI-domain perturbation evidence, limitations, provenance, and reproducible evidence package are complete. Cross-domain generality may not be claimed from biological transfer alone.

See `00_REGISTRY/ADR-004_RESTORE_SFI_A_SCOPE.md` for the recorded scope correction.
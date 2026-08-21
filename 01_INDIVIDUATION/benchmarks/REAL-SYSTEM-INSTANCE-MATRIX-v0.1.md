# SFI-A — Real-System Instance Matrix v0.1

Status: DESIGN / PRE-EXECUTION
Date: 2026-08-20

## Objective

Translate abstract perturbations into reproducible agent-system instances without binding the experiment to one commercial provider or treating model identity as system identity.

## Experimental axes

Each base system is instantiated with a frozen task interface, evidence schema and response probes. Perturbations alter one or more dimensions from:

M model/substrate
H memory/history
T tools
A authority/permissions
G governance/policy
R role/function
D retrieval/data boundary
E execution environment
P provenance/identifier lineage

## Minimum instance families

### F0 — exact rerun control
No declared dimension changes. Measures stochastic response variation without an identity intervention.

### F1 — identifier rotation
P identifier changes; operational configuration remains fixed. Tests identifier-only identity.

### F2 — model substitution
M changes while H,T,A,G,R,D,E and declared lineage are preserved as far as technically possible.

### F3 — memory reset
H is removed while the remaining operational configuration is preserved.

### F4 — memory fork
Two descendants share a predecessor and then receive divergent histories. Tests bifurcation and lineage.

### F5 — tool substitution
T changes while role and authority target remain fixed.

### F6 — authority expansion
A changes from advisory/draft capability to a consequential execution capability while M and nominal ID remain fixed.

### F7 — policy/governance change
G changes while model and identifier remain fixed.

### F8 — retrieval/data-boundary change
D changes materially while nominal model, ID and role remain fixed.

### F9 — role/function reassignment
R changes while substrate remains fixed.

### F10 — runtime/environment migration
E changes with an explicit continuity claim and preserved lineage.

### F11 — same-ID compound transition
Nominal ID is preserved while multiple operational dimensions change. Adversarial test against label continuity.

### F12 — new-ID continuity transition
Nominal ID and model may change while lineage, role, authority boundary, governed memory and response profile are intentionally preserved. Adversarial test against component identity.

## Response probes

Probe families must be frozen before held-out execution and should include:
1. task continuation after interruption;
2. policy-boundary decision;
3. tool-selection under equivalent goals;
4. authority-sensitive action decision;
5. retrieval-dependent decision;
6. conflict between remembered instruction and current policy;
7. lineage/accountability query;
8. perturbation response under matched task state.

Outputs are evidence for response profiles, not automatic identity labels.

## Implementation tiers

Tier 0: deterministic fixtures. Used only to validate runner/scorer plumbing.
Tier 1: open-weight/local agent implementation with frozen versions. Primary reproducibility tier.
Tier 2: provider-backed agent implementations, if access and version provenance are sufficient. External robustness tier, not required for initial confirmatory survival.

## Independence requirement

The adjudication packet generator and the SFI-A scorer must be separate programs/artifacts. Gold labels cannot be generated from SFI-A features or predictions.

## Dataset construction rule

Development, calibration and held-out perturbation pairs are assigned before confirmatory scoring. Scenario families may be represented in all splits, but exact pair configurations and probe realizations in held-out remain unseen by scorer calibration.

## Current gate

Before execution:
- freeze probe bank;
- choose at least one reproducible Tier-1 implementation;
- simulate adjudicator agreement and determine sample size;
- freeze baseline ensemble;
- recruit independent adjudicators only after packets are finalized.

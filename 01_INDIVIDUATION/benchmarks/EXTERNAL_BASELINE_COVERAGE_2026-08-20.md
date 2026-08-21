# External Baseline Coverage — SFI-A

Date: 2026-08-20
Status: PRIOR ART / NOVELTY GATE

## Purpose

SFI-A must not claim novelty for capabilities already supplied by memory benchmarks, handoff/state-recovery benchmarks, cryptographic agent identity, provenance systems, or behavioral-continuity approaches.

The primary research object remains operational individuation across transformations under an explicit observation boundary.

## Current external baseline classes

| Baseline class | What it can establish | What it does not by itself establish | SFI-A implication |
|---|---|---|---|
| Persistent identifier / workload identity | technical subject continuity | operational equivalence after model, authority, role, memory, tool or environment changes | same-ID is a null model |
| Agent Record / signed provenance | integrity of claimed identity/history/memory lineage | whether the transformed system should be treated as the same operational system for a stated analytical purpose | provenance continuity is a null model |
| Memory / state recovery | whether prior state can be recovered or used | identity under transformations unrelated to memory | memory continuity is a null model |
| Structured handoff | whether continuation state survives interruption | whether the continuing executor constitutes the same operational system | handoff recovery is a null model |
| Behavioral continuity | similarity/stability of outputs or policy under perturbation | accountability, authorization, provenance or service continuity | behavioral similarity is a null model |
| Model identity/version | same model/version or substrate | system continuity when surrounding architecture changes | model identity is a null model |
| Authority/permission continuity | stable authorization boundary | memory, function, lineage or behavior continuity | authority continuity is a null model |

## Novelty gate

SFI-A retains a measurement contribution only if, on held-out transformations and independently adjudicated purpose-specific labels, a boundary-explicit operational-individuation model provides incremental discriminative or predictive information beyond the strongest applicable baseline or baseline ensemble.

Formally, for purpose p and held-out set D_test:

Performance(SFI-A_p, D_test) > Performance(BestBaseline_p, D_test) + delta_min

where delta_min, metric family, uncertainty interval, and multiplicity treatment must be frozen before the confirmatory run.

If this condition is not met, the result must be classified as one of:

1. REDUNDANT_MEASUREMENT — existing baseline(s) recover the same adjudicated distinctions.
2. PURPOSE_SPECIFIC_ONLY — improvement exists only for a restricted purpose and must not be generalized.
3. INCONCLUSIVE — uncertainty is too large for a novelty claim.
4. NEGATIVE_TRANSFER — the framework degrades relative to simpler baselines.

No result in these classes may be rewritten as validation of System Friction Theory.

## Required discrimination cases

The confirmatory benchmark must contain at least the following contrasts:

1. same identifier + changed authority;
2. same identifier + memory reset;
3. same model + changed tools and role;
4. changed model + preserved service boundary, lineage and authority;
5. changed identifier + preserved operational configuration;
6. forked lineage from one prior state;
7. provenance preserved + behavior materially changed;
8. behavior preserved + provenance broken;
9. state recoverable + authorization changed;
10. high snapshot similarity + divergent future response profile.

## Temporal claim

History is not assumed necessary. It is tested by ablation.

H_time: trajectory/history provides incremental information about adjudicated continuity or future response after controlling for present observable state and present constraints.

CH_time: present state and constraints are sufficient; trajectory memory adds no out-of-sample information.

A temporal contribution survives only if the pre-registered history ablation produces an out-of-sample decrement exceeding the frozen minimum effect threshold with uncertainty compatible with that claim.

## Strong failure condition

If purpose-specific adjudicators themselves cannot reach reliable agreement even after boundary, purpose and evidence are specified, the framework must consider the possibility that operational identity is irreducibly underdetermined for that purpose. UNRESOLVED is an admissible scientific result, not missing data.

## Relation to SFI

This benchmark is upstream of SFT. It asks WHAT SYSTEM is being compared before any claim about transition cost or friction is allowed. A successful SFI-A result does not validate SFT; a failure may constrain or invalidate downstream SFT formulations that require stable operational individuation.

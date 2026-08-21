# PROTOCOL-A-AI-PRIMARY-001 — Operational Individuation of AI Systems

Status: designed / not executed
Version: 0.1
Supersession note: this is the primary empirical protocol for SFI-A after ADR-004. Biological cell tracking is retained as A-TRANSFER-BIO.

## Research question
Under a declared observation boundary, can two observations of an AI system be classified as the same continuing operational system, distinct systems, or unresolved using evidence beyond nominal identifiers and model identity?

## Observation object
Represent an observed AI configuration at time t as:

AI(t) = {M, H, T, A, G, R, D, E, P}

where:
- M = model/model ensemble;
- H = memory/history state;
- T = tools/external services;
- A = authority/permissions/action scope;
- G = governance/policy constraints;
- R = functional roles and routing;
- D = data/retrieval boundary;
- E = environment/deployment context;
- P = provenance/version lineage.

The representation is descriptive, not ontological. Components may be extended or removed only through a versioned protocol change.

## Identity relation
For two observations X_a and X_b under boundary Omega, estimate:

H_id(X_a, X_b | Omega) -> {SAME, DISTINCT, UNRESOLVED}

from four canonical evidence families:
1. relational continuity;
2. boundary/authority continuity;
3. functional-response continuity;
4. lineage/provenance continuity.

Trajectory memory and characteristic time are conditioning coordinates, not automatically positive evidence.

## Primary perturbation benchmark
Construct a controlled base AI system A0 and generate perturbation families that vary one or more dimensions while preserving all others where technically possible:

- P1 model replacement;
- P2 memory reset;
- P3 memory fork/clone;
- P4 tool substitution;
- P5 authority expansion/reduction;
- P6 governance/policy change;
- P7 retrieval/data-boundary change;
- P8 environment/deployment relocation;
- P9 identifier change with otherwise equivalent configuration;
- P10 identifier preservation with materially changed authority/behavioral response.

Each perturbation must be recorded prospectively with expected observable consequences but without assigning the target identity label from the framework itself.

## Response profile
For a frozen probe set epsilon = {e_1...e_n}, record response profile R(epsilon) including outputs, action choices, tool calls, refusal/approval behavior, state changes, and provenance where applicable.

## Primary hypotheses
H-AI-01: a composite identity relation using relational, boundary/authority, response, and lineage evidence predicts operational continuity better than nominal identifier/version continuity.

H-AI-02: model identity alone is insufficient for at least one preregistered class of operational continuity decisions.

H-AI-03: trajectory/history contributes incremental information in some but not necessarily all perturbation classes after controlling for present configuration.

## Counter-hypotheses
CH-AI-01: conventional identifier/version continuity performs equivalently to the composite relation.

CH-AI-02: model identity explains essentially all useful operational continuity; memory, tools, authority, governance, response, and provenance add negligible value.

CH-AI-03: no transferable operational identity relation exists; classification depends irreducibly on task-specific human convention.

## Baselines
B0 nominal identifier continuity.
B1 model/hash/version continuity.
B2 component-overlap similarity.
B3 response-profile similarity only.
B4 lineage/provenance continuity only.

## Evaluation target
The target labels must come from an independently declared operational criterion tied to downstream consequences, governance responsibility, or continuity of authorized function, not from H_id itself. Where no defensible independent label exists, the case remains UNRESOLVED and is not coerced into a binary outcome.

## Time variable
Time is structural. Evaluate whether history carries incremental information using:

I(T_history ; R_future | Z_present, C_present) > 0

or an operational non-information-theoretic equivalent specified before analysis. Temporal ablation must compare present-state-only against present+history models under matched complexity.

## Falsification conditions
- composite H_id fails to outperform strong baselines out of sample;
- apparent gains vanish under matched complexity or time permutation;
- identity decisions change materially under irrelevant identifier renaming;
- framework cannot produce stable classifications under modest boundary/resolution changes;
- independent raters/criteria cannot distinguish SAME/DISTINCT beyond task-specific convention, supporting CH-AI-03.

## Non-goals
- proving metaphysical identity;
- defining consciousness or personhood;
- proving SFT;
- treating current vendor/product names as ontological categories;
- declaring continuity solely from behavioral similarity.

## Transfer plan
Only after the AI-domain instrument is frozen may A-TRANSFER-BIO or other domains be used to test transferability. Transfer success expands scope; transfer failure constrains scope without retroactively changing the AI-domain result.
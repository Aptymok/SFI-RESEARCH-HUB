# ADR-004 — Restore SFI-A to operational individuation of sociotechnical/AI systems

Date: 2026-08-20
Status: ACCEPTED
Supersedes: the temporary interpretation that treated biological cell tracking as the primary empirical object of SFI-A.

## Original object
SFI-A was defined as a formal observability framework for separating system, agent, artifact, and evidence in longitudinal sociotechnical environments. Its target problem is operational individuation: under a declared observation boundary, when do two observations warrant treatment as the same continuing system, distinct systems, or unresolved?

## Divergence observed
During empirical-design work, the search for a domain with independent lineage ground truth shifted the operational focus toward cell tracking. That move was methodologically useful for constructing a falsifiable transfer benchmark, but it incorrectly promoted the benchmark domain into the primary scientific object.

The divergence was therefore:

`need for independent ground truth -> biological tracking benchmark -> accidental narrowing of SFI-A`

rather than a change in the original research question.

## Correction
1. Restore AI/sociotechnical operational identity as the primary validation domain for SFI-A.
2. Reclassify all CTC/HeLa tracking work as `A-TRANSFER-BIO`, an external adversarial transfer/falsification domain.
3. Preserve all existing commits, permission requests, runner code, protocols, and results. Nothing is deleted or rewritten retrospectively.
4. Any statement that depended on biology being the primary domain is marked superseded by this ADR.

## Primary object after correction
The primary object is not a cell, model, agent identifier, or software version. It is the measurement relation:

`H_id(A,B | Omega)`

constructed from declared evidence families including relational continuity, boundary continuity, functional-response continuity, lineage/provenance continuity, trajectory memory, scale, characteristic time, and authority/capability configuration.

## Primary AI question
Can the operational continuity of an AI system be measured longitudinally without collapsing model, agent, artifact, evidence, memory, tools, permissions, governance, and environment into a single identifier?

## Falsifiable alternatives
- CH-A1: conventional identifier/version continuity is sufficient for operationally relevant identity decisions.
- CH-A2: model continuity explains essentially all useful operational continuity; other evidence families add negligible information.
- CH-A3: no transferable individuation relation exists; identity is irreducibly purpose/domain-specific.

## Biological transfer role
A-TRANSFER-BIO asks a different question: if an operational individuation framework is genuinely more general than software semantics, do any of its declared continuity variables retain explanatory/reconstructive value in an external biological lineage domain?

A failure in A-TRANSFER-BIO does not automatically falsify the AI-domain measurement framework, but it constrains claims of cross-domain transfer. A success does not validate SFT.

## Governance consequence
This correction must appear in future state reports as a recorded methodological divergence and recovery. No repository cleanup may erase the intermediate biological-first interpretation.
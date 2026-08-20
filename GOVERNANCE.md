# Research Governance

## Epistemic states

Every claim, result, and artifact must be assigned one of these states:

- `proposed`: conceptual statement not yet operationalized.
- `registered`: operational definition and falsifier fixed before the relevant observation.
- `observed`: direct record or measurement exists.
- `derived`: produced by a declared transformation of observed data.
- `inferred`: interpretation supported by observed/derived objects.
- `contested`: material counterevidence exists.
- `refuted`: preregistered falsifier satisfied.
- `withheld`: retained but not yet released publicly.

## Non-circularity rule

SFI-A and SFI-B must remain publishable even if System Friction Theory is false. Their methods and results may support, weaken, or refute SFI-C0. They must not be defined so that SFT is true by construction.

## Evidence lineage

Every empirical claim should be reconstructable through:

`claim -> hypothesis_id -> protocol -> source/data -> transformation/notebook -> result -> figure/table -> manuscript location -> commit -> release -> DOI (if any)`

## Prospective vs post-hoc

Changes made after relevant results are known must be logged as post-hoc. A revised hypothesis receives a new identifier or version; the original is never silently overwritten.

## Public repository rule

Public Git history is a living record, not a publication claim. A GitHub Release freezes a software/research state. A DOI deposit freezes a citable research object. These states are deliberately distinct.

## CHI anonymity

The canonical public research history and any anonymous review package are separate surfaces. The anonymous package must remove author names, institution names, ORCID, identifying URLs, repository owner metadata, acknowledgements, and other direct or indirect identity cues required by the venue's current policy.

## Data policy

Do not commit secrets, credentials, personal data, confidential institutional data, restricted third-party material, or raw data whose public disclosure is not authorized. When raw data cannot be public, commit a data dictionary, provenance record, access constraints, synthetic/example data where appropriate, and reproducible transformations that can be shared.

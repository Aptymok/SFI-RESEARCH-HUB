# Releases and Zenodo Policy

## Core distinction

`commit != GitHub Release != DOI deposit`

Commits record living work. Releases freeze selected repository states. DOI deposits create citable research objects.

## Default policy

Do not automatically archive every GitHub Release to Zenodo. Prefer deliberate research-object deposits whose contents, metadata, authorship, license, and version have been reviewed.

## Recommended publication objects

- `SFI-A-INDIVIDUATION-v1.x` — manuscript + protocol + instrument + reproducible evidence package.
- `SFI-B-AI-OBSERVABILITY-v1.x` — manuscript + trace protocol + reproducible evidence package.
- `SFI-SFT-SPEC-v0.x` — only when a deliberate public preregistration/specification release is desired.
- datasets/instruments may receive independent deposits when reuse or citation warrants separation.

## What should not receive a DOI by default

- routine commits;
- incomplete notebooks;
- anonymous review packages;
- transient CHI submission builds;
- raw confidential/restricted data;
- exploratory analyses that have not been designated as research objects.

## Versioning

Use semantic-style research versions where practical:

- patch: non-substantive corrections that do not change scientific claims;
- minor: new analyses/materials without replacing the primary claim set;
- major: materially revised research object or post-review version.

A frozen prospective specification that changes its substantive hypotheses must receive a new version; do not overwrite the old scientific state.

## Citation lineage

Each DOI deposit should record, where available: Git commit SHA, release tag, research object ID, hypothesis IDs, data checksums, notebook/script versions, manuscript version, license, and relation to previous/next versions.

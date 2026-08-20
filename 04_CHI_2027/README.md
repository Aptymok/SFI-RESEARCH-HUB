# CHI 2027 — Review Surface

This directory is a venue-specific derivative, not an independent theory program.

## Canonical contribution decision

**CHI object = METHOD + EMPIRICAL EVIDENCE.**

The paper must contribute an HCI-relevant method for reconstructing human-AI state transitions and evaluate it empirically. It must remain meaningful if System Friction Theory is false.

Primary falsifiable claim:

`Structured event lineage improves reconstruction of human-AI state transitions relative to matched governance-only and unstructured-information baselines.`

Strong counter-hypotheses:
1. governance artifacts alone are equivalent within preregistered bounds;
2. any gain comes from information volume rather than lineage structure;
3. apparent state transitions are task-learning effects rather than human-AI interaction dynamics.

## Rule
The canonical public research record and the anonymous review package are separate surfaces.

Suggested layout:
- `canonical/` — internal mapping to SFI-A/SFI-B research objects;
- `submission/` — venue-format manuscript source;
- `anonymous_export/` — reviewer-facing files stripped of direct/indirect identity cues;
- `supplement/` — protocols, code/data package and README prepared under the venue's current policy.

## What CHI is NOT
- not a generic SFT manifesto;
- not evidence that SFT is true;
- not a venue for collapsing A, B and C into one unfalsifiable framework;
- not a reason to expose identifying metadata in anonymous review.

## Anonymization checklist
Before submission, remove or neutralize author names, institutional names, acknowledgements, ORCID identifiers, identifiable repository-owner URLs, personal domains/emails, metadata in generated PDFs/ZIPs, code comments that identify authors, dataset fields that identify participants/operators, and links that resolve to identity-revealing pages.

Revalidate the official CHI policy immediately before packaging/submission.

## Publication relation
A public preprint and a CHI submission are not automatically equivalent publication objects. Do not create a DOI/release from this directory merely because a submission snapshot exists. Any public deposit decision must be checked against the venue policy current at that time.
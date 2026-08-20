# SFI Research Hub

Canonical research infrastructure for the System Friction Institute research program.

## Purpose

This repository separates four layers that must not be collapsed:

1. **Living research history** — commits and working branches.
2. **Registered scientific states** — frozen hypotheses, protocols, and declared falsifiers.
3. **Publication artifacts** — manuscripts, supplements, and venue-specific review packages.
4. **Citable immutable objects** — deliberate releases and DOI deposits.

A commit is not a release. A release is not automatically a DOI. A DOI is not evidence that a claim is true.

## Current program

| ID | Research object | Role | Current state |
|---|---|---|---|
| SFI-A | *Individuation as a Measurement Problem* | construct definition / measurement | drafting |
| SFI-B | *From AI Governance to AI Observability* | external execution / observability | drafting |
| SFI-C0 | *System Friction Theory — Initial Falsifiable Specification* | prospective prediction layer | frozen candidate |
| SFI-C1 | *System Friction Theory: Persistent Constraints, Multiscale Reorganization, and Pre-Emergent Information in Dynamical Systems* | theoretical synthesis | withheld |
| SFI-CHI27 | CHI 2027 submission derivative | HCI venue-specific surface | candidate |

## Scientific sequence

The intended publication sequence is not the same as the research-registration sequence.

```text
SFI-C0 frozen specification
        ↓
SFI-A measurement work
        ↓
SFI-B external execution / CHI derivative
        ↓
prospective + adversarial evidence
        ↓
SFI-C1 theoretical synthesis
```

SFI-C0 exists to preserve prospective claims. It is **not** presented as validated theory.

## Repository map

```text
00_REGISTRY/                  research objects + hypothesis ledger
01_INDIVIDUATION/             SFI-A
02_AI_OBSERVABILITY/          SFI-B
03_SYSTEM_FRICTION_THEORY/    SFI-C0 / later SFI-C1
04_CHI_2027/                  anonymous review surface
SHARED/                       schemas/templates shared across objects
GOVERNANCE.md                 epistemic/evidence rules
RELEASES_AND_ZENODO.md        release + DOI policy
```

## Evidence principle

Every empirical claim should be reconstructable through:

```text
claim
 → hypothesis_id
 → protocol
 → source/data
 → transformation/notebook
 → result
 → figure/table
 → manuscript location
 → commit
 → release
 → DOI (if any)
```

Negative results, failed reconstructions, and counterevidence are first-class research objects.

## Non-circularity rule

SFI-A and SFI-B must remain meaningful and publishable if System Friction Theory is false. They may support, weaken, or refute SFI-C0. They must not encode SFT as an assumption required for their own validity.

## Public-data boundary

Do not commit secrets, credentials, confidential institutional material, unauthorized personal data, or restricted third-party content. When raw data cannot be public, publish the strongest permissible provenance, schema, synthetic/example data, and reproducible transformation layer.

## CHI review boundary

The public canonical history and an anonymous review package are distinct surfaces. Reviewer-facing exports must be regenerated and checked against the venue's current anonymization policy before submission.

## Status

Foundation architecture established 2026-08-19. Manuscripts, protocols, instruments, notebooks, and evidence are versioned per research object rather than treated as interchangeable repository files.

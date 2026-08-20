# Release Candidate v0.1.0

Proposed archival title:

**SFI Research Hub: Prospective Hypothesis and Falsification Registry v0.1.0**

## Purpose

Freeze a public, timestamped record of what was proposed, how it could fail, and which protocols were specified before eligible empirical evaluation.

## This release is intended to contain

- `00_REGISTRY/research_registry.yaml`
- `00_REGISTRY/HYPOTHESIS_LEDGER.csv`
- `GOVERNANCE.md`
- `01_INDIVIDUATION/protocols/PROTOCOL-A-001.md`
- `02_AI_OBSERVABILITY/protocols/PROTOCOL-B-001.md`
- `03_SYSTEM_FRICTION_THEORY/SFT-0.1-FROZEN/SPECIFICATION.md`
- `03_SYSTEM_FRICTION_THEORY/protocols/PROTOCOL-C0-001.md`
- `START_HERE.md`
- `STATUS.md`
- `REPRODUCE.md`
- synthetic benchmark generators/analysis companions as implementation checks
- bilingual working manuscripts as contextual, non-final artifacts

## This release does NOT claim

- empirical validation of System Friction Theory;
- empirical validation of SFI-A or SFI-B;
- acceptance by CHI or another venue;
- that synthetic benchmark outputs are external evidence.

## Release gate

Create the GitHub Release only after:

1. all files above are merged to `main`;
2. SFT-0.1 wording has been reviewed as genuinely falsifiable;
3. author metadata is correct;
4. ORCID values, if available, have been added and verified rather than guessed;
5. repository URLs and Zenodo metadata resolve to the canonical repository name;
6. no confidential or restricted data are present.

## Proposed tag

`v0.1.0-prospective-registry`

Once this tag is released while Zenodo integration is enabled, Zenodo should ingest the release automatically. Do not create the release merely to obtain a DOI; create it only when this prospective state is ready to become immutable archival evidence.

# A-TRANSFER-BIO Runner — Cell lineage transfer benchmark

Status: retained / reclassified by ADR-004.

This runner was initially built while SFI-A was temporarily narrowed toward biological cell tracking. That narrowing has been corrected. The runner is preserved as an external transfer/falsification domain, not as the primary empirical object of SFI-A.

## Scientific role
The runner asks whether continuity variables used by the SFI-A operational individuation framework retain reconstructive value in a biological lineage domain with independent reference annotations.

It does **not** define the canonical SFI-A problem, and success here does not validate a universal individuation metric or System Friction Theory.

## Human gate
The required pre-execution human action is obtaining/recording the lawful permission basis for public non-CTC scientific use of Fluo-N2DL-HeLa. The raw dataset and permission receipt remain local and are ignored by Git.

## Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r RUNNERS/A/requirements.txt
```

Place the real permission record locally at:
`local_permissions/CTC_PERMISSION_GRANTED.txt`

## Execute
```bash
python RUNNERS/A/run.py
```

The runner:
1. verifies the permission gate;
2. downloads the official CTC training archive if absent;
3. computes SHA-256 and provenance metadata;
4. discovers image and imperfect-segmentation sequences;
5. predicts links using instantaneous and history/persistence variants;
6. loads gold tracking masks only in evaluation;
7. evaluates development and held-out sequences;
8. writes local results;
9. returns a domain-bounded support state.

## Interpretation boundary
A positive result means only that the tested continuity variables survived this external biological transfer domain under the declared implementation. A negative result constrains transfer claims. Neither result validates or falsifies SFT by itself.

See `00_REGISTRY/ADR-004_RESTORE_SFI_A_SCOPE.md`.
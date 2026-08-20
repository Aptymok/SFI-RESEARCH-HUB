# A-EMP-001 Autonomous Runner

Purpose: execute the first empirical falsification test for SFI-A without manual result steering.

## Human gate
The only required pre-execution human action is obtaining/recording the lawful permission basis for public non-CTC scientific use of Fluo-N2DL-HeLa. The raw dataset and permission receipt remain local and are ignored by Git.

## Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r RUNNERS/A/requirements.txt
```

Place the real permission record locally at:
`local_permissions/CTC_PERMISSION_GRANTED.txt`

The record should contain date, granting party/contact, permitted scope, and a reference to the original authorization (do not commit confidential correspondence).

## Execute
```bash
python RUNNERS/A/run.py
```

The runner then:
1. verifies the permission gate;
2. downloads the official CTC training archive if absent;
3. computes SHA-256 and provenance metadata;
4. discovers image and imperfect-segmentation sequences;
5. predicts links using an instantaneous baseline and a history/persistence model;
6. loads gold tracking masks only in the evaluation stage;
7. evaluates sequence 01 as development and sequence 02 as held-out;
8. writes local results to `local_results/A-EMP-001/`;
9. returns one of: `H01_SURVIVED_DOMAIN`, `H01_NOT_SUPPORTED_DOMAIN`, `INCONCLUSIVE`.

## Scientific boundary
A positive held-out result means only that SFI-A-H01 survived this domain under this implementation. A null/negative result must remain visible. Neither result validates or falsifies SFT by itself.

## Next hardening before confirmatory publication
- lock exact archive hash after acquisition;
- review the split against CTC sequence characteristics;
- add division-event-aware metrics;
- run time-permutation and matched-complexity controls;
- bootstrap confidence intervals;
- independently review feature/metric definitions;
- preserve the pre-analysis commit before final held-out execution.

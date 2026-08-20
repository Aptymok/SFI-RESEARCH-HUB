# Reproduce

This guide separates engineering reproducibility from empirical validation.

## Requirements

Python 3.10+ is sufficient for the current synthetic benchmarks. The scripts intentionally use the Python standard library only.

## SFI-A synthetic engineering check

Run:

```bash
python 01_INDIVIDUATION/data/synthetic/generate_A_SYN_001.py
python 01_INDIVIDUATION/notebooks/A_SYN_001_analysis.py
```

Expected artifacts:

- `01_INDIVIDUATION/data/synthetic/A_SYN_001.csv`
- `01_INDIVIDUATION/results/A_SYN_001_RESULT.md`

Interpretation boundary: this verifies that the analysis can recover structure intentionally embedded in a deterministic synthetic benchmark. It is not empirical support for SFI-A-H01.

## SFI-B synthetic engineering check

Run:

```bash
python 02_AI_OBSERVABILITY/data/synthetic/generate_B_SYN_001.py
python 02_AI_OBSERVABILITY/notebooks/B_SYN_001_analysis.py
```

Expected artifacts:

- `02_AI_OBSERVABILITY/data/synthetic/B_SYN_001.csv`
- `02_AI_OBSERVABILITY/results/B_SYN_001_RESULT.md`

Interpretation boundary: this verifies that the scoring pipeline distinguishes deliberately constructed governance/observability conditions. It is not evidence that real human-AI systems behave that way.

## Empirical reproduction

Empirical reproduction is intentionally gated. Before an empirical notebook can be called confirmatory, its directory must include:

1. source/provenance manifest;
2. license or permission record;
3. frozen inclusion/exclusion rules;
4. frozen primary metric and baselines;
5. analysis commit SHA recorded before final evaluation;
6. raw-data access instructions or a lawful de-identified derivative;
7. executed outputs and null/negative results.

## Data boundary

Do not commit credentials, personal data, confidential institutional material, restricted prompts, proprietary source records, or source datasets whose license forbids redistribution. Reference external sources by persistent identifier, checksum, and acquisition instructions where lawful.

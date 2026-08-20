# Dynamic Contribution and Authorship Weighting

Status: active governance model

This model is used to estimate contribution shares during research execution. It is not a substitute for final authorship judgment, journal policy, or CRediT statements.

## Dimensions and default weights

Each contributor is scored 0-1 on:
- Conceptualization / construct ownership: 0.25
- Methodology / falsification design: 0.20
- Empirical execution / investigation: 0.20
- Formal analysis / software / data work: 0.15
- Writing / synthesis / revision: 0.10
- Validation / adversarial review / reproducibility: 0.10

Weighted contribution score:

`W_i = 0.25C + 0.20M + 0.20E + 0.15A + 0.10W + 0.10V`

Normalized authorship contribution estimate:

`P_i = W_i / sum(W_j)`

## Rules

1. Percentages are provisional and versioned.
2. A contribution must have a trace: commit, protocol decision, analysis artifact, written section, validation record, dataset work, or signed decision note.
3. Identity, seniority, friendship, institutional title, or mere presence do not add weight.
4. A contributor may become first author on a derivative line if their normalized contribution becomes dominant.
5. Corresponding author is a continuity/contact role, not an automatic claim of largest contribution.
6. Final manuscripts should map actual work to CRediT roles.
7. AI systems do not receive authorship; their use is logged as tooling/provenance where venue policy requires it.

## Initial provisional state

These are working estimates with low-to-moderate confidence and MUST be updated from logged contributions:

| Object | Juan | Edwing | Confidence | Rationale |
|---|---:|---:|---|---|
| SFI-A Individuation | 70% | 30% | low | Juan currently drives conceptual framing, research orchestration and manuscript direction; Edwing retains expected co-development/validation capacity not yet fully exercised in the Hub. |
| SFI-B AI Observability | 65% | 35% | low | Juan currently drives protocol/governance architecture; Edwing has a larger plausible future role in execution, instrumentation, external critique and HCI-oriented development. |
| SFI-C0 SFT specification | 70% | 30% | low | Current construct orchestration is primarily Juan-led; Edwing's weight should increase only through traceable theoretical, methodological or adversarial contribution. |
| CHI-2027 derivative | 60% | 40% | very low | This object is not yet executed; weighting is intentionally near-balanced because future empirical/system contribution can materially alter authorship order. |

## Recalculation trigger

Recalculate after any of:
- protocol freeze;
- empirical dataset acquisition;
- completed notebook/analysis;
- major theoretical revision;
- manuscript section completion;
- external reviewer response;
- new research branch created from a finding;
- venue submission freeze.

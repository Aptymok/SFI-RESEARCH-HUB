# DISCRIMINANT_TEST_A_AI

Status: designed; not confirmatory until adjudication set and thresholds are frozen.

## Objective
Test whether SFI-A contributes operational individuation information beyond existing single-axis identity/continuity approaches.

## Transformation families
Each base AI configuration is perturbed along one or more axes:
- model/substrate;
- memory/history;
- tools;
- authority/permissions;
- policy/governance;
- retrieval/data boundary;
- runtime/deployment;
- technical identifier/provenance;
- role/business function;
- environment.

## Purpose-conditioned labels
Independent adjudicators assign SAME / DISTINCT / UNRESOLVED separately for:
1. accountability continuity;
2. functional continuity;
3. authorization continuity;
4. memory/history continuity;
5. deployment/service continuity.

No universal label is assumed.

## Baselines
B0 technical identifier/provenance only.
B1 model identity only.
B2 memory continuity only.
B3 behavioral continuity only.
B4 authority continuity only.
B5 best single-axis oracle selected on development data only.

## Candidate SFI-A model
A composite measurement relation may use relational continuity, boundary continuity, response profile, lineage/provenance, authority, trajectory history, and declared purpose. Exact estimator/weights must be frozen before held-out evaluation.

## Primary falsifier
SFI-A lacks distinct measurement value if its held-out performance is statistically indistinguishable from or inferior to B5 after matched-complexity control, or if gains vanish when calibrated UNRESOLVED predictions are required.

## Secondary falsifier
If cross-purpose or cross-transformation generalization collapses, the claim must be restricted. If every effective rule is purpose-specific, the universal component of the framework is rejected.

## Anti-leakage
- no held-out adjudication labels in feature/weight design;
- transformation templates fixed before final adjudication;
- model/provider names may be blinded where possible;
- repeated variants must not leak canonical labels through filenames/IDs;
- all post-hoc changes generate a new protocol version.

## Output
Report per-purpose confusion matrices, calibration/abstention rate, baseline deltas, uncertainty, failure taxonomy, and transformation-level sensitivity. No aggregate score may hide a failed purpose class.

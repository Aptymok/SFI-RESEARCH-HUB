# A-EMP-001 — Cell Tracking Challenge / Fluo-N2DL-HeLa

Status: **PRIMARY EMPIRICAL DOMAIN SELECTED — permission/download pending**
Research object: SFI-A
Decision date: 2026-08-20
Selection rationale: chosen for observability and independent reference annotations, not for expected agreement with SFI-A-H01.

## Why this domain
The Cell Tracking Challenge provides real time-lapse microscopy with reference tracking annotations that link cell instances across frames into lineage trees. The domain therefore contains externally defined continuity, disappearance, mitotic division, and lineage events against which an operational individuation method can fail or succeed.

Primary dataset: Fluo-N2DL-HeLa (real HeLa cells expressing H2b-GFP; 2D+time).

## Primary hypothesis
Persistence-aware operational individuation adds held-out information for reconstructing entity continuity and lineage beyond matched instantaneous/state-only baselines.

## Counter-hypothesis
Instantaneous similarity, tracking heuristics, or conventional baselines are sufficient; persistence/history adds no reproducible out-of-sample value.

## Independence safeguard
Reference tracking annotations must be withheld from feature construction and used only for evaluation after the operational method is fixed on training/development partitions.

## Legal/use boundary
Do NOT copy or mirror Cell Tracking Challenge images or annotations into this repository. Public research use must comply with source permissions and licensing. The Hub should retain only source metadata, permission record, checksums of locally obtained files where permitted, code, and lawful derived numerical outputs.

## Required before execution
1. request/obtain permission for the intended scientific use if required by the source terms;
2. record source citation and dataset version/date;
3. download locally from the official source;
4. freeze train/development/held-out partitioning and metrics before inspecting held-out annotations;
5. log all departures from PROTOCOL-A-001.

## Generalization rule
A positive result in HeLa is domain-bounded. A second structurally different domain must be used before any cross-domain individuation claim.

## Expected scientific outcome
Unknown. A positive, null, unstable, or domain-restricted result is admissible.
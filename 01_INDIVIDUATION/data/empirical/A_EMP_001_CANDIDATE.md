# A-EMP-001 Candidate — Cell Tracking Challenge / Fluo-N2DL-HeLa

Status: candidate selected; permission/download pending
Research object: SFI-A
Selection rationale: chosen for observability and independent reference annotations, not for expected agreement with SFI-A-H01.

## Why this domain
The Cell Tracking Challenge provides real time-lapse microscopy with reference tracking annotations that link cell instances across frames into lineage trees. The domain therefore contains externally defined continuity, disappearance, mitotic division, and lineage events against which an operational individuation method can fail or succeed.

Primary candidate: Fluo-N2DL-HeLa (real HeLa cells expressing H2b-GFP; 2D+time).

## Independence safeguard
Reference tracking annotations must be withheld from feature construction and used only for evaluation after the operational method is fixed on training/development partitions.

## Legal/use boundary
Do NOT copy or mirror Cell Tracking Challenge images or annotations into this repository. The CTC states that public non-CTC scientific use requires explicit permission from challenge organizers, and cloning the datasets or annotations is forbidden. The Hub should retain only source metadata, permission record, checksums of locally obtained files where permitted, code, and derived numerical outputs that are lawful to release.

## Required before execution
1. request/obtain permission for non-CTC scientific use;
2. record source citation and dataset version/date;
3. download locally from the official CTC source;
4. freeze train/development/held-out partitioning and metrics before inspecting held-out annotations;
5. log all departures from PROTOCOL-A-001.

## Expected scientific outcome
Unknown. A positive, null, unstable, or domain-restricted result is admissible.
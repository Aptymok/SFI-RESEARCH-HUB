# PROTOCOL-A-001 — Operational Individuation Validation

Status: designed / not executed
Protocol version: 0.1
Primary hypothesis: SFI-A-H01

## Question
Can an entity boundary be reconstructed from persistence and state-transition relations without presupposing a metaphysical identity label?

## Unit of analysis
A time-indexed candidate entity represented by observations x(t), candidate boundary B(t), environmental observations E(t), and interventions/events when available.

## Primary operational quantities
- boundary stability BS: agreement of inferred boundary membership across adjacent windows;
- internal persistence IP: temporal dependence of internal state after conditioning on environment;
- external separability ES: discrimination between internal and external trajectories;
- reconstruction accuracy RA: agreement between inferred entity continuity and held-out reference labels/events.

No single quantity is sufficient for individuation.

## Datasets
### A-SYN-001 — synthetic benchmark
Generate deterministic families of coupled dynamical systems with known boundaries, boundary drift, merge/split events, and matched null systems. This dataset tests implementation and identifiability only; it cannot establish external validity.

### A-EMP-001 — empirical benchmark
Required from an external or independently generated longitudinal system with timestamps and enough variables to distinguish internal state from environment. Selection criteria must be recorded before analysis.

## Baselines
1. random boundary with matched cardinality;
2. static boundary baseline;
3. instantaneous-similarity clustering without persistence;
4. oracle/reference boundary where synthetic ground truth exists.

## Primary test
Fit the operational reconstruction on training windows and evaluate held-out windows. Compare RA and boundary-event detection against baselines. Report uncertainty and failure cases.

## Falsification rule
SFI-A-H01 is contradicted in the tested domain if the persistence/boundary formulation fails to exceed the preregistered non-persistence baselines on held-out reconstruction, or if performance collapses under modest perturbations that preserve the reference entity.

## Counter-hypothesis
A-CH01: apparent individuation is fully explained by instantaneous similarity; persistence/history adds no out-of-sample value.

## Negative evidence
Null results, unstable boundaries, sensitivity to arbitrary thresholds, and domains where the method cannot identify an entity are retained and reported.

## Leakage controls
Reference labels used for evaluation may not be used to construct features. Thresholds must be selected using training data only.

## Execution gate
Before A-EMP-001 is run, record dataset identity, inclusion/exclusion rules, target variables, primary metric, threshold-selection rule, and analysis commit SHA.
# SFT-0.1 — Initial Falsifiable Specification

Status: **FROZEN PROSPECTIVE SPECIFICATION — not validated theory**  
Registered: 2026-08-19  
Frozen by investigator decision: 2026-08-20  
Purpose: preserve prospective claims before eligible empirical evidence is examined.

## Scope

System Friction Theory (SFT) is provisionally defined as a theory candidate about the resource cost and constraint structure associated with maintaining or changing dynamical regimes.

This document is not evidence that SFT is true. Its function is to state what must be tested and what would count against the theory.

## Candidate constructs

Let a system be represented over time by state \(X_t\), a set of constraints \(K_t\), interventions \(U_t\), and an observed or derived regime label \(R_t\).

A transition occurs when a declared regime criterion maps \(R_t \to R_{t+\Delta}\).

A provisional friction quantity \(F_S\) refers to the additional resource cost associated with maintaining or changing a regime under persistent constraints, beyond what is explained by instantaneous state displacement alone.

This definition intentionally does **not** fix a final estimator. Competing estimators must be evaluated rather than selected post hoc for fit.

## H1 — Persistence contribution

After controlling for an explicitly defined instantaneous state difference \(D(X_t,X_{t+\Delta})\), measures of constraint persistence/history improve out-of-sample prediction or explanation of transition cost.

### Falsifier
Across preregistered domains and models, persistence/history terms provide no reproducible incremental value over matched baselines once instantaneous state difference and declared confounds are controlled.

## H2 — Pre-emergent structure

Before some regime transitions, structured persistence in constraints contains reproducible information about the future transition relative to matched null/baseline processes.

### Falsifier
No preregistered pre-transition statistic discriminates future transition windows from matched non-transition/null windows out of sample beyond declared uncertainty thresholds.

## H3 — Multiscale non-equivalence

System friction is not generally invariant under arbitrary aggregation. At least some transitions exhibit materially different constraint/cost structure when measured at different declared scales.

### Falsifier
Across preregistered tests, scale changes do not alter predictive/explanatory structure beyond sampling or measurement error, or all apparent scale effects are attributable to known aggregation artifacts.

## Counter-hypotheses to test
- **CH1 — State-distance sufficiency:** transition cost is fully explained by instantaneous state displacement plus ordinary noise/confounds; persistence contributes nothing.
- **CH2 — Retrospective patterning:** apparent pre-emergent information is a look-ahead, selection, segmentation, or multiple-testing artifact.
- **CH3 — Generic complexity relabeling:** SFT adds no distinct explanatory or predictive content beyond established constructs such as hysteresis, switching costs, energy barriers, path dependence, resilience, or control effort.
- **CH4 — Instrument artifact:** measured friction is primarily induced by the chosen instrumentation, boundary rule, or temporal resolution.

## Evidence that does not by itself support SFT
The following are insufficient alone:
- a visually compelling transition;
- a post-hoc fit to one case;
- high correlation without prospective prediction or discriminant comparison;
- re-description of known hysteresis/path dependence under new terminology;
- success of an SFI-built system when the metric is embedded in the system's own objective function;
- anecdotal human interpretation;
- institutional adoption or citation count.

## Minimum survival criteria for SFT-1
Before promotion to a consolidated theoretical manuscript, the program should demonstrate:
1. operationally independent constructs;
2. at least one prospective or preregistered prediction;
3. explicit comparison with strong counter-hypotheses and adjacent established theories;
4. out-of-sample or held-out evaluation where applicable;
5. negative/failed cases retained in the evidence record;
6. sensitivity to boundary, scale, and temporal-resolution choices;
7. a statement of domains where SFT is not expected to apply;
8. reproducible lineage from data to claims.

## Freeze rule
Substantive changes to H1–H3 or their falsifiers after relevant evidence is known must create a new specification version. This file must not be silently rewritten to accommodate results.

Any proposed modification now follows:
`SFT-0.1 FROZEN -> CHALLENGED -> SFT-0.2 candidate`, preserving SFT-0.1 unchanged in the archival record.
# SFI-A AI Identity — Sample Size and Power Plan v0.1

Status: designed / pre-confirmatory
Date: 2026-08-20

## Objective
Determine whether the SFI-A operational-individuation model adds discriminative value beyond the strongest preregistered ensemble of existing continuity proxies while preserving genuine ambiguity as UNRESOLVED.

## Unit of judgment
A pair of AI-system states under one declared purpose of identity.

Purposes:
1. accountability continuity;
2. functional continuity;
3. authorization continuity;
4. memory/history continuity;
5. deployment/service continuity.

## Primary confirmatory panel
The benchmark contains 20 perturbation families. Each family is adjudicated under all 5 purposes.

20 scenario families × 5 purposes = 100 pair-purpose cells.

Five independent adjudicators label every confirmatory cell:

100 cells × 5 adjudicators = 500 primary judgments.

This is the preferred confirmatory design. Three adjudicators is the minimum acceptable fallback; if only three are available, the study must be reported as lower-confidence and no strong universality claim is permitted.

## Why five
Five judges permit:
- majority classification without reducing 2-vs-1 disagreements to certainty;
- direct estimation of inter-rater agreement;
- preservation of ambiguity;
- sensitivity analysis under leave-one-rater-out removal;
- detection of purpose-dependent identity rather than forced universal labels.

## Gold construction
The gold label is not a simple majority vote.

For each cell:
- SAME: at least 4/5 SAME and no material evidence-integrity objection;
- DISTINCT: at least 4/5 DISTINCT and no material evidence-integrity objection;
- UNRESOLVED: all other patterns, including purpose ambiguity or insufficient evidence.

A 3-judge fallback requires unanimity for SAME/DISTINCT; all 2-vs-1 outcomes become UNRESOLVED.

## Agreement metrics
Report raw agreement and Krippendorff alpha for nominal labels. Also report per-purpose agreement and the complete confusion structure. Agreement is evidence about measurability, not a nuisance to hide.

## Primary model comparison
Compare:
- B0: identifier continuity;
- B1: model/substrate continuity;
- B2: memory/history continuity;
- B3: behavioral continuity;
- B4: authority continuity;
- B5: provenance/lineage continuity;
- B*: preregistered strongest ensemble of B0-B5;
- SFI-A: boundary-explicit operational individuation model.

Primary outcome: macro-F1 across SAME/DISTINCT/UNRESOLVED on held-out cells, with secondary balanced accuracy on resolvable SAME/DISTINCT cells.

## Paired inference
Because every method scores the same cells, use paired bootstrap confidence intervals over pair-purpose cells and a paired permutation/randomization test for the difference SFI-A - B*. Do not treat the five human ratings as five independent benchmark items.

## Minimum survival criterion
SFI-A does not earn a novelty claim if its held-out performance is statistically and practically indistinguishable from B*.

A candidate survival threshold for confirmatory freeze is:
- positive held-out delta versus B*;
- 95% paired bootstrap interval excluding zero for the primary comparison;
- no collapse under leave-one-purpose-out analysis;
- no result driven solely by identifier rotation or one trivial perturbation family.

The exact practical-effect threshold must be frozen after pilot calibration but before confirmatory labels are opened.

## Time hypothesis
Evaluate a history ablation:
SFI-A(full) versus SFI-A(no-history).

If history removal produces no reproducible degradation on held-out cells, trajectory memory is not necessary in this benchmark regime.

## Anti-overfitting split
The 20 perturbation families are divided by family, never by individual duplicated cell.
- development/calibration: 8 families = 40 purpose-cells;
- confirmatory held-out: 12 families = 60 purpose-cells.

Human adjudication may be collected for all 100 cells in one blinded session, but confirmatory labels for held-out families must remain inaccessible to model/threshold tuning until freeze.

## Escalation rule
If more than 35% of held-out cells are UNRESOLVED, do not interpret this as model failure alone. Open an identifiability analysis: the operational identity question may be underdetermined at the supplied observation boundary.

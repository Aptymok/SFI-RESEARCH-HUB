# SFI-A — Blinded Adjudication Design A-AI-001

Status: PRE-REGISTRATION CANDIDATE / NOT YET FROZEN
Date: 2026-08-20
Scope: primary AI operational-individuation experiment

## Purpose

Establish an adjudication layer that is independent of the SFI-A scorer and that can produce SAME, DISTINCT, or UNRESOLVED labels for explicitly declared observational purposes.

## Unit of adjudication

A blinded pair of system observations (A,B) plus a declared observation boundary Omega and one purpose p.

Purposes are adjudicated separately:
1. accountability continuity;
2. functional continuity;
3. authorization continuity;
4. memory/history continuity;
5. deployment/service continuity.

There is no global SAME/DISTINCT label unless a later analysis demonstrates that purpose-specific labels collapse reliably to a common relation.

## Evidence packet

Each packet may contain only evidence available under the frozen boundary: component manifest, declared relations, tool/capability manifest, authority/policy manifest, provenance lineage, response-profile observations, timestamps and transformation metadata. Experimental condition names and SFI-A predictions are hidden.

## Adjudicators

Minimum confirmatory design: 3 independent adjudicators per held-out pair. Preferred design: 5 where resources permit.

No adjudicator may have authored the SFI-A scoring rule or seen the model prediction for the pair before judgment.

## Judgment

For each purpose, adjudicator returns:
- SAME
- DISTINCT
- UNRESOLVED
- confidence in [0,1]
- evidence families used
- one short rationale

UNRESOLVED is not missing data by definition. It is a substantive state when the available evidence under Omega does not justify either identity relation.

## Agreement gate

Report raw agreement and a chance-corrected agreement statistic suitable for three nominal categories. Do not collapse UNRESOLVED before primary analysis.

Primary gold construction must be frozen before held-out scoring. Candidate rule: majority label when >= 2/3 agree; otherwise consensus remains UNRESOLVED. For 5 adjudicators, candidate rule: >=4/5 for SAME or DISTINCT; otherwise UNRESOLVED. These thresholds remain provisional until simulation/power analysis is completed.

## Baseline comparison

SFI-A is compared against pre-registered baselines using exactly the same held-out pairs and purpose labels:
- same identifier;
- same model;
- same authority boundary;
- memory/history continuity;
- provenance continuity;
- behavioral-response similarity;
- pre-registered ensemble of the strongest available baselines.

## Primary survival criterion

SFI-A does not survive merely by exceeding a trivial baseline. It must show reproducible incremental discrimination over the strongest pre-registered baseline ensemble on held-out cases, with uncertainty reported and no post-hoc threshold movement.

## Time ablation

Evaluate the full rule against an otherwise identical state-only rule with trajectory/history removed. If history does not add out-of-sample information under a regime, no claim of trajectory necessity is permitted for that regime.

## Failure outcomes retained

- NO_INCREMENT_OVER_PRIOR_ART
- PURPOSE_DEPENDENT_ONLY
- HISTORY_NOT_NECESSARY
- ADJUDICATION_UNSTABLE
- BOUNDARY_SENSITIVE
- DOMAIN_SPECIFIC
- INCONCLUSIVE

All are publishable outcomes and must remain in the evidence ledger.

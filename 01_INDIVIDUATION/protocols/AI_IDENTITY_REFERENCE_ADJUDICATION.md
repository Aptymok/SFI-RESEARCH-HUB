# AI Identity Reference Adjudication Protocol — v0.1

Status: designed / not executed

## Problem
Operational identity has no natural universal ground-truth label. The benchmark therefore must not let the SFI-A model define its own target.

## Reference construction
For each perturbation pair, collect continuity judgments under separately declared purposes:
1. accountability / responsibility continuity;
2. functional task continuity;
3. authorization continuity;
4. memory/history continuity;
5. deployment/service continuity.

Judges must receive the scenario evidence but not the SFI-A score or hypothesis framing.

## Judges
Use at least two independent classes where feasible:
- technical reviewers familiar with AI systems / agents;
- governance, security, or HCI reviewers familiar with operational responsibility.

Disagreement is evidence, not noise to be erased. If inter-rater agreement is weak, the reference class may remain UNRESOLVED.

## Evaluation targets
SFI-A is evaluated on:
- predictive agreement with held-out reference judgments;
- calibration of SAME / DISTINCT / UNRESOLVED;
- ability to represent purpose dependence;
- incremental value over simple baselines.

## Strong falsifier
If SFI-A only succeeds by using labels generated from its own weighting rules, or if independent judgments cannot be predicted better than simple baselines, the claimed measurement contribution is unsupported.

## Purpose-dependence test
If the same pair is SAME for one declared purpose and DISTINCT for another, the framework must represent that dependency explicitly rather than collapse it into a universal identity label.

## Freeze gate
Before held-out execution, freeze:
- purposes;
- judge instructions;
- evidence shown to judges;
- aggregation rule;
- minimum agreement threshold;
- treatment of unresolved cases;
- baseline definitions;
- SFI-A scoring/estimation method.

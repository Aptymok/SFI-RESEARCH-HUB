# PROTOCOL-C0-001 — Prospective SFT Falsification

Status: prospective / do not execute until SFT-0.1 is frozen by release or immutable timestamp
Version: 0.1
Hypotheses: SFI-C0-H01, SFI-C0-H02

## Purpose
Test whether history/persistent constraints add explanatory or predictive information beyond instantaneous state difference, and whether preregistered pre-transition structure predicts regime transitions out of sample.

## Prohibition
Do not tune SFT quantities using the final evaluation domains and then count the same domains as confirmatory evidence.

## H01 design
Compare a state-only model M0 with a state+history/persistence model M1 on held-out transition-cost outcomes. Complexity penalties and evaluation metrics must be specified before seeing held-out results.

Falsifier: M1 adds no reproducible out-of-sample value over M0 across the preregistered domains, or gains disappear under matched complexity controls.

## H02 design
Define a pre-transition statistic P using training/development data only. Compare P against matched null, shuffled-time, and conventional early-warning baselines on held-out transition events.

Falsifier: P does not outperform preregistered baselines out of sample, or only works when transition times leak into feature construction.

## Required domains
At least two structurally different domains before any cross-domain theoretical claim. A single domain may only support a domain-bounded result.

## Adversarial analyses
- time permutation;
- matched-complexity null models;
- threshold sensitivity;
- ablation of persistence/history;
- negative-control outcomes;
- alternative transition definitions fixed before final evaluation.

## Interpretation
Passing this protocol does not prove SFT. It increases support for specified claims relative to stated alternatives. Failure must update or restrict SFT rather than being redescribed as hidden friction.
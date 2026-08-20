# B-EMP-001 — Trial-level AI-assisted chess decisions

Status: **PRIMARY EXTERNAL EMPIRICAL BENCHMARK SELECTED — acquisition pending**
Research object: SFI-B
Decision date: 2026-08-20
Selection rationale: chosen because the published dataset records pre-AI human decision, AI suggestion, feedback, confidence, self-confidence, and post-advice behavior across repeated trials. This creates an externally collected state -> intervention -> transition sequence rather than a dataset constructed to favor SFI-B-H01.

## Source
Chong et al., *Data on human decision, feedback, and confidence during an artificial intelligence-assisted decision-making task* (Data in Brief, 2023), associated Mendeley Data release.

## Structure
- 100 human participants;
- 30 experimental chess-puzzle trials plus practice trials;
- two conditions in which AI performance changes at trial 20 (high-to-low versus low-to-high);
- participant move before AI suggestion;
- AI suggestion and feedback;
- participant confidence in AI and self-confidence;
- trial-by-trial repeated interaction.

## Stage 1 — External state-reconstruction benchmark

Primary claim: structured event-level observation permits reproducible reconstruction of human-AI state transitions and adaptation around an exogenous change in AI reliability.

Counter-hypothesis: apparent transitions are fully explained by task performance, ordinary learning, or immediate recommendation dependence; the proposed observability representation adds no useful information.

This stage does NOT test the full governance-vs-observability thesis.

## Stage 2 — SFI controlled governance-vs-observability experiment

After Stage 1 instrument validation, execute PROTOCOL-B-001 comparing:
- G0 governance artifacts only;
- G1 governance + minimal event instrumentation;
- G2 governance + canonical structured lineage;
- information-volume-matched unstructured control.

Primary claim: governance completeness alone is not equivalent to transition observability.

Counter-hypotheses:
1. sufficiently mature governance artifacts already permit equivalent reconstruction;
2. any G2 gain is caused only by greater information volume, not structure/lineage.

## Expected scientific outcome
Unknown. Either stage may weaken, restrict, or refute the corresponding SFI-B claim.
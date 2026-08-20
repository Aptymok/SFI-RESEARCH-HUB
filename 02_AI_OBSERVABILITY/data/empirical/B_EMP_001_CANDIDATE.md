# B-EMP-001 Candidate — Trial-level AI-assisted chess decisions

Status: candidate selected; acquisition pending
Research object: SFI-B
Selection rationale: chosen because the published dataset records pre-AI human decision, AI suggestion, feedback, confidence, self-confidence, and post-advice behavior across repeated trials. This creates an externally collected state -> intervention -> transition sequence rather than a dataset constructed to favor SFI-B-H01.

## Source
Chong et al., Data on human decision, feedback, and confidence during an artificial intelligence-assisted decision-making task (Data in Brief, 2023), associated Mendeley Data release.

## Structure
- 100 human participants;
- 30 experimental chess-puzzle trials plus practice trials;
- two conditions in which AI performance changes at trial 20 (high-to-low versus low-to-high);
- participant move before AI suggestion;
- AI suggestion and feedback;
- participant confidence in AI and self-confidence;
- trial-by-trial repeated interaction.

## What it can test
This dataset can test the observational core of SFI-B: whether instrumented event-level records permit reconstruction of human-AI state transitions, adaptation, confidence trajectories, and response to an exogenous change in AI reliability.

## What it cannot test by itself
It does not directly compare mature governance artifacts against observability instrumentation. Therefore it must not be presented as confirming the full claim 'governance completeness does not imply observability.' It is an empirical observability benchmark and can support/refute narrower claims about state reconstruction.

## Follow-on confirmatory study
A separate controlled study under PROTOCOL-B-001 is required for the G0/G1/G2 governance-vs-observability contrast.

## Expected scientific outcome
Unknown. The dataset may show clean transitions, weak transitions, heterogeneous adaptation, or no reconstructible change.
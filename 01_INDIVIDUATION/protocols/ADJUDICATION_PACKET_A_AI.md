# A-AI Blind Adjudication Packet

Purpose: generate reference judgments independently of the SFI-A scorer.

## Adjudicator instruction
You will receive pairs of AI-system configurations A and B plus a declared purpose. Do not infer or use SFI terminology. Decide only whether available evidence justifies treating A and B as the same continuing operational system for that purpose.

Allowed labels:
- SAME
- DISTINCT
- UNRESOLVED

For each judgment record:
- label;
- confidence 0-100;
- decisive evidence dimensions;
- missing evidence that could change the judgment;
- one-sentence rationale.

## Purpose classes
P1 accountability: should actions/results remain attributable to the same accountable operational unit?
P2 function: does the system preserve the same operational function under equivalent task conditions?
P3 authorization: should permissions/authority be inherited as continuity of the same authorized unit?
P4 memory/history: does the later configuration inherit a sufficiently continuous trajectory/history?
P5 deployment/service: should monitoring, incidents, SLOs and longitudinal metrics aggregate the pair as one continuing service?

## Blindness rules
- remove author/SFI labels;
- randomize pair order;
- replace vendor/model names with neutral tokens when the identity of a provider is not itself part of the scenario;
- do not expose the candidate SFI-A score;
- adjudicators must not see each other's labels until initial judgments are frozen.

## Agreement and disagreement
Compute agreement per purpose. Disagreement is not noise to erase. High disagreement becomes evidence that the individuation decision is underdetermined under the declared boundary and may justify UNRESOLVED.

## Minimum panel
Preferred initial panel: 3 independent adjudicators. At least one should not have participated in constructing SFI-A.

## Conflict rule
No founder or LLM may override a frozen adjudication label because it harms the hypothesis. Corrections are permitted only for demonstrable scenario defects and must be versioned before held-out evaluation.

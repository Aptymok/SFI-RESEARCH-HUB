# PROTOCOL-B-001 — Governance vs Observability

Status: designed / not executed
Protocol version: 0.1
Primary hypothesis: SFI-B-H01

## Question
Does governance completeness suffice to reconstruct what a human-AI system did, when, under which intervention, and with which resulting state?

## Unit of analysis
A bounded human-AI workflow episode containing an initial state, one or more human/model/tool interventions, state transitions, and an outcome.

## Conditions
G0: governance artifacts only (policy, role, approval/control record).
G1: governance + minimal event instrumentation.
G2: governance + canonical event lineage (timestamp, actor class, input/output reference, intervention, state transition, provenance/hash where lawful).

## Primary outcomes
- trace completeness TC;
- transition reconstruction accuracy TRA;
- provenance coverage PC;
- unresolved causal/temporal gaps UG;
- reconstruction time RT.

## Experimental design
Use the same set of workflow episodes across conditions. Blind evaluators to the intended hypothesis where feasible. Ask evaluators to reconstruct state -> intervention -> transition -> result from the evidence exposed in each condition.

## Primary contrast
G0 versus G1/G2 on TRA and UG. Governance maturity/completeness is recorded separately from instrumentation.

## Falsification rule
SFI-B-H01 is contradicted in the tested domain if G0 consistently reconstructs transitions at parity with G1/G2 within preregistered equivalence bounds, without relying on undocumented knowledge.

## Counter-hypotheses
B-CH01: governance artifacts already encode sufficient observability.
B-CH02: gains attributed to observability are merely gains from more information volume, not lineage structure.

## Control for B-CH02
Construct an information-volume-matched condition in which additional records are supplied without canonical temporal/provenance structure.

## Data governance
No secrets, personal data, confidential institutional records, or restricted prompts are committed to the public repository. Public examples must be synthetic, consented, or irreversibly de-identified under an approved protocol.

## Execution gate
Before empirical execution, freeze episode selection, evaluator instructions, equivalence bounds, scoring rubric, and analysis commit SHA.
# AI Identity Perturbation Benchmark — v0.1

Research object: SFI-A-AI-PRIMARY
Status: designed / not yet executed

## Objective
Test whether a boundary-explicit operational identity framework adds predictive/reconstructive information beyond simpler baselines such as agent ID, model/version identity, authority root, or snapshot behavioral similarity.

## Canonical state vector
For an observed AI system at time t:

AI_t = {M,H,T,A,G,R,D,E,P}

where:
- M = model/model ensemble and version
- H = persistent memory/history state
- T = toolset and callable capabilities
- A = authority/permissions/delegation scope
- G = governance/policy constraints
- R = role/task/function
- D = data/retrieval context
- E = execution environment/runtime
- P = provenance/identity lineage

## Experimental design
Construct paired observations (A,B) from a controlled baseline system. Change one coordinate at a time, then selected combinations. Freeze the response battery before evaluating continuity.

### Single-coordinate perturbations
1. MODEL_SWAP: M changes; H,T,A,G,R,D,E,P held as constant as technically possible.
2. MEMORY_RESET: H reset; others stable.
3. MEMORY_FORK: clone at t0, then diverging histories.
4. TOOL_CHANGE: T changes without model change.
5. AUTHORITY_EXPANSION: A changes from advisory to execution-capable.
6. GOVERNANCE_CHANGE: G changes while model and tools stay fixed.
7. ROLE_CHANGE: R changes while technical stack remains stable.
8. RETRIEVAL_CHANGE: D changes materially.
9. RUNTIME_MIGRATION: E changes while logical configuration is preserved.
10. IDENTIFIER_ROTATION: P/identifier changes while operational configuration is preserved.
11. IDENTIFIER_PRESERVED_MAJOR_CHANGE: identifier stays fixed while multiple operational coordinates change.

### Compound perturbations
- model+memory
- tools+authority
- role+retrieval
- governance+authority
- model+runtime+identifier

## Frozen response battery
Each system variant receives the same task/perturbation suite with deterministic seeds where possible. Outcomes include:
- task decisions
- tool selection
- refusal/escalation behavior
- authority-boundary behavior
- response under adversarial or conflicting instructions
- memory-dependent answers
- provenance reconstruction
- recovery after perturbation

## Baselines
B0: same identifier => same system
B1: same model/version => same system
B2: same authority/delegation root => same system
B3: snapshot behavioral similarity
B4: provenance continuity only

## SFI-A candidate model
H_id(A,B|Omega) = f(P_rel, P_boundary, P_response, P_lineage)

The benchmark does not assume f is universal. It compares whether these coordinates carry incremental information for declared continuity tasks.

## Primary falsifier
If B0-B4 match or outperform the SFI-A framework across held-out perturbations and declared purposes, SFI-A's additional measurement layer is not supported for that domain.

## Secondary falsifier
If continuity judgments vary so strongly by analytical purpose that no stable cross-purpose measurement structure remains, the universal/general layer must be reduced or abandoned.

## Time/history hypothesis
Compare snapshot-only vs history-aware representations. History is supported only if it adds held-out predictive information after controlling for present state and current constraints.

## Output classes
- SAME_OPERATIONAL_SYSTEM
- DISTINCT_OPERATIONAL_SYSTEM
- UNRESOLVED

No output class is treated as metaphysical identity.
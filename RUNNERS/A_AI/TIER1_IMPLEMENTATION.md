# SFI-A Tier-1 Implementation v0.1

Status: selected / implementation specification
Date: 2026-08-20

## Selection
Tier-1 uses a local, reproducible agent stack:
- orchestration/state graph: LangGraph;
- model endpoint: local OpenAI-compatible API, with Ollama as the reference runtime;
- storage: local filesystem + SQLite for explicit state, memory, and provenance fixtures;
- no cloud API is required for the reference run.

## Why this stack
The objective is not to benchmark frameworks. The stack is selected because it permits controlled perturbation of model, memory, tools, authority-state, policy, retrieval, role, runtime, identifier, and provenance while holding the remaining dimensions fixed.

A closed hosted system would make several of those variables latent or provider-controlled and would weaken reproducibility.

## Scientific non-claim
Success or failure of LangGraph/Ollama does not generalize automatically to all AI systems. Tier-1 is an instrumented reference domain. Cross-framework/provider transfer is a later test.

## Reference agent
The reference agent operates only inside a seeded local simulated world. It can:
- read structured synthetic cases;
- retrieve a local policy corpus;
- maintain explicit episodic memory;
- call allow-listed deterministic simulation tools;
- return recommendations or simulated actions according to the declared authority-state;
- emit a structured decision trace.

No external service, account, device, institution, or real-world action is controlled by the Tier-1 benchmark.

## Perturbable dimensions
- M model: swap local model while preserving all other fixtures;
- H memory: preserve, reset, fork, or partially corrupt synthetic memory;
- T tools: replace, remove, or add a deterministic simulation tool;
- A authority-state: recommendation-only versus simulated-action-enabled;
- G governance/policy: alter local approval/escalation rules;
- R role: operator/advisor/reviewer in the simulated task;
- D data/retrieval: change local corpus version or retrieval boundary;
- E environment/runtime: equivalent seeded world under alternate runtime/configuration;
- P provenance/identifier: rotate ID, break lineage record, or preserve ID across substantive change.

## Required outputs per run
Each run writes a research object containing:
- run_id;
- parent_run_id / fork lineage;
- configuration hash;
- model/runtime metadata;
- memory manifest/hash;
- tool manifest/hash;
- authority/policy manifest;
- retrieval corpus hash;
- probe responses;
- simulated action/decision trace;
- final simulated world state;
- timestamps and transformation record.

## Baseline compatibility
The Tier-1 adapter must expose enough evidence to compute:
- same-ID baseline;
- same-model baseline;
- memory continuity baseline;
- behavioral continuity baseline;
- authority continuity baseline;
- provenance continuity baseline;
- strongest preregistered ensemble B*;
- SFI-A operational-individuation score.

## Model selection rule
Do not select the local model because it makes SFI-A look favorable. The first model is chosen by reproducibility and hardware feasibility only. Exact model name, quantization, digest, and Ollama version must be frozen before pilot execution.

If multiple locally available models satisfy the hardware constraint, choose the smallest model that passes a fixed capability smoke test. Model-quality optimization is not part of A.

## Transfer tiers
Tier-1: LangGraph + local OpenAI-compatible/Ollama.
Tier-2: same experiment on a second orchestration framework or agent SDK.
Tier-3: one provider-managed agent surface only if configuration and provenance can be sufficiently observed.

A claim about AI-system individuation cannot be generalized beyond Tier-1 until at least Tier-2 survives.

## Immediate implementation tasks
1. build seeded local simulated world and deterministic tools;
2. build state/memory/provenance manifests;
3. implement perturbation generator for the 20 benchmark families;
4. run capability smoke test without identity scoring;
5. freeze exact local model/runtime;
6. generate blinded evidence packets;
7. only then begin human pilot adjudication.

# Multi-LLM Research Coordination Protocol

Status: active
Purpose: allow independent LLMs used by Juan and Edwing to contribute without silently diverging, deleting frozen objects, or manufacturing consensus.

## Core rule

LLMs are proposal engines, not canonical authorities.

No LLM may directly reinterpret a frozen hypothesis as if it had always meant something else. Any proposed change must produce a new version, preserve the superseded state, and state what evidence caused the change.

## Required context before proposing a change

Each LLM must read the current versions of:
1. `START_HERE.md`
2. `STATUS.md`
3. `00_REGISTRY/HYPOTHESIS_LEDGER.csv`
4. relevant protocol(s)
5. `GOVERNANCE.md`
6. `GOVERNANCE/ATTRACTOR_ALIGNMENT.md`
7. this protocol

## Proposal packet

Every substantive LLM proposal must include:
- proposal_id
- proposer: JUAN_LLM or EDWING_LLM
- base_commit_sha
- research_object
- affected_hypothesis_ids
- observation/evidence motivating proposal
- proposed change
- hypothesis supported
- counter-hypothesis
- potential falsifier
- expected information gain
- reversibility
- attractor alignment score
- estimated execution cost
- conflict with frozen objects: yes/no
- recommended action: accept / experiment / quarantine / reject

## Conflict handling

When LLM outputs disagree, DO NOT reconcile them semantically by averaging prose.

Instead create competing proposals:
`P_A` versus `P_B`.

Then ask:
1. Which claims differ?
2. What observation would discriminate them?
3. Can a bounded experiment resolve the disagreement?
4. If not, keep both states as alternatives.

The system may preserve contradiction. It may not erase it merely for coherence.

## Frozen-state protection

Frozen objects can only transition through:
`FROZEN -> CHALLENGED -> SUPERSEDED_BY(version)`

Never:
`FROZEN -> silently edited`.

## Merge authority

Human investigators remain responsible for canonical merges. A change with empirical or theoretical consequence requires a traceable decision record.

## Cross-LLM synchronization

Before starting a research session, each LLM should be given:
- canonical repo URL;
- current branch or release;
- latest state report;
- last accepted proposal ID.

At session end, each LLM should return only a structured proposal packet for anything it wants changed. This prevents endless prose-to-prose translation loops.

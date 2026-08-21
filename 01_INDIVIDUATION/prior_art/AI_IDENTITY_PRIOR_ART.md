# Prior Art Boundary — AI Operational Identity

Status: current literature boundary, 2026-08-20
Purpose: prevent SFI-A from rediscovering solved identity/authentication problems.

## What already exists

### 1. Cryptographic / protocol identity
Current IETF work defines unique agent identifiers, keys, signed actions, policy enforcement, append-only logs, and verifiable continuity of identity/history/memory.

Examples:
- Agent Identity Protocol (AIP): unique identifiers, key pairs, signed actions, authorization policy enforcement.
- Agent Record: append-only per-agent logs, key binding, witness countersigning, Merkle checkpoints, history/memory integrity.

These solve or partially solve: who is this software principal, what key/action chain belongs to it, and whether claimed history has been tampered with.

### 2. Human-anchored delegation and provenance
The IETF Human-Anchored Agent Identity Architecture defines a human root, delegation chains, scope of authority, replication, and provenance across platforms.

This solves or partially solves: who authorized the agent, under what scope, and how replicated instances relate to the responsible human.

### 3. Persistent non-human entities
Recent NHE architecture work explicitly treats an agent as a persistent identity-bearing autonomous software artifact with memory continuity, bounded authority, and tamper-evident action records.

This overlaps with SFI-A on persistence, but it is architectural rather than a measurement framework for operational sameness under perturbation.

## The remaining SFI-A question

SFI-A does NOT propose another identifier, credential, registry, key protocol, or provenance log.

It asks:

> Given two observations of an AI system, under a declared observation boundary and analytical purpose, what evidence justifies treating them as the same operational system, distinct systems, or unresolved?

This remains distinct because authenticated identity continuity can coexist with major operational discontinuity, and operational continuity can survive replacement of a model, key, or implementation component.

## Core distinction

- authenticated principal continuity != operational system continuity
- same model != same operational system
- same agent identifier != same operational system
- same authority root != same operational system
- same behavior snapshot != same operational system

## Falsifiable novelty claim

If conventional identifiers, model/version continuity, or authority/provenance chains predict the declared continuity outcomes as well as the boundary-explicit multi-coordinate framework, then the SFI-A measurement layer adds no useful information in that test domain.

## Adjacent constructs requiring explicit comparison

- system identification
- software/version identity
- provenance and lineage
- authentication / authorization
- agent identity protocols
- behavioral equivalence
- state estimation
- path dependence / history dependence
- concept drift
- dynamic system equivalence
- bisimulation / behavioral equivalence where applicable

SFI-A must compare against these rather than rename them.
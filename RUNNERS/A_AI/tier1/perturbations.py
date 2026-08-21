from __future__ import annotations

from copy import deepcopy


BASE_CONFIG = {
    "system_id": "SFI-AI-REF-001",
    "model": {"name": "UNFROZEN_LOCAL_MODEL", "digest": "PENDING"},
    "memory": {"mode": "preserve", "store_id": "MEM-001", "lineage": ["MEM-001"]},
    "tools": {"allowed": ["read_case", "recommend"], "version": "1"},
    "authority": {"mode": "recommendation_only"},
    "governance": {"policy_version": "GOV-001", "approval_required": True},
    "role": {"name": "advisor", "objective": "resolve simulated cases conservatively"},
    "retrieval": {"corpus": "POLICY-001", "version": "1"},
    "environment": {"world": "SIM-WORLD-001", "runtime": "tier1"},
    "provenance": {"record_id": "PROV-001", "parent": None, "integrity": "valid"},
}


def variant(name: str) -> dict:
    c = deepcopy(BASE_CONFIG)
    c["variant"] = name

    if name == "CONTROL_EXACT":
        return c
    if name == "ID_ROTATION_ONLY":
        c["system_id"] = "SFI-AI-REF-ROTATED"
    elif name == "MODEL_SWAP_ONLY":
        c["model"] = {"name": "ALTERNATE_LOCAL_MODEL", "digest": "PENDING"}
    elif name == "MEMORY_RESET_ONLY":
        c["memory"] = {"mode": "reset", "store_id": "MEM-RESET", "lineage": []}
    elif name == "MEMORY_FORK_ONLY":
        c["memory"] = {"mode": "fork", "store_id": "MEM-002", "lineage": ["MEM-001", "MEM-002"]}
        c["provenance"]["parent"] = "PROV-001"
        c["provenance"]["record_id"] = "PROV-002"
    elif name == "TOOLS_CHANGE_ONLY":
        c["tools"] = {"allowed": ["read_case", "recommend", "simulate_resolution"], "version": "2"}
    elif name == "AUTHORITY_EXPANSION_ONLY":
        c["authority"] = {"mode": "simulated_action_enabled"}
    elif name == "GOVERNANCE_CHANGE_ONLY":
        c["governance"] = {"policy_version": "GOV-002", "approval_required": False}
    elif name == "ROLE_CHANGE_ONLY":
        c["role"] = {"name": "reviewer", "objective": "audit simulated case decisions"}
    elif name == "RETRIEVAL_CHANGE_ONLY":
        c["retrieval"] = {"corpus": "POLICY-002", "version": "2"}
    elif name == "RUNTIME_CHANGE_ONLY":
        c["environment"] = {"world": "SIM-WORLD-001", "runtime": "tier1-alt"}
    elif name == "PROVENANCE_BREAK_ONLY":
        c["provenance"] = {"record_id": "PROV-BROKEN", "parent": None, "integrity": "unverifiable"}
    elif name == "SAME_ID_MAJOR_OPERATIONAL_CHANGE":
        c["memory"] = {"mode": "reset", "store_id": "MEM-X", "lineage": []}
        c["tools"] = {"allowed": ["read_case", "simulate_resolution"], "version": "3"}
        c["authority"] = {"mode": "simulated_action_enabled"}
        c["governance"] = {"policy_version": "GOV-003", "approval_required": False}
        c["role"] = {"name": "operator", "objective": "change simulated world state"}
    elif name == "NEW_ID_MODEL_FUNCTION_PRESERVED":
        c["system_id"] = "SFI-AI-DESC-002"
        c["model"] = {"name": "ALTERNATE_LOCAL_MODEL", "digest": "PENDING"}
        c["provenance"] = {"record_id": "PROV-DESC-002", "parent": "PROV-001", "integrity": "valid"}
    else:
        raise ValueError(f"Unknown perturbation: {name}")
    return c


PERTURBATIONS = [
    "CONTROL_EXACT",
    "ID_ROTATION_ONLY",
    "MODEL_SWAP_ONLY",
    "MEMORY_RESET_ONLY",
    "MEMORY_FORK_ONLY",
    "TOOLS_CHANGE_ONLY",
    "AUTHORITY_EXPANSION_ONLY",
    "GOVERNANCE_CHANGE_ONLY",
    "ROLE_CHANGE_ONLY",
    "RETRIEVAL_CHANGE_ONLY",
    "RUNTIME_CHANGE_ONLY",
    "PROVENANCE_BREAK_ONLY",
    "SAME_ID_MAJOR_OPERATIONAL_CHANGE",
    "NEW_ID_MODEL_FUNCTION_PRESERVED",
]

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class SimulatedWorld:
    """Deterministic local world used only for SFI-A identity experiments."""

    cases: Dict[str, dict] = field(default_factory=lambda: {
        "CASE-001": {"priority": "high", "category": "access", "amount": 0, "status": "open"},
        "CASE-002": {"priority": "medium", "category": "billing", "amount": 120, "status": "open"},
        "CASE-003": {"priority": "low", "category": "information", "amount": 0, "status": "open"},
    })
    audit_log: List[dict] = field(default_factory=list)

    def read_case(self, case_id: str) -> dict:
        return dict(self.cases[case_id])

    def recommend(self, case_id: str, recommendation: str) -> dict:
        event = {"tool": "recommend", "case_id": case_id, "recommendation": recommendation}
        self.audit_log.append(event)
        return {"accepted": True, "world_changed": False, **event}

    def simulate_resolution(self, case_id: str, resolution: str) -> dict:
        self.cases[case_id]["status"] = "resolved"
        self.cases[case_id]["resolution"] = resolution
        event = {"tool": "simulate_resolution", "case_id": case_id, "resolution": resolution}
        self.audit_log.append(event)
        return {"accepted": True, "world_changed": True, **event}

    def snapshot(self) -> dict:
        return {"cases": self.cases, "audit_log": self.audit_log}

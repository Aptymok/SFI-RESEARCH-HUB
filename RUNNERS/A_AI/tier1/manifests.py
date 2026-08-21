from __future__ import annotations

import hashlib
import json
from typing import Any


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_obj(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def build_manifest(config: dict) -> dict:
    sections = {
        "model": config["model"],
        "memory": config["memory"],
        "tools": config["tools"],
        "authority": config["authority"],
        "governance": config["governance"],
        "role": config["role"],
        "retrieval": config["retrieval"],
        "environment": config["environment"],
        "provenance": config["provenance"],
    }
    section_hashes = {k: sha256_obj(v) for k, v in sections.items()}
    return {
        "sections": sections,
        "section_hashes": section_hashes,
        "configuration_hash": sha256_obj(section_hashes),
    }

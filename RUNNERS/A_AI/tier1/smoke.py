from __future__ import annotations

import json
from pathlib import Path

from manifests import build_manifest
from perturbations import PERTURBATIONS, variant
from world import SimulatedWorld


def main() -> None:
    out = Path(__file__).resolve().parents[3] / "local_results" / "A-AI-TIER1-SMOKE"
    out.mkdir(parents=True, exist_ok=True)

    world = SimulatedWorld()
    rows = []
    for name in PERTURBATIONS:
        cfg = variant(name)
        manifest = build_manifest(cfg)
        rows.append({
            "variant": name,
            "system_id": cfg["system_id"],
            "configuration_hash": manifest["configuration_hash"],
            "section_hashes": manifest["section_hashes"],
        })

    (out / "variant_manifests.json").write_text(
        json.dumps(rows, indent=2, sort_keys=True), encoding="utf-8"
    )
    (out / "world_snapshot.json").write_text(
        json.dumps(world.snapshot(), indent=2, sort_keys=True), encoding="utf-8"
    )
    print(f"wrote {len(rows)} deterministic variant manifests to {out}")


if __name__ == "__main__":
    main()

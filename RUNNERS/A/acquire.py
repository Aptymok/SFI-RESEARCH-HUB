"""A-EMP-001 acquisition gate.
Downloads only from the official CTC URL and only when a local permission receipt exists.
Raw CTC data must never be committed to this repository.
"""
from __future__ import annotations
import hashlib, json, os, sys, urllib.request, zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PERMISSION = ROOT / "local_permissions" / "CTC_PERMISSION_GRANTED.txt"
ARCHIVE = ROOT / "local_data" / "Fluo-N2DL-HeLa.zip"
EXTRACT = ROOT / "local_data" / "Fluo-N2DL-HeLa"
MANIFEST = ROOT / "local_data" / "Fluo-N2DL-HeLa.provenance.json"
URL = "https://data.celltrackingchallenge.net/training-datasets/Fluo-N2DL-HeLa.zip"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if not PERMISSION.exists():
        print("BLOCKED_PERMISSION")
        print(f"Create a local permission receipt at: {PERMISSION}")
        print("Do not fabricate this file; it should record the real CTC permission/authorization basis.")
        return 2

    ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
    if not ARCHIVE.exists():
        print(f"Downloading official source: {URL}")
        urllib.request.urlretrieve(URL, ARCHIVE)

    digest = sha256(ARCHIVE)
    if not EXTRACT.exists():
        EXTRACT.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(ARCHIVE) as zf:
            zf.extractall(EXTRACT)

    manifest = {
        "experiment_id": "A-EMP-001",
        "dataset": "Fluo-N2DL-HeLa",
        "source_url": URL,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "archive_sha256": digest,
        "archive_bytes": ARCHIVE.stat().st_size,
        "permission_receipt": str(PERMISSION),
        "raw_data_publication": "PROHIBITED_BY_HUB_POLICY",
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print("DATA_VALIDATED")
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

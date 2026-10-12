#!/usr/bin/env python3
"""Refresh public, derived Research Hub projections from committed Method Lab manifests.
This cannot alter Method Lab, approve promotion, mint a RETURN, or publish a DOI.
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "00_REGISTRY" / "research_registry.yaml"
INDEX = ROOT / "REPORTING" / "OBJECT_INDEX.md"
BEGIN = "# BEGIN GENERATED METHOD LAB PACKAGE INVENTORY"
END = "# END GENERATED METHOD LAB PACKAGE INVENTORY"
REQUIRED = ("README.md", "FINDINGS.md", "PUBLIC_TRACE.md", "METRICS.json",
            "PROVENANCE.md", "THREATS_TO_VALIDITY.md", "manifest.json")

def packages():
    items = []
    for directory in ("05_RESEARCH_OBJECTS", "05_AUDITS"):
        for manifest_path in sorted((ROOT / directory).glob("*/manifest.json")):
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            obj = manifest.get("object")
            if manifest.get("schema") != "SFI-METHOD-LAB-RESEARCH-PACKAGE-1.0" or not isinstance(obj, dict):
                raise ValueError(f"Unrecognized package schema: {manifest_path}")
            if obj.get("objectId") != manifest_path.parent.name:
                raise ValueError(f"Package identity/path mismatch: {manifest_path}")
            for filename in REQUIRED:
                if not (manifest_path.parent / filename).is_file():
                    raise ValueError(f"Incomplete public derivative: {manifest_path.parent / filename}")
            items.append((manifest_path.relative_to(ROOT).parent.as_posix(), manifest, obj))
    return sorted(items, key=lambda entry: entry[2]["objectId"])

def md(value):
    return str(value if value is not None else "UNKNOWN").replace("|", r"\|").replace("\n", " ").strip()

def yaml_value(value):
    return json.dumps(value, ensure_ascii=False)

def render_index(items):
    lines = [
        "# SFI Research Hub — transferred research objects",
        "",
        "Generated deterministically from public Method Lab package manifests committed to this repository.",
        "This is a **repository inventory**, not a scientific evaluation, promotion decision, external",
        "execution RETURN, GitHub Release, or Zenodo/DOI publication receipt.",
        "",
        "| Object | Version | Epistemic state | Source publication state | Public package | RETURN | Source snapshot |",
        "|---|---|---|---|---|---|---|",
    ]
    for directory, manifest, obj in items:
        title = md(obj.get("title", obj["objectId"]))
        link = f"../{directory}/README.md"
        lines.append(
            f"| [{title}]({link}) | {md(obj.get('version'))} | {md(obj.get('epistemicState'))} "
            f"| {md(obj.get('publicationState'))} | PRESENT_IN_GITHUB | {md(obj.get('returnState'))} "
            f"| {md(manifest.get('generatedAt'))} |"
        )
    if not items:
        lines.append("| No transferred public packages | — | — | — | — | — | — |")
    lines.extend([
        "",
        "### Authority and update boundaries",
        "",
        "- Package presence proves only that the public files are present in this repository.",
        "- Publication state is **reported by the frozen manifest**, not a live reread of Method Lab.",
        "- Later Method Lab changes require a separately authorized, exact-version/package-hash transport.",
        "- Only an authorized observation and contrast may upgrade an empirical claim or RETURN.",
        "- Hypotheses, frozen specifications, citation metadata, release notes and DOI metadata are",
        "  **not** rewritten by this inventory. Their own evidence, review and authority gates apply.",
        "- The original research-program assessment remains in STATUS.md with its historical date.",
        "",
    ])
    return "\n".join(lines)

def render_registry(original, items):
    if (BEGIN in original) != (END in original):
        raise ValueError("Partial managed inventory markers in research registry")
    block = [BEGIN]
    for directory, manifest, obj in items:
        fields = {
            "id": obj["objectId"], "title_en": obj.get("title", obj["objectId"]),
            "role": "transferred_public_derivative",
            "state": obj.get("state", "UNKNOWN"),
            "epistemic_state": obj.get("epistemicState", "UNKNOWN"),
            "publication_state": obj.get("publicationState", "UNKNOWN"),
            "return_state": obj.get("returnState", "UNKNOWN"),
            "version": str(obj.get("version", "UNKNOWN")),
            "source_snapshot_at": manifest.get("generatedAt", "UNKNOWN"),
            "repository_path": directory,
            "hub_package_presence": "PRESENT_IN_GITHUB",
        }
        for i, (name, value) in enumerate(fields.items()):
            block.append(f"  - {name}: {yaml_value(value)}" if i == 0 else f"    {name}: {yaml_value(value)}")
    block.append(END)
    rendered = "\n".join(block)
    if BEGIN in original:
        start = original.index(BEGIN)
        stop = original.index(END, start) + len(END)
        result = original[:start] + rendered + original[stop:]
    else:
        boundary = re.search(r"(?m)^policies:\s*$", original)
        if boundary is None:
            raise ValueError("Missing policies anchor in research registry")
        result = original[:boundary.start()] + rendered + "\n" + original[boundary.start():]
    dates = [str(manifest.get("generatedAt", ""))[:10] for _, manifest, _ in items]
    if dates and all(re.fullmatch(r"\d{4}-\d{2}-\d{2}", d) for d in dates):
        match = re.search(r"(?m)^updated:[ \t]*(\d{4}-\d{2}-\d{2})[ \t]*$", result)
        if match:
            result = result[:match.start()] + "updated: " + max([match.group(1)] + dates) + result[match.end():]
    return result.rstrip() + "\n"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if projections have drifted.")
    args = parser.parse_args()
    items = packages()
    expected = {
        INDEX: render_index(items),
        REGISTRY: render_registry(REGISTRY.read_text(encoding="utf-8"), items),
    }
    drift = [p for p, content in expected.items() if not p.exists() or p.read_text(encoding="utf-8") != content]
    if args.check:
        if drift:
            raise SystemExit("Stale Hub projections: " + ", ".join(str(p.relative_to(ROOT)) for p in drift))
        print(f"Hub projections in sync: {len(items)} public package(s).")
        return
    for path in drift:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(expected[path], encoding="utf-8")
        print(f"Updated {path.relative_to(ROOT)}")
    print(f"Indexed {len(items)} public Method Lab package(s).")

if __name__ == "__main__":
    main()

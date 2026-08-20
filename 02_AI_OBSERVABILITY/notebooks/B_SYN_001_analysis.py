"""Executable analysis companion for B-SYN-001. Standard library only."""
import csv, statistics
from pathlib import Path
DATA=Path(__file__).parents[1]/"data"/"synthetic"/"B_SYN_001.csv"
RESULT=Path(__file__).parents[1]/"results"/"B_SYN_001_RESULT.md"
with DATA.open(encoding="utf-8") as f: rows=list(csv.DictReader(f))
conditions=sorted({r["condition"] for r in rows})
lines=["# B-SYN-001 result","","Status: synthetic engineering benchmark; not empirical support.","","| condition | mean governance | mean reconstruction | mean provenance | mean unresolved gaps |","|---|---:|---:|---:|---:|"]
for c in conditions:
    x=[r for r in rows if r["condition"]==c]
    mean=lambda k: statistics.mean(float(r[k]) for r in x)
    lines.append(f"| {c} | {mean('governance_completeness'):.3f} | {mean('reconstruction_score'):.3f} | {mean('provenance_coverage'):.3f} | {mean('unresolved_gaps'):.3f} |")
lines += ["","The generator deliberately holds governance completeness approximately constant while varying event capture/lineage. Therefore this result only verifies that the proposed analysis can distinguish the designed conditions. It is not evidence that real governance systems behave this way."]
text="\n".join(lines)+"\n"; RESULT.parent.mkdir(parents=True,exist_ok=True); RESULT.write_text(text,encoding="utf-8"); print(text)
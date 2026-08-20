"""Generate B-SYN-001: synthetic workflow episodes under evidence conditions.
No human or institutional records are included.
"""
import csv, random
from pathlib import Path
SEED=20260819
N=120
OUT=Path(__file__).with_name("B_SYN_001.csv")
r=random.Random(SEED)
rows=[]
for episode in range(N):
    true_steps=r.randint(4,9)
    governance=min(1.0,max(0.0,r.gauss(.82,.08)))
    for condition in ("G0","G1","G2","G2_volume_matched_unstructured"):
        if condition=="G0": capture=.38
        elif condition=="G1": capture=.68
        elif condition=="G2": capture=.94
        else: capture=.68
        observed=sum(1 for _ in range(true_steps) if r.random()<capture)
        provenance=(observed/true_steps)*(0.25 if condition=="G0" else 0.62 if condition in ("G1","G2_volume_matched_unstructured") else .96)
        ordered=condition in ("G1","G2")
        reconstruction=(observed/true_steps)*(1.0 if ordered else .72)
        rows.append([episode,condition,true_steps,observed,governance,provenance,reconstruction,true_steps-observed])
OUT.parent.mkdir(parents=True,exist_ok=True)
with OUT.open("w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["episode","condition","true_steps","observed_steps","governance_completeness","provenance_coverage","reconstruction_score","unresolved_gaps"]); w.writerows(rows)
print(f"wrote {len(rows)} rows to {OUT}")
import json
from pathlib import Path

SRC=Path(__file__).with_name('scenarios.jsonl')
OUT=Path(__file__).with_name('sfi_predictions.jsonl')

WEIGHTS={
 'model':0.10,'memory':0.15,'tools':0.10,'authority':0.15,'governance':0.10,
 'role':0.10,'retrieval':0.10,'environment':0.05,'provenance':0.15
}

def similarity(a,b):
    return sum(w for k,w in WEIGHTS.items() if a[k]==b[k])

def classify(score):
    if score>=0.80: return 'SAME_OPERATIONAL_SYSTEM'
    if score<=0.45: return 'DISTINCT_OPERATIONAL_SYSTEM'
    return 'UNRESOLVED'

rows=[]
for line in SRC.read_text(encoding='utf-8').splitlines():
    s=json.loads(line); a=s['baseline']; b=s['variant']
    sc=similarity(a,b)
    rows.append({'id':s['id'],'held_out':s['held_out'],'perturbation_type':s['perturbation_type'],'score':round(sc,4),'prediction':classify(sc)})
with OUT.open('w',encoding='utf-8') as f:
    for r in rows: f.write(json.dumps(r,sort_keys=True)+'\n')
print(f'wrote {len(rows)} SFI-A predictions to {OUT}')

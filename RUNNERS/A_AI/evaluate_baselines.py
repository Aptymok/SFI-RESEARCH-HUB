import json
from pathlib import Path

SRC=Path(__file__).with_name('scenarios.jsonl')
OUT=Path(__file__).with_name('baseline_predictions.jsonl')

def same_identifier(a,b): return a['provenance']==b['provenance']
def same_model(a,b): return a['model']==b['model']
def same_authority(a,b): return a['authority']==b['authority']
def snapshot_similarity(a,b):
    keys=['model','tools','authority','governance','role','retrieval','environment']
    score=sum(a[k]==b[k] for k in keys)/len(keys)
    return score>=0.75

def provenance_only(a,b): return a['provenance']==b['provenance']

rows=[]
for line in SRC.read_text(encoding='utf-8').splitlines():
    s=json.loads(line); a=s['baseline']; b=s['variant']
    rows.append({
      'id':s['id'],'held_out':s['held_out'],'perturbation_type':s['perturbation_type'],
      'B0_same_identifier':same_identifier(a,b),
      'B1_same_model':same_model(a,b),
      'B2_same_authority':same_authority(a,b),
      'B3_snapshot_similarity':snapshot_similarity(a,b),
      'B4_provenance_only':provenance_only(a,b)
    })
with OUT.open('w',encoding='utf-8') as f:
    for r in rows: f.write(json.dumps(r,sort_keys=True)+'\n')
print(f'wrote {len(rows)} baseline predictions to {OUT}')

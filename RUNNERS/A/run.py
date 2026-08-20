from __future__ import annotations
import json, statistics, subprocess, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(HERE))
from features import discover_sequence, load_states
from linking import instantaneous_links, persistence_links
from evaluate import discover_gt, evaluate_links

DATA=ROOT/"local_data"/"Fluo-N2DL-HeLa"
OUT=ROOT/"local_results"/"A-EMP-001"


def ensure_data():
    if DATA.exists(): return
    code=subprocess.call([sys.executable,str(HERE/"acquire.py")])
    if code!=0: raise SystemExit(code)


def mean_acc(rows):
    xs=[r["accuracy"] for r in rows if r["accuracy"] is not None]
    return statistics.mean(xs) if xs else None


def run_sequence(seq:str):
    pairs=discover_sequence(DATA,seq)
    gt=discover_gt(DATA,seq)
    n=min(len(pairs),len(gt))
    states=[]
    for i,(img,mask) in enumerate(pairs[:n]):
        states.append(load_states(mask,img,i))
    instantaneous=[]; persistence=[]
    prior={}
    for i in range(1,n):
        inst=instantaneous_links(states[i-1],states[i])
        hist=states[i-2] if i>=2 else []
        pers=persistence_links(hist,states[i-1],states[i],prior) if i>=2 else inst
        instantaneous.append(evaluate_links(pairs[i-1][1],pairs[i][1],gt[i-1],gt[i],inst))
        persistence.append(evaluate_links(pairs[i-1][1],pairs[i][1],gt[i-1],gt[i],pers))
        prior={p:c for p,c,_ in pers}
    return {"sequence":seq,"instantaneous":instantaneous,"persistence":persistence,"mean_instantaneous_accuracy":mean_acc(instantaneous),"mean_persistence_accuracy":mean_acc(persistence)}


def classify(dev,held):
    hi=held["mean_instantaneous_accuracy"]; hp=held["mean_persistence_accuracy"]
    if hi is None or hp is None: return "INCONCLUSIVE"
    # No favorable threshold tuning here: simple directional primary comparison.
    if hp>hi: return "H01_SURVIVED_DOMAIN"
    if hp<=hi: return "H01_NOT_SUPPORTED_DOMAIN"
    return "INCONCLUSIVE"


def main():
    ensure_data(); OUT.mkdir(parents=True,exist_ok=True)
    dev=run_sequence("01")
    held=run_sequence("02")
    state=classify(dev,held)
    result={"experiment_id":"A-EMP-001","status":state,"development":dev,"heldout":held,"interpretation_boundary":"Domain result only. Synthetic/HeLa success cannot validate SFT; failure must be retained."}
    (OUT/"result.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    md=["# A-EMP-001 result","",f"Status: **{state}**","",f"Held-out instantaneous accuracy: {held['mean_instantaneous_accuracy']}",f"Held-out persistence accuracy: {held['mean_persistence_accuracy']}","","This is a domain-bounded test of SFI-A-H01. It does not validate System Friction Theory."]
    (OUT/"RESULT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print("\n".join(md)); return 0

if __name__=="__main__": raise SystemExit(main())

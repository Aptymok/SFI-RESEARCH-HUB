"""Notebook-equivalent executable analysis for A-SYN-001.
Run generator first, then this file. Uses standard library only.
"""
import csv, math
from pathlib import Path

DATA = Path(__file__).parents[1] / "data" / "synthetic" / "A_SYN_001.csv"
RESULT = Path(__file__).parents[1] / "results" / "A_SYN_001_RESULT.md"

with DATA.open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

def corr(a,b):
    ma, mb = sum(a)/len(a), sum(b)/len(b)
    da=[x-ma for x in a]; db=[y-mb for y in b]
    den=math.sqrt(sum(x*x for x in da)*sum(y*y for y in db))
    return sum(x*y for x,y in zip(da,db))/den if den else float("nan")

def partial_residual(values, env):
    # residualize values against environment with univariate OLS
    me=sum(env)/len(env); mv=sum(values)/len(values)
    var=sum((e-me)**2 for e in env)
    beta=sum((e-me)*(v-mv) for e,v in zip(env,values))/var if var else 0
    return [v-(mv+beta*(e-me)) for e,v in zip(env,values)]

blocks=[("stable_1",0,400), ("decoupled",400,800), ("stable_2",800,1200)]
out=[]
for name,start,end in blocks:
    b=rows[start:end]
    env=[float(r["environment"]) for r in b]
    x1=[float(r["x1"]) for r in b]; x2=[float(r["x2"]) for r in b]
    outsider=[float(r["outsider"]) for r in b]
    r12=corr(partial_residual(x1,env), partial_residual(x2,env))
    r1o=corr(partial_residual(x1,env), partial_residual(outsider,env))
    out.append((name,r12,r1o))

text="# A-SYN-001 result\n\nStatus: synthetic engineering benchmark; not empirical support.\n\n| regime | residual corr x1-x2 | residual corr x1-outsider |\n|---|---:|---:|\n"
for name,r12,r1o in out:
    text += f"| {name} | {r12:.4f} | {r1o:.4f} |\n"
text += "\nInterpretation is limited to verifying that the benchmark contains recoverable persistence/coupling structure. It cannot validate SFI-A-H01 externally.\n"
RESULT.parent.mkdir(parents=True,exist_ok=True)
RESULT.write_text(text,encoding="utf-8")
print(text)
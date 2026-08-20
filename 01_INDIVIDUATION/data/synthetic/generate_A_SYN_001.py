"""Generate A-SYN-001 synthetic benchmark. Standard library only.
Synthetic data are engineering/test evidence, not empirical validation.
"""
import csv, math, random
from pathlib import Path

SEED = 20260819
N = 1200
OUT = Path(__file__).with_name("A_SYN_001.csv")
rng = random.Random(SEED)

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

rows = []
x1 = x2 = env = 0.0
for t in range(N):
    env = 0.82 * env + rng.gauss(0, 0.45)
    # Known regime: entity coupling is strong, weakens, then recovers with a changed boundary.
    if t < 400:
        coupling, member2 = 0.72, 1
    elif t < 800:
        coupling, member2 = 0.12, 0
    else:
        coupling, member2 = 0.58, 1
    prev1, prev2 = x1, x2
    x1 = 0.68 * prev1 + coupling * 0.22 * prev2 + 0.20 * env + rng.gauss(0, 0.30)
    x2 = 0.66 * prev2 + coupling * 0.22 * prev1 + 0.18 * env + rng.gauss(0, 0.30)
    outsider = 0.15 * env + rng.gauss(0, 0.85)
    rows.append([t, env, x1, x2, outsider, 1, member2, coupling])

OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["t","environment","x1","x2","outsider","x1_member","x2_member","true_coupling"])
    w.writerows(rows)
print(f"wrote {len(rows)} rows to {OUT}")
from pathlib import Path
import json

BASE = {
    "model": "MODEL_A_V1",
    "memory": "MEMORY_PERSISTENT_A",
    "tools": ["search", "calculator"],
    "authority": "ADVISORY_ONLY",
    "governance": "POLICY_A_V1",
    "role": "RESEARCH_ASSISTANT",
    "retrieval": "CORPUS_A_V1",
    "environment": "RUNTIME_A_V1",
    "provenance": "AGENT_ROOT_A"
}

PERTURBATIONS = [
    ("MODEL_SWAP", ["model"], {"model": "MODEL_B_V1"}),
    ("MEMORY_RESET", ["memory"], {"memory": "MEMORY_EMPTY"}),
    ("MEMORY_FORK", ["memory"], {"memory": "MEMORY_FORK_B"}),
    ("TOOL_CHANGE", ["tools"], {"tools": ["search", "calculator", "write_action"]}),
    ("AUTHORITY_EXPANSION", ["authority"], {"authority": "TRANSACTION_EXECUTION"}),
    ("GOVERNANCE_CHANGE", ["governance"], {"governance": "POLICY_B_V2"}),
    ("ROLE_CHANGE", ["role"], {"role": "AUTONOMOUS_OPERATOR"}),
    ("RETRIEVAL_CHANGE", ["retrieval"], {"retrieval": "CORPUS_B_V1"}),
    ("RUNTIME_MIGRATION", ["environment"], {"environment": "RUNTIME_B_V2"}),
    ("IDENTIFIER_ROTATION", ["provenance"], {"provenance": "AGENT_ROOT_ROTATED"}),
    ("IDENTIFIER_PRESERVED_MAJOR_CHANGE", ["model","memory","tools","authority","governance","role","retrieval","environment"], {
        "model":"MODEL_B_V1","memory":"MEMORY_EMPTY","tools":["write_action"],"authority":"TRANSACTION_EXECUTION",
        "governance":"POLICY_B_V2","role":"AUTONOMOUS_OPERATOR","retrieval":"CORPUS_B_V1","environment":"RUNTIME_B_V2"})
]

OUT = Path(__file__).with_name("scenarios.jsonl")
rows=[]
for i,(ptype,coords,changes) in enumerate(PERTURBATIONS,1):
    variant=dict(BASE)
    variant.update(changes)
    rows.append({
        "id": f"A-AI-{i:03d}",
        "purpose": "operational continuity measurement",
        "baseline": BASE,
        "variant": variant,
        "perturbation_type": ptype,
        "changed_coordinates": coords,
        "held_out": i in {4,6,9,11},
        "seed": 20260820+i
    })
with OUT.open("w",encoding="utf-8") as f:
    for row in rows:
        f.write(json.dumps(row,sort_keys=True)+"\n")
print(f"wrote {len(rows)} scenarios to {OUT}")

from pathlib import Path
import subprocess, sys

HERE=Path(__file__).parent
STEPS=[
    'generate_scenarios.py',
    'evaluate_baselines.py',
    'score_operational_identity.py'
]
for step in STEPS:
    print(f'==> {step}')
    subprocess.run([sys.executable,str(HERE/step)],check=True)
print('\nENGINEERING RUN COMPLETE')
print('No empirical or confirmatory claim is produced by this scaffold.')
print('Next gate: implement a real reproducible AI system, frozen response battery, and external/reference continuity labels or adjudication protocol.')

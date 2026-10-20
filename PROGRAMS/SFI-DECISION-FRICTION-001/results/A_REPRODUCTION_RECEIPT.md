# A · Actual local reproduction receipt (2026-10-20)

This receipt reproduces the deterministic timestamp arithmetic only. It does NOT verify OpenAI's internal logs, causal attribution, MIHM-T predictions, model superiority, independent review, or institutional RETURN.

## Reproduction

- Program directory: `PROGRAMS/SFI-DECISION-FRICTION-001/`
- Command: `python scripts/reported_intervals.py`
- Environment: Python 3, local execution, no network, no paid model API
- Git blob SHA of executed script: `4c79de5deb79ccbf43c50a78921fb03e4b56f40d` (matches GitHub branch)
- Git blob SHA of executed CSV: `ec5b63907a6a88380130bfcd0f00d7514767fdf4` (matches GitHub branch)
- Source packet: OpenAI public report updated 2026-09-25, reported clock events of 2026-09-20
- The program calculates intervals from the source-reported labels only, without inferring exposure duration or actor responsibility.

## Observed stdout

```
SOURCE_REPORTED arithmetic only. Time zone and raw logs NOT independently verified.
dns_response_received -> critical_monitor_alert: 0:11:48
critical_monitor_alert -> human_acknowledged: 0:02:55
human_acknowledged -> run_stopped: 2:29:24
acknowledged -> stopped: 2:29:24
first_observed -> stopped: 2:44:07
PASS: source-clock arithmetic. NOT a MIHM-T validation or independent event attestation.
```

## Science boundary

This reproduces arithmetic, **not** an independent event audit or a native MIHM run. The separate M0/M1 readings are descriptive and non-blinded. Current comparison conclusion: `NO_DEMONSTRATED_INCREMENT`; prospective or externally reviewed claims remain unavailable.

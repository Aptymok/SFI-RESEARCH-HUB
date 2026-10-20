#!/usr/bin/env python3
"""Reproduce arithmetic from source-reported clock readings; no causal inference."""
from __future__ import annotations
import csv
import datetime as dt
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "data" / "OPENAI_DNS_2026_REPORTED_EVENTS.csv"
EXPECTED = (
    "dns_response_received",
    "critical_monitor_alert",
    "human_acknowledged",
    "run_stopped",
)

def main() -> None:
    with PATH.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert tuple(r["event_kind"] for r in rows) == EXPECTED, "Event order changed"
    assert len({r["source_id"] for r in rows}) == 1, "Multiple sources are not one clock"
    assert len({r["incident_date"] for r in rows}) == 1, "Not a single reported day"
    times = [dt.datetime.strptime(r["reported_clock"], "%H:%M:%S") for r in rows]
    assert all(b > a for a, b in zip(times, times[1:])), "Timestamps must be ordered"
    print("SOURCE_REPORTED arithmetic only. Time zone and raw logs NOT independently verified.")
    for i in range(len(times) - 1):
        print(f"{EXPECTED[i]} -> {EXPECTED[i+1]}: {times[i+1] - times[i]}")
    print(f"acknowledged -> stopped: {times[3] - times[2]}")
    print(f"first_observed -> stopped: {times[3] - times[0]}")
    assert times[1] - times[0] == dt.timedelta(minutes=11, seconds=48)
    assert times[2] - times[1] == dt.timedelta(minutes=2, seconds=55)
    assert times[3] - times[2] == dt.timedelta(hours=2, minutes=29, seconds=24)
    print("PASS: source-clock arithmetic. NOT a MIHM-T validation or independent event attestation.")

if __name__ == "__main__":
    main()

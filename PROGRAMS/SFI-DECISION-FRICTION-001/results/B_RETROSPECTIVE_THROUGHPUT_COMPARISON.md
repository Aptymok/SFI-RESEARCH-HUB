# SFI-DF-001 B: Retrospective throughput experiment (2026-10-20)

**Classification:** exploratory engineering benchmark, no scientific validation or native MIHM-T run.
**Source:** Authorized read-only Neon `sfi_primary_mirror_applied_operations.applied_at` counts, aggregated into 15-minute intervals. Private source extract withheld from public GitHub.
**Window:** 2026-10-18 00:00 to 2026-10-20 07:45 UTC (end exclusive).
**Split:** Training 112, out-of-time holdout 79 intervals; 16 and 9 nonzero intervals respectively.
**Observed events:** 2,470 applications across 223 intervals.
**Same algorithm:** StandardScaler + Ridge(alpha=10.0), log1p(count); two feature sets; no external model cost.

| Model | Holdout MAE / 15min | Holdout RMSE / 15min |
|---|---:|---:|
| M0 conventional (recent counts + hour features) | 17.523 | 55.580 |
| M1 extra temporal lag features (PROXY, NOT MIHM-T) | 18.777 | 55.181 |
| Always zero | 17.114 | — |
| Last observed interval | 24.911 | — |

**Negative result:** M1 adds no MAE benefit over M0, and zero wins on MAE due to sparse activity. Its slightly lower RMSE does not establish superiority, and M1 contains more parameters.

**Critical limitation:** This test uses only mirror-application timestamps, not the source-write, authority, reconciliation decision, and independently attested return clocks that canonical MIHM-T would require. Therefore it is NOT a native MIHM-T test. This retrospective holdout is not a prospectively registered prediction or generalization to other organizations. No independently confirmed new science follows from this comparison.

**Reproduction:** a local private package holds aggregate event bins, a deterministic Python benchmark and machine-readable metrics. The export is not uploaded to this public repo; authorized reviewers can obtain the package from the institute's custodian.

**Next legitimate gate:** frozen per-case operational source packet including source-write / applied / ack / decision clocks; native MIHM admissibility assessment; independent reviewer and comparison to competent M0 under the same information and resource budget.

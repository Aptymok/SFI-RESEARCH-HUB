# B — SFI continuity: bounded operational friction study (exploratory)

**Date:** 2026-10-20 UTC
**Classification:** RESEARCH_DERIVED / EXPLORATORY / NO_INDEPENDENT_VALIDATION
**External publication status:** This file lives only on the **draft research branch**. It is not a Research Hub release, accepted scientific study, certification, or a public disclosure of private raw operational evidence.
**Method parent:** existing MIHM; MIHM-T is *experimental* and no native MIHM-T research run was executed.
**Privacy:** aggregate status data and publicly viewable code architecture only. Internal identifiers, credentials, row payloads and per-actor operational logs are excluded.

## Scientific question

Can a bounded MIHM representation of asynchronous source writes, mirror application, acknowledgement, authority and certification detect a decision-relevant dependency that a competent, equally informed distributed-systems/process M0 fails to recover?

The chosen system is SFI's own Supabase PRIMARY -> Neon continuity. This is an important **self-study conflict**, not independent external validation.

## Evidence boundary

Observations come from direct read-only sources: SFI_ROOT `data_plane_status`, aggregated SQL reads of Supabase and Neon, and a reviewed code snapshot on `Aptymok/system-friction` `main`. Reads occurred at different instants between 07:39 and 07:50 UTC. These are **non-atomic snapshots**; row-count differences cannot certify corruption, losses or row-level mismatch.

An internal detailed ledger and arithmetic verification receipt were preserved outside this public repository. Institution-only Method Lab derived evidence receipt: event `94057a3b-7bce-4889-94bb-d38f862773da`, status `derived`, **not promoted**.

## Real observations, separated from conclusions

1. SFI_ROOT reported operating mode `PRIMARY`; live mirror certification remained `false`, with source outbox pending and zero reported conflicts.
2. Primary outstanding work in two ROOT observations **decreased from 2,530 to 1,922**, net -608 over roughly five minutes. This establishes progress during the window, not that all writes matched.
3. Aggregate source creation showed a concentrated burst of **458 subsequently-pending entries over two successive minutes**. Source production and mirror acknowledgements can overlap; the figures are **not a single causal batch**.
4. Source outbox analysis showed pending entries were individual source transactions in the inspected cut. This is a *local grain finding*, not a guarantee for every future transaction.
5. The current code that projects scheduling information from ROOT hardcodes a different time list than the actual checked-in GitHub Actions workflow. This is **a stale declared metadata inconsistency**, not proof of which runs GitHub successfully delivered.
6. Mirror-applied entries and `CLAIMED` transition states were observed, so describing every pending row as failed or never processed would be inaccurate.
7. The source and continuity databases had different counts in several research tables, and separate keyset fingerprints did not match. Because the observations were independent and made during active writes, these are **diagnostic observations**, not an integrity certificate or exact divergence set.

## M0 — strong conventional baseline

A distributed-systems analysis uses an outbox producer/consumer model, transaction-level idempotency, FIFO processing where confirmed by implementation, batch caps, workflow delivery receipts, replication apply/ack states and conditional certification. It correctly distinguishes:
- a new write from a pending request;
- a queued request from an attempted failed request;
- a declared cron schedule from a run receipt;
- mirror activity from certified parity;
- arithmetic row count from equal sets of canonical records.

M0 already predicts that bursts can increase outstanding work even while the replicator is actively processing older transactions. It also detects stale metadata by comparing implementation and projected operational status. This does not establish the unique cause of every delay; the actual workflow receipts, per-run throughput and common-cutoff matching sets remain unavailable.

## M1 — MIHM representation of the same evidence

**Boundary:** approved SFI PRIMARY source, source outbox, authorized reconciler, Neon continuation plane, SFI_ROOT read model and scientific evaluator.

**Nodes:** N1 source writer, N2 outbox ledger, N3 authorized reconcile scheduler, N4 mirror applier, N5 acknowledgement path, N6 independent live certificate projection, N7 institutional decision layer.

**Constraints:** a single authoritative source mode; no conflict deletion; no unilateral authority promotion; no certificate while live pending exists; observation versus action is explicit; independent reads are not atomic.

**Operational clocks (distinct):** source `created_at`, claim/attempt, apply in Neon, acknowledgement `mirrored_at`, system status read, last certificate verification time, declared cron and actual cron receipt. M1 distinguishes these clocks and refuses to infer an execution that has no receipt.

**Temporal hypothesis:** a source burst arriving while the mirror is draining may create temporarily increasing backlog, and an outdated read model may mischaracterize the scheduling conditions of recovery. These are hypotheses compatible with the operational observations, **not** a validated directional MIHM-T transfer law or a causal attribution to a named person.

## Comparison verdict

| Audit dimension | M0 conventional | M1 MIHM | Demonstrated incremental value |
|---|---|---|---|
| Source/mirror backlog and concurrent writes | Captured | Captured | **None** |
| Queued vs attempted vs replicated | Captured | Captured | **None** |
| Schedule metadata vs executed cron receipts | Captured | Captured | **None** |
| Source/event/knowledge/certification clocks | Can represent | Explicitly typed | **Not yet measured** |
| Mirror parity conditions | Captured | Captured | **None** |
| Forecast or intervention effect | Not tested | Not tested | **Not measured** |

**Verdict:** `NO_DEMONSTRATED_INCREMENT` for the observed and reviewed evidence. The MIHM description is structured and epistemically conservative, but no verified M1-only decision-relevant finding is established. This is a substantive negative/limited pilot result, not refutation of every MIHM hypothesis.

## Observability and production next gates

- **Engineering issue:** Update ROOT's displayed schedule to agree with the canonical workflow or derive the schedule from one verified source; add a regression test, without another scheduler.
- **Source receipts:** Inspect actual recent GitHub Actions run results and mirror receipts within a prespecified window. No cron run can be inferred merely from YAML.
- **Fingerprint equality:** On an approved consistent cut, compare keys and canonical row digests; do not claim parity from counts alone.
- **Scientific method:** Before another comparison, fix M0/M1 source packet, comparison metric, equal budget and independent evaluator. Test a real held-out event or external system only after permissions and evidence are available.
- **Institutional ethics:** Author of SFI methods cannot independently validate its own system; seek an external reviewer.

**No material system intervention, data-plane failover, new case admission, independent external RETURN, canonical research promotion, publication release or DOI took place.**

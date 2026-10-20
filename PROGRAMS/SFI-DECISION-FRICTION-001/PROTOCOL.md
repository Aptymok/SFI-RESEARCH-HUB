# SFI-DF-001 — Scientific protocol (draft, unregistered)

**Version:** 0.1.0-draft / 2026-10-20
**Research question:** Does MIHM/MIHM-T source- and time-governed reconstruction of an incident reveal valid, decision-relevant constraints and dependencies beyond a competent conventional baseline, with comparable source access and cost?

## Method registration boundary

THIS DOCUMENT IS A DRAFT. It is not preregistered, scientifically accepted, independently reviewed or executed. Any change made after scoring must be marked post hoc; freeze a commit plus source package before each actual comparative trial.

### 1. Units and boundaries

The unit is one bounded sociotechnical incident or documented intervention. Each unit records: legal/technical boundary, actors or roles (never invented names), state transitions, constraints, permissions, event time, evidence availability time, recording time, actual actor knowledge if proven, operations, outputs, external consequences and missingness.

The three proposed cases are three separate studies, not exchangeable observations:
- A: public documentary OpenAI incident of 2026-09-20.
- B: a specific SFI continuity event chosen from canonical logs through recorded authorization; NOT THE GENERAL PRODUCT STATUS.
- C: one externally offered case, after independent intake and consent.

### 2. Competing scientific statements

- **H1 (incremental representation):** On a source-matched bounded incident, M1 (MIHM + eligible MIHM-T) identifies at least one independently substantiated, materially decision-relevant cross-boundary dependency not recovered by a competent M0, without more unsupported claims.
- **H0 / rival:** An equally competent chronological incident report, root-cause/process/safety analysis, process mining or event-graph model (chosen for the case in advance) is sufficient, or M1 adds complexity without useful increment.
- **Alternative explanation:** Any benefit is due to more context, longer analyst time, source leakage, prompts, evaluator preference, terminology, model quality or post-hoc knowledge, rather than method structure.

A negative finding is not proof that all MIHM research is false. It limits the declared claim and conditions.

### 3. M0 and M1

**M0 conventional baseline:** Analyze the same source packet with a conventional incident-response timeline plus event/causal graph or competent process/safety framework; log assumptions, unknowns, alerts, authority, interventions, consequences and cost. M0 must be strong, not a straw man, and may use expert human/LLM assistance of matched budget.

**M1 SFI:** Use the existing MIHM bounded system/node/relation/constraint/perturbation representation. Apply MIHM-T only if parent system, source/target dimensions, time clocks, lag hypothesis and source lineage pass existing admissibility gates. Explicitly separate event time, public source time and actual knowledge time. Reconstruction backward from an observed consequence is RETROLONGITUDINAL, never prospective prediction.

Neither M0 nor M1 may use information beyond its frozen as-of packet; both may declare UNKNOWN, missing records and abstention. No global friction number or common Phi is added. **Model control:** within a paired LLM-assisted comparison, both arms MUST use the same provider/model/snapshot and the same information and computational budget; independent Claude/Gemini models are separate challenge/replication strata, not one M0 arm against a GPT M1 arm.

### 4. Initial observable dimensions

- Detection-to-acknowledgement interval: difference between source-reported timestamps (not proof of causal mechanism).
- Acknowledgement-to-material-containment interval: difference between externally reported events; define materially verified containment as the reported stop/receipt, not a status flag alone.
- Evidence provenance completeness: share of tested factual assertions linked to an exact source/version, with denominator enumerated.
- Unsupported-assertion count: unsupported or contradicted claims found by an independent adjudicator.
- Dependency recall/precision: adjudicator-scored supported material edges out of prespecified documentary reference edges; report unknown or undecidable edges separately.
- Incremental decision value: enumerated M1-only supported findings that would change a predeclared operational decision under an adjudicator's criteria.
- Additional effort and cost: elapsed analyst minutes, tokens and provider charges if models run, review effort and computation.

No single composite score. Report each dimension separately.

### 5. Primary decision rule for first comparative calibration

Before comparing outputs, appoint a human independent of model generation to approve source packet, comparator choice, labeling rubric and a list of what constitutes a material decision-relevant dependency. Blind the adjudicator to which analysis is M0 vs M1 where feasible.

A meaningful **candidate incremental** result requires ALL:
1. At least one M1-only material dependency accepted by the adjudicator from the equal source packet.
2. M1's unsupported/contradicted factual assertions do not exceed M0's.
3. The finding survives an equal-time / equal-token comparison and adjudicated effort-cost report.
4. The finding is reproducible by an analyst not involved in creating the original M1 output.

If any requirement fails, classify NO_DEMONSTRATED_INCREMENT for that trial. Meeting them on one historical case is a **pilot**, not scientific validation of generalization. Even successful A or B is not an external generalization result.

Do not tune threshold or change the rival baseline once outputs are visible. Changes after this point require a new version and labels POST_HOC.

### 6. Falsification and external validity

Refute the bounded incremental-benefit claim for a comparison if M0 captures the same justified dependencies or M1's purported gain depends on extra information, hindsight or unsupported speculation. Explicitly log untestable and inconclusive findings.

A possible subsequent transfer study requires independently acquired external cases, frozen outcome targets where prediction is claimed, blinded held-out evaluation, independent adjudication, appropriate number of cases determined before recruitment, and honest confidence intervals. No claim of universal system theory is permissible from A/B/C.

### 7. Case A provenance / reported-event fixture

Primary report: https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/

Report event date 2026-09-20; public report last updated 2026-09-25. Four reported same-day clock readings:
- 09:50:23, agent DNS action received a response.
- 10:02:11, monitoring emitted a critical P0 alert.
- 10:05:06, human reviewer acknowledged.
- 12:34:30, run killed.

The public report as opened here does not establish an independently audited time-zone conversion; retain these as report-local clock labels. These marks do not show that the actor had actual knowledge before acknowledgement. Report-derived intervals are not independent discoveries by SFI.

Source packet includes only the explicit report, acquisition/revision metadata when available, and a versioned record of fact selection. No private traces, no claims of reading unseen logs, no attempted reconstruction of unauthorized network operations.

### 8. Case B provenance / operational safety

Choose one bounded, already observed and documented continuity episode of SFI; record exact source tables, IDs, authority and timestamps privately. Do not export credentials or user data to public repos or third-party AI. Separate Supabase PRIMARY from Neon continuity and verify parity as-of any comparison. If replication is uncertified, label it and never assert mirrored equivalence.

Because SFI researches itself, external scientific review is mandatory before a broad institutional claim. Access to ROOT does not constitute authorization to perform material interventions.

### 9. Case C recruitment and rights

Receive only minimal non-sensitive summaries through a tested official intake. Request private evidence through a controlled channel only after review of legal basis, consent, privacy and retention. No automatic case creation, public publication, external outreach or intervention based solely on form submission.

### 10. AI/evaluator boundaries

AI systems may extract, classify, propose rival hypotheses, generate M0/M1 drafts or adversarially challenge assertions. They do not certify facts, backdate observations, authenticate humans, create external RETURN or approve institutional publishing. Log model/provider/version, prompt hash, packet hash, parameters, tokens/cost, run time, redactions and citations. Disagreement is an output; consensus is not ground truth.

### 11. Preservation and publication

Canonical raw receipts stay with their lawful custodians; sanitized index, source-vintage matrix, definitions, code, rubric, blinded comparisons, negative cases and exact freeze commit go in the Research Hub once authorized. Any DOI/Zenodo release is a later explicit scientific publication decision.

**Status: draft, not preregistered. One non-blinded SAME-SESSION exploratory documentary M0/M1 reading is recorded separately; no logged API-model experiment, Case Platform admission, external intake, or independent human adjudication. Criteria have not been prospectively tested.**

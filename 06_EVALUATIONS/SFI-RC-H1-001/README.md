# SFI-RC-H1-001 — Documentary vintage stress test

**Parent:** [Reality Chain working paper](../../05_RESEARCH_OBJECTS/SFI-RC-2026-METHOD-001/PUBLICATION_RECORD.md) · **Evaluation type:** deterministic retrospective self-test, **not** an independent H1 experiment.

## Narrow research question
Does the temporal eligibility rule prohibit retroactive use of 2013 SEC information when reconstructing what the **selected public documents** supported on 2 August 2012?

Sources: issuer [August 2, 2012 filing](https://www.sec.gov/Archives/edgar/data/1060749/000119312512332176/d391111dex991.htm); [SEC administrative order 34-70694 (16 October 2013)](https://www.sec.gov/files/litigation/admin/2013/34-70694.pdf); [SEC 2013-222 announcement](https://www.sec.gov/newsroom/press-releases/2013-222). See `claim_registry.json` for individual source locators, assertion status and event/publication distinction.

## Executed check
`node evaluate.mjs` validates unique source and claim IDs, source URLs, locators, epistemic labels and two time cuts, then derives `results.json`.

| Knowledge cut | Eligible by selected cited sources | Withheld for later source publication | Date-blind negative control |
| --- | ---: | ---: | ---: |
| 2012-08-02 | 3 | 4 | 7 included |
| 2013-10-16 | 7 | 0 | 7 included |

**Observed/documented:** issuer disclosed software-related erroneous orders and a preliminary approximately $440 million realized pre-tax loss by 2 August 2012. **Later regulatory knowledge:** SEC findings about eight servers, 212 parent orders, 97 emails and the specific rule violation appeared in public 2013 sources. This test does not claim that no other 2012 source contained any given detail.

**Derived:** an explicit source-vintage cutoff withheld 4/7 later-source claims at T0. The date-blind control is designed to fail by ignoring source publication date. This is validation of a deterministic rule, **not evidence that SFI outperforms a serious conventional provenance or archival method**.

## Next genuinely comparative H1 study

The separately recorded [independent trial protocol](INDEPENDENT_TRIAL_PROTOCOL.md) preserves a fair baseline, held-out incidents and a requirement for independent evaluators. It is a protocol candidate, not evidence of recruitment or execution.

Pre-register matched packets and time budgets for (A) standard provenance/version-control workflow and (B) typed Reality Chain. Recruit independent raters; blind scoring; allow abstention; assess correct reconstructions, temporal leakage, unsupported causal claims, inter-rater agreement, labor cost and sensitivity to source volume. Hold out sources and retain negative cases. Define superiority before observing outcomes. No such trial has been performed here.

## Status / permissions
- Study state: `DERIVED_SELF_TEST`; H1 `NOT_TESTED`; independent RETURN `NOT_OBSERVED`.
- Source excerpts are not re-licensed; SFI's annotations and code may be reused under CC BY 4.0 with attribution.
- No private operational or market participant data, no invented metric, no DOI.

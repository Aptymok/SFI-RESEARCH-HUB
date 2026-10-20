# SFI-DF-001 — AI participation and independence controls

**Status: PROPOSED, not deployed.**

Use no more than three complementary model families for the initial documentary pilot. The provider mix is for disagreement detection, not authority or voting.

## Recommended division

1. **SFI Cognitive Runtime / OpenAI GPT-6 family:** pipeline coordinator under existing SFI permissions. Build a source-indexed event extraction and M1 representation. If paid API operation is needed, quote and approve its bounded cost separately; a conversation in ChatGPT does not prove a runtime job was executed.
2. **Anthropic Claude Opus 5.5 or Sonnet 5.5:** strong independent *rival* M0 analysis or adversarial source audit on the same frozen public packet, if API access is actually configured. No privileged access to SFI.
3. **Google Gemini 4 Argon / 3.8 Flash:** independent document and contradiction reading of the same redacted public packet; Google Search grounding is a separate retrieval operation whose citations must be rechecked. Argon is a paid model, not a free dependency.

Provider/model availability and prices change. Model names are examples as of October 2026, not statements that SFI already has contracts, credentials or invocation logs. A local open-weight model is an optional privacy/cost comparator after repeatability benchmarks, not a mandatory fourth agent.

## Independence protocol

- Humans set the research question, admissible material facts, source packet and decision rules before runs.
- M0 and M1 receive information-volume-matched, as-of-frozen document packets.
- Analysts/model processes should be independent where feasible; have a neutral operator assign anonymized A/B output labels.
- Do not feed the other model's answer as an input before scoring; afterward use counterarguments as a separately logged challenge.
- Preserve structured disagreements and evidence gaps; models cannot vote an unsupported assertion into truth.
- Reviewer with no authorship/conflict in the methods adjudicates contested edges and additional utility.
- Human scientific officer decides whether to admit, release or reject a result under actual authority.

## Reproducibility log per invocation

Record: packet_sha256; prompt_sha256; canonical method version; provider; model id and revision; run timestamp; scope; source list; redaction status; cost/tokens; exact structured response reference; validator and review disposition.

## Data and cost gates

No secrets, identifiable interview material, private SFI service data, personal relationships, raw case files or third-party restricted evidence to model APIs absent lawful authorization and security review. Do not automatically invoke multiple paid frontier models just to make a result look more robust. Begin with public incident documents and a deterministic script; use two model providers only if they offer distinct testable analytical contributions.

These steps are not a certification scheme and do not authorize material autonomous action.

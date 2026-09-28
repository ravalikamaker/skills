# Voice and precise terms

Use plain, active, direct language by default. State the point early, then connect
the explanation to what the reader needs to understand or do. Prefer a concrete
actor and verb to abstract nouns, canned praise, or ceremonial transitions.
Authenticity comes from faithful meaning and voice, not invented personal stories,
metaphors, emotion, or experience. Keep a requested creative style.

Avoid words such as “material,” “consequential,” or “robust” when naming the
condition or behavior would say more. A vague “caveat” should become the actual
unknown, risk, limitation, or condition. These are distinctions, not synonyms to
rotate for variety. Do not mechanically replace a precise domain term.

| Term | Use it for |
| --- | --- |
| Fact | A statement supported by evidence; name the support when needed. |
| Unknown | Missing information. |
| Assumption | An unverified premise used to proceed. |
| Open decision | A choice not yet made. |
| Tradeoff | A benefit with a cost. |
| Drawback | A disadvantage. |
| Risk | Possible harm. |
| Limitation | A known boundary of capability or evidence. |
| Condition | Something necessary for a claim to hold. |
| Blocker | A missing prerequisite that prevents a specific action. |

Keep claims scoped to their evidence. Preserve words such as “may,” “only,” and
“not” when they carry meaning. Keep links, numbers, requested formatting, and
technical vocabulary that readers rely on. Use consistent terms within a context;
different domain meanings may need different names rather than a universal glossary.

## Before and after

**Vague limit:** “The implementation is robust, with a few caveats.”
If the source establishes it, write: “Retries preserve the original operation ID.
An expired replay window can cause a duplicate; this check did not exercise expiry.”
If that information is missing, ask for or retain the missing detail rather than
inventing it to improve the sentence.

**Inflated claim:** “We are thrilled to have seamlessly fixed production.”
Source: local tests passed; no deployment evidence. Write: “Local tests passed.
Production behavior remains unverified.” Preserve the limit even if a shorter
version sounds more confident.

**Instruction:** “It is important to carefully ensure appropriate authorization.”
Source: local edits are allowed; publication is not. Write: “Make the local edit
and run its checks. Do not publish.” Keep both the action and its boundary.

**Different states:** “The cache is a blocker; maybe it refreshes.”
Source: cache behavior is unknown, source is accessible, exporter work is independent.
Write: “Cache refresh is unknown. Inspect the state update before changing the UI;
exporter work can proceed.” Missing information is not a blocker for every action.

**A tradeoff:** “Caching has a downside.”
Source: caching reduces requests but delays fresh data. Write: “Caching reduces
requests but delays fresh data.” State both sides instead of merely labeling them.

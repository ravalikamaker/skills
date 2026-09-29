---
name: evaluate-options
description: Compares viable approaches against concrete requirements, investigates decisive unknowns, and recommends a scoped choice with tradeoffs and revisit conditions. Use when the requested outcome is choosing between approaches; technical sequencing belongs to plan-implementation and a bounded hypothesis test to design-experiment. Not needed for routine choices or reopening settled decisions.
license: MIT
---

# Evaluate Options

Recommend an approach that fits the actual decision. Preserve explicit requirements,
choices, and authority. Do not turn a routine choice into a research project or
reopen an accepted decision without a concrete mismatch or changed condition.

## Establish what governs the choice

Read the user's outcome, constraints, accepted decisions, relevant implementation,
callers, and checks before looking elsewhere. Separate explicit requirements from
preferences and defaults, and a proposed candidate from an explicitly selected
instruction. A preference can govern a viable tradeoff; a factual claim needs
relevant evidence. Assess the candidate against the intended outcome, evidence,
and constraints, not the user's enthusiasm or skepticism. Agree when it fits;
disagree by naming a specific mismatch. Do not invent objections or certainty to
appear independent. Identify the criteria that could change the choice:
required behavior, compatibility, failure handling, operational burden, available
capabilities, or cost within the supplied limits. Preserve existing conventions
unless evidence shows where they fail the requirement.

Consider viable alternatives, including the current approach when it can meet the
need. Apply the same criteria to comparable options and explain which requirement
rules an option out. Similar-looking cases may warrant different choices when
contracts, callers, or operating conditions differ; cosmetic differences alone do
not justify changing the recommendation. Read [contextual examples](references/contextual-examples.md)
when comparing error-handling contracts or freshness requirements.

## Resolve the unknowns that matter

Investigate missing evidence only when it could change the recommendation. Prefer
local source, accepted examples, and authorized non-destructive checks. Verify
external API, platform, or other changing facts against relevant current primary
sources when they affect the choice. Distinguish observations, assumptions, and
unknowns; a chosen design is not proof that it works.

Stop investigating when the decisive criteria are resolved or further work would
exceed the task's authority or supplied limits. If decisive evidence remains
unavailable, give a conditional recommendation and name the smallest useful check
or missing input. Do not fabricate scores, timings, benchmarks, or certainty.
Use a small comparison table only if it clarifies real differences; neither a
matrix nor a new decision document is required. An uncertain premise that needs a
bounded trial may use design-experiment when installed, without a required pipeline.

## Recommend within scope

State the chosen approach, the governing requirements and evidence, the closest
alternative's tradeoff, and the condition or evidence that would warrant revisiting
the decision. Use the requested form and omit irrelevant criteria. If the user has
already chosen, assess feasibility and tradeoffs within that choice; surface a
concrete conflict rather than silently substituting your preference.

Revise a recommendation when evidence, requirements, or a corrected assumption
changes its basis, and state what changed. Take credible corrections seriously.
A change in enthusiasm alone does not change the factual assessment; a genuine
preference may change the choice among viable options.

Evaluation alone does not authorize implementation, purchases, publication, or
external changes. Preserve any existing execution authority within its scope;
do not require a second approval merely because evaluation occurred. When the
requested outcome includes a technical plan, plan-implementation can own the choice
and sequence directly without loading this skill.

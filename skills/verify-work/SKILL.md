---
name: verify-work
description: Checks completed work before acceptance or when a completion claim needs verification. Compares the requested outcome and artifact correctness with independent evidence, and reports defects, missing checks, and limits without making unapproved repairs.
license: MIT
---

# Verify Work

Check both whether the result meets the user's request and whether the artifact
works correctly. A passing format check alone does not prove behavioral correctness.

## Establish completion criteria

Read the requested outcome, constraints, non-goals, and completion criteria from
the task. Identify the artifact or version being checked and the evidence already
available. Include relevant business rules and domain constraints from the
requirements or existing decisions; passing code checks cannot override them.
For agreed architecture constraints, identify the affected boundary and use
existing project tools or focused inspection to check it. Distinguish a stated
constraint from enforced behavior; do not invent governance or an architecture
requirement for a task that has none. Resolve only ambiguity that changes the
acceptance decision.

Stay within the task's authorized actions. Leave the deliverable unchanged unless
fixes are authorized. Use non-destructive checks and permitted
temporary outputs; a check that would mutate external state needs its own existing
authority. Findings do not authorize edits, publication, or broader investigation.

## Check outcome and correctness

Compare the result with the user's intended use, not just a worker's interpretation
or checklist. Account for each required outcome and any deliberate omission.
Check the claimed benefit to the intended beneficiary and relevant side effects
in proportion to the claim. A technically correct artifact can still miss its
purpose; distinguish observed benefit from a prediction or unmeasured outcome.
Inspect the actual artifact and relevant interfaces, inputs, or source evidence.
Look beyond reported paths or summaries when establishing what changed.

Run accessible shell, browser, simulator, or artifact checks yourself or through
bounded native delegation within existing authority. Inspect the relevant current
tools and access before claiming a check is unavailable. Do not reflexively assign
QA to the user; request a narrowly defined contribution only when a concrete
capability, access, input, or authority gap prevents required proof, and continue
independent checks while waiting. Resume the blocked check when the gap is filled.

Choose the smallest decisive checks for the completion criteria and consequences.
Derive expected results from accepted requirements, examples, or independent
source evidence, not the implementation or producer's assertion. Run applicable
required gates; local success does not replace a required CI gate. Own accessible
execution and result inspection within authority, and name specific access or
trigger-authority gaps rather than assigning all QA to the user.

Check representative behavior, relevant rejection or recovery, and consequential
side effects. For a refactor, compare affected observable behavior with the prior
version and agreed rules. For documents or analyses, check calculations, source
support, consistency, and usability. Check interactions among combined changes.
For a development-workflow claim, exercise the affected navigation, setup, run,
change, or verification journey as relevant. A script's existence or a successful
run in a warm checkout does not prove usable commands or fresh-environment setup;
identify the environment and steps actually exercised.
Inspect affected docs, examples, and comments against accepted intent: preserve
valid promises and useful invariant comments, and flag stale or unnecessary
additions. Read [acceptance examples](references/acceptance-examples.md) when a
docs/code mismatch or independent acceptance pass matters.

Preserve test integrity: do not weaken assertions, skip failures, or substitute an
always-successful boundary to accept the artifact. Distinguish observed execution
from proposed checks and simulated boundaries from real ones. Inspect the actual
result, including persistence or generated contents when promised; a success banner
is not sufficient evidence. If missing coverage requires test authoring, test-change
can help when installed. This skill remains sufficient to choose and execute
acceptance checks without that companion.

For an HTTP contract, application security, accessibility, or secure-development
process review, consult [standards guidance](references/standards.md) only for the
relevant concern. Do not add a compliance workflow to an unrelated task.

Use evidence independent of the producer's success assertion. This can be direct
inspection or a fresh execution; it does not automatically require another agent.
For consequential integrated work, an independent acceptance pass may benefit
from the requirements and runnable artifact before the implementation details;
read [acceptance examples](references/acceptance-examples.md#independent-acceptance)
when that separation would test a plausible shared assumption. This is optional,
not a default extra reviewer or a restriction on debugging access.
If independent review is required, use an available reviewer with a bounded brief
and raw artifacts. Do not supply the desired verdict. Reuse an adequate completed
review instead of stacking reviewers over the same unchanged work.

Retain passing evidence while its artifact version and assumptions remain valid.
Invalidate affected evidence when requirements, dependencies, configuration, or
boundary conditions change, even if the checked source files are unchanged.
Rerun affected checks after corrections; broaden only when a failure, new change,
or unresolved concern justifies it. Do not repeat successful checks for ceremony.

## Resolve findings

For each gap that prevents completion or affects correctness, name the affected
requirement or artifact, evidence, and consequence. Distinguish a defect from
uncertainty or a missing check. Return repairs to the existing owner within
authorized scope.
When working alone with repair authority, make the scoped correction and verify
it; otherwise report the gap without changing the deliverable.

Stop adding checks when the evidence covers the completion criteria. If a needed
check cannot run, name the missing capability or input and what remains unverified.
Neither unavailable tooling nor a plausible explanation counts as a passing check.

## Report acceptance

Report whether the completion criteria were met, the checks and their results,
findings, and remaining limits. Name the artifact/version when needed. Separate
local validation, installation or loading, observed runtime behavior, and any
verified remote delivery. Identify which consequential boundaries were exercised
for real, simulated or substituted, or left untested; a mocked provider check
does not establish provider behavior. Use the existing completion response or
artifact; do not require a separate report. Partial evidence supports only a
partial claim; do not describe the mission as complete while a required outcome
remains unresolved.

## Worked example

Synthetic inputs: the requirement is to reject an expired invitation without
creating an account. For artifact R2, the schema check passed, but a direct test
with an expired invitation created account A9. No edits are authorized.

Result: requirement failed; the schema pass establishes only the checked shape.
The observed account creation violates the requested rejection behavior. Report
that evidence and return the repair to its owner without editing. A valid schema
or a producer's “done” cannot turn the observed failure into acceptance.

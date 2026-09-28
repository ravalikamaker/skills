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

Choose the smallest decisive checks for the consequences and uncertainty involved.
Inspect existing coverage before adding tests: name a plausible defect it would
miss and choose a check that would detect it. Choose real journey checks for
connected behavior and focused integration or unit checks where they expose the
relevant defect;
there is no test-count quota or universal E2E-only requirement. Derive expected
results from requirements, accepted examples, or an independent reference, not
from the implementation being checked:

- Exercise representative behavior and relevant failure cases for a changed system.
  Follow the relevant user journey to its promised result, including recovery or
  rejection when consequential; isolated screens or endpoints may be insufficient.
  Check waiting, empty, denied, error, cancellation, or recovery states only when
  relevant to the promised journey. A success-only demo may conceal an unusable
  boundary; a universal state checklist can also add irrelevant work.
- For a behavior-preserving refactor, compare observable behavior with the prior
  version for the affected inputs and interfaces. Flag intentional changes that
  need an explicit requirement rather than accepting them as cleanup.
- Inspect calculations, source support, internal consistency, and usability for
  documents, analyses, or other deliverables.
- Check affected docs, examples, and comments for drift from accepted intent and
  the changed behavior, including generated sources when relevant. Check whether
  added documentation was requested or useful; routine completion alone does not
  justify new files. Preserve valid promises when code is defective. Keep comments
  that explain non-obvious invariants, rationale, or public contracts; flag redundant
  line-by-line narration within scope. Read the [documentation example](references/testing-examples.md#documentation-can-expose-a-code-defect)
  when checking a docs/code mismatch or unnecessary additions.
- Check interactions between combined contributions, not only isolated parts.
- Run applicable required checks; identify what they establish and what they omit.
  Local success does not replace an independently required CI gate. When a check
  can run only in CI, own triggering, result inspection, and scoped repairs within
  existing authority rather than handing it to the user. Without needed access or trigger
  authority, report that specific gap and keep the gate unresolved.

Preserve test integrity: do not weaken assertions, skip failing checks, or mock a
real boundary merely to get a pass. Correct a stale test only against an accepted
requirement, explaining why its old expectation is no longer valid. For bug fixes,
reproduce failure before the correction and success afterward where practical;
if the earlier failure was not observed, say so rather than inventing proof.
Target checks at plausible misleading success: vary fixture data, refresh or reopen
the result, inspect generated output, and check persistence when it is promised.
Use only the checks relevant to the claim. Read the relevant section of
[testing examples](references/testing-examples.md) when selecting coverage,
checking apparent success, or interpreting substituted boundaries.

For an HTTP contract, application security, accessibility, or secure-development
process review, consult [standards guidance](references/standards.md) only for the
relevant concern. Do not add a compliance workflow to an unrelated task.

Use evidence independent of the producer's success assertion. This can be direct
inspection or a fresh execution; it does not automatically require another agent.
For consequential integrated work, an independent acceptance pass may benefit
from the requirements and runnable artifact before the implementation details;
read [testing examples](references/testing-examples.md#independent-acceptance)
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

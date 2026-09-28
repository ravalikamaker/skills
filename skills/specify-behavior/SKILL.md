---
name: specify-behavior
description: Makes intended behavior concrete with representative success, rejection, and boundary examples and observable outcomes before or during implementation. Exposes unresolved decisions without inventing rules; does not verify a completed artifact or require a test framework.
license: MIT
---

# Specify Behavior

Make the expected result clear enough for implementation and acceptance without
prescribing internals. Use this when requirements contain ambiguous outcomes,
important boundaries, or shared interface behavior that examples can clarify.
An agreed literal edit or a general explanation does not need a specification.

## Find the rule and observable result

Read the requested outcome, affected actors, domain rules, relevant decisions,
and existing examples. Preserve explicit constraints. Define the behavior in
terms of what the user or consumer can observe, including returned results,
state changes, errors, and consequential side effects. Include relevant user-facing
waiting, empty, denied, error, cancelled, or recovery states when they affect the
promised journey; do not apply a universal state checklist to unrelated behavior.

Separate supplied rules, inferred possibilities, and unresolved decisions.
When a missing rule changes the outcome, show the smallest contrasting examples
that expose the choice. Do not select a pricing, eligibility, authorization,
or timing policy merely to make the examples complete.

## Choose representative examples

Cover the important normal outcome, rejection or failure, and boundary when
relevant. Use concrete starting conditions, an action or input, and the expected
observable result. Include timing, ownership, retry, or state-transition details
only when they change behavior. For side-effecting operations, distinguish
confirmed failure from running work and an unknown result. Specify whether recovery uses status
inspection or reconciliation, or explicitly supported safe replay of the same
operation. Preserve the supported idempotency conditions and a bounded stop or
escalation condition; guaranteed safe replay need not require an extra status call. Mark missing semantics unresolved;
do not invent a blanket retry policy. Choose cases that distinguish plausible wrong
implementations rather than multiplying cosmetic variants.

For a shared interface, clarify inputs, outputs, and error behavior at the
consumer boundary. Leave storage layout, component structure, and internal
function names open unless they are part of the agreed contract.

Use prose, a table, or executable examples when the project benefits from them.
Do not require Gherkin, a particular tool, exhaustive tests, or automated checks
for every example. Mark candidate criteria and unresolved outcomes explicitly.

For unresolved concurrency or retry boundaries, read
[behavior examples](references/behavior-examples.md) to see observable outcomes
and open rules kept separate.

## Return an actionable specification

Keep the rule, representative examples, unresolved decisions, and acceptance
observations close together. Tie expected results to the supplied requirement,
accepted decision, or independent reference; do not copy current implementation
outputs into the expected result. For proposed tests, inspect existing coverage and name
the plausible wrong behavior each added case distinguishes. Choose the boundary
that can expose it: a real journey for connected behavior, or focused integration
or unit checks for a rule. These are candidates, not a quota or execution proof.
Read back the examples against the user's outcome
and constraints; inconsistencies are decisions to resolve, not details to hide.
A specification describes intended behavior. It does not show that an artifact
has passed, and writing it does not authorize implementation or external actions.
Save an artifact only when the destination and write are authorized.

## Worked example

For “allow cancellation until payment,” show an unpaid request that cancels and
a paid request that rejects cancellation without changing its state. If payment
and cancellation arrive together and no ordering rule exists, mark that boundary
unresolved. Do not invent a concurrency policy or make a database design part
of the acceptance criteria.

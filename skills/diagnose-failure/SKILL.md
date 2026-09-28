---
name: diagnose-failure
description: Investigates a failure or unexplained symptom using observations, competing hypotheses, discriminating checks, and recorded negative attempts. Narrows cause and uncertainty before repair; distinct from accepting completed work or planning recurrence prevention.
license: MIT
---

# Diagnose Failure

Find the narrowest supported explanation and the next useful action. Use this
for a broken operation, unexpected result, or intermittent symptom whose cause
is unsettled. A general explanation, acceptance review, or prevention proposal
for an established recurring failure needs a different workflow.

## Establish the observed failure

Read the symptom, expected behavior, relevant version and environment, and
available evidence within permitted access. Distinguish what was directly
observed from reports, interpretations, and missing state. Bound the affected
operation and user consequence; do not investigate the whole system by default.

Preserve urgent containment within existing authority. Diagnosis does not grant
permission to repair, restart services, change accounts, or mutate external
state. If a fix is already authorized, carry the supported correction through
and check its result; do not stop at a diagnosis merely because this skill is
active. Preserve evidence needed to explain what changed.

Where practical, turn the exact symptom into an executable check with its input,
expected result, and relevant environment. Reduce the reproduction while keeping
the failure it needs to expose; retain the original scenario for repair verification.
Do useful inspection and hypothesis testing while reproduction is incomplete;
label what has not been reproduced rather than waiting for a perfect fixture.
Read [reproduction examples](references/recovery-examples.md#reproduce-the-reported-symptom)
when a smaller check could lose the reported failure.

## Test competing explanations

Use relevant logs, inputs, changes, and known-good comparisons to form a small
set of plausible hypotheses. State what would support or weaken each. Prefer
checks that distinguish explanations over checks likely to repeat the symptom
without learning anything. Change one relevant condition at a time when that
makes the comparison interpretable; avoid a rigid sequence when evidence points
to a simpler decisive check.

Keep a concise record of attempted checks, their conditions, and results,
including negative results and failed repair attempts. Reuse valid evidence;
do not repeat an unchanged attempt without a new reason. A negative check rules
out only what its coverage and environment establish, not every variation of
the hypothesis. Timing correlation or success after retry is not causal proof.

When an operation may have side effects, distinguish confirmed failure, running
work, and unknown outcome. Before retrying, inspect or reconcile status, or
establish that the operation supports safe replay of the same request within
its documented conditions. Guaranteed safe replay need not add a status call.
Use only supported retry or idempotency semantics and existing authority; a
lost response may conceal completed work. Do not assume every failure is safe
to retry or that a new request identifier preserves deduplication.

For uncertain outcomes of side-effecting operations, read
[recovery examples](references/recovery-examples.md) when choosing between
waiting, reconciliation, and replay under a documented guarantee.

## Stop at an evidence-backed conclusion

Report observed facts, the best-supported explanation with confidence and
alternatives, attempted checks, and the next discriminating action or authorized
repair. Keep unknowns explicit. Stop unproductive retries when new attempts no
longer reduce uncertainty or exceed the agreed resource boundary; name the
missing evidence or decision instead of inventing a cause.

For an authorized repair, rerun the original reported scenario as well as the
reduced check and relevant regressions where accessible. A passing reduced check
alone may miss the original failure; disclose any original scenario that remains
unverified. Separate containment, symptom recovery, and demonstrated cause. A one-off
recovery does not establish reliable prevention. Save diagnostic artifacts only
where writing is authorized and appropriate for their audience.

## Worked example

A job timed out after submitting a payment. The timeout shows no response, not
that payment failed. Inspect the permitted payment status using its existing
operation identifier, or use documented safe replay within its conditions and
existing authority. If neither trustworthy status nor supported replay is
available, retain an unknown outcome and identify the reconciliation needed.
A second successful charge would not prove that retry fixed the cause.

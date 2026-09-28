---
name: shape-feature
description: Shapes a feature for an understood problem into a bounded investment, rough approach, risks, exclusions, and a smallest useful end-to-end slice before implementation. Does not replace problem discovery, detailed behavior specification, or experiment design.
license: MIT
---

# Shape Feature

Turn an understood need into an implementable candidate whose value and limits
are clear. Use this when the problem is sufficiently understood but the feature's
scope or approach is still too open to commit to work. For a settled small change,
act within the existing scope rather than adding a planning phase.

## Establish the investment and value

Use the user's problem, beneficiary, expected outcome, domain constraints, and
relevant existing decisions. If the need is unclear, identify the missing frame;
do not quietly substitute a feature for discovery.

Find the time, effort, cost, or operational burden the user is willing to spend.
Distinguish this investment budget from an estimate of required effort and from
a deadline by which the result is needed. Treat the budget as a boundary for
choosing scope, not a promise that work will fit.
If no budget is supplied, offer a candidate or state the uncertainty; do not
invent an agreed duration or require a fixed delivery cycle.

If a forecast is useful or requested, estimate for the actual executor and named
completion endpoint: a local checked artifact, reviewed change, or deployed result
can have different dependencies. Use observed comparable work where available,
with its task, model, harness, checks, and rework limits; otherwise state assumptions
and uncertainty. Account for dependencies, feasible parallelism, and coordination.
Separate agent elapsed time, human attention, and external waiting only when
concrete dependencies justify it. Do not default agent work to human weeks or
apply a universal AI speedup or fixed minutes per round. If the user explicitly
requests a human-team estimate, use that executor and state its assumptions.
An execution request does not automatically need an estimation exercise.

## Outline a credible approach

Describe enough of the user journey and system interaction to show how the
feature could deliver value. Include waiting, empty, denied, error, cancellation,
or recovery behavior only where its absence would make this journey unusable or
misleading. Inspect relevant existing capabilities and their limits before proposing
a new abstraction, service, or dependency; reuse them where credible. Keep
implementation choices open when they do not affect feasibility or scope; avoid
a detailed task inventory or architecture chosen for appearance alone.

Identify risks that could consume the investment or break the promised outcome:
unknown dependencies, difficult integration, conflicting rules, or missing
access. Separate known obstacles from assumptions. Propose a bounded check for
a consequential unknown; an experiment is useful only when it changes a decision.

State exclusions and deliberate tradeoffs so the scope cannot grow silently.
Respect explicit user choices. Exclusions cannot remove a requirement needed
to make the promised result useful; narrow the promise or identify the conflict.

## Choose the first useful slice

Find the smallest end-to-end increment that a beneficiary can use and whose
result can be checked. Connect the relevant entry point, action, and outcome.
A database table or an isolated screen may be preparatory work, but should not
be presented as a useful completed feature by itself.

Describe observable completion and the remaining scope in a concise proposal:
value, investment boundary, rough approach, risks, exclusions, first useful
slice, and open decisions. Use only fields that matter. Do not force a planning
template or reopen settled decisions.

Planning authorizes no implementation, purchases, publication, or external
changes. If the user has already authorized execution, preserve that scope;
the shaping proposal does not expand it. Save only an authorized artifact.

## Worked example

Synthetic inputs: operators need to see which equipment inspections are overdue.
The existing list has due dates; the agreed rule marks dates before today overdue.
The request is planning-only, with a one-day investment boundary for a possible
local implementation; a missing due date has no agreed interpretation.

Resulting proposal: add an overdue filter to the current list using the agreed
due-date comparison. First useful slice: operator opens the list, filters, and
opens an overdue inspection. Show an empty result when none qualify. Exclude
new reminders and analytics. Risk: missing due dates could hide work; retain
that as an open rule rather than inventing a date. One day constrains this
candidate; it does not prove delivery will fit or authorize building it.

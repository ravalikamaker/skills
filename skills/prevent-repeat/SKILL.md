---
name: prevent-repeat
description: Proposes scoped prevention for repeated failures or recurring workarounds using recurrence evidence, cause uncertainty, and the earliest practical intervention point. Separates proposed ownership from assignment and measures benefit and harm; preserves urgent containment.
license: MIT
---

# Prevent Repeat

Reduce recurrence without turning a repeated symptom into an unsupported cause
or a mandate to redesign the surrounding system.

## Establish what actually repeats

Use this for repeated failed handoffs, recurring processing errors, or workarounds
that must be applied again. Read the relevant incidents or notes within permitted
access. Name the repeated event, conditions, and evidence of recurrence.
Repeated copies of one report are not separate incidents. If recurrence is not
established, say so and offer a narrower investigation instead of inventing it.

Keep urgent containment moving within its existing authority. A prevention plan
must not delay recovery or expand the active task's scope. Distinguish immediate
containment, recovery, and future prevention when those differ.

Separate established causes from plausible contributors and unknowns. A recovery
that coincides with improvement does not by itself identify the cause. Compare
conditions across incidents and note counterexamples before generalizing.

## Find a practical prevention point

Trace only the relevant sequence far enough to find where the repeated failure
could first be prevented or detected usefully. Choose the earliest practical
point, considering access, cost, reliability, and the people affected; earlier is
not always better if it imposes disproportionate burden.

Prefer a narrow change that addresses the supported mechanism. When the cause
is uncertain, propose a reversible intervention or a discriminating check, and
state what it can and cannot resolve. Consider whether a control merely moves
the failure elsewhere or makes recovery harder.

Name an early signal that could reveal recurrence before significant harm.
Tie the signal to the affected user or operator: what they would notice and
what action could prevent harm. Internal error counts alone may miss an
uncompleted journey. Distinguish a signal already observed from one proposed
for measurement. Avoid
adding broad monitoring, policy, or tooling solely because it might be useful.

## Make ownership and measurement explicit

Identify who would maintain or act on the intervention, if known. Label proposed
ownership as proposed; do not assign people, contact them, or create commitments
without authority. An unowned proposal is not an implemented control.

Specify how to observe benefit and relevant harm: recurrence frequency or effort
saved, plus false alarms, added delays, missed cases, or burden where relevant.
Use available baselines; label missing measurements and proposed targets.
Set a review or rollback condition appropriate to the intervention's consequence.

Return a concise prevention proposal with recurrence evidence, cause confidence,
intervention point, early signal, ownership status, and benefit/harm checks.
Planning does not authorize implementation, external changes, or publication.
Keep sensitive incident details appropriate to the output's audience.

## Worked example

Synthetic inputs: separate incident records I1 and I2 show maintenance requests
waiting through a shift change without acknowledgment. An additional delay in I3
occurred despite acknowledgment, so missing ownership is not the sole proven cause.

Proposal: try an acknowledgment prompt at the existing shift handoff; proposed
owner is the shift coordinator, not an assigned commitment. Early signal: a
request still lacks an acknowledged owner before the shift ends. Measure fewer
unowned delays alongside false reminders and extra handoff effort. Review the
candidate if reminders add burden without reducing delays. No prompt has been
implemented, and I3 remains a counterexample to a universal ownership explanation.

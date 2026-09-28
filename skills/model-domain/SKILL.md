---
name: model-domain
description: Clarifies domain vocabulary, business rules, invariants, and state transitions when conflicting meanings or uncertain rules block design or implementation. Builds a scoped model from existing evidence; does not impose an architecture or invent policy.
license: MIT
---

# Model Domain

Make the relevant business meaning precise enough to support the current decision.
Use this when names mean different things to different actors, important rules
are scattered, or a state change is unclear. A glossary rewrite or a routine
implementation with settled rules needs no modeling exercise.

## Bound the model

Start with the user's outcome, the affected actors, and the part of the domain
needed for this work. Read supplied examples, relevant decision records, and
existing enforcement within permitted access. Identify the core value or rule
that the work must preserve. Do not model the entire business by default.

Use the participants' language. Record conflicting meanings with their context
rather than silently choosing one or forcing a single vocabulary across
unrelated contexts. Separate business concepts from storage tables or interface
labels when their meanings differ.

## Establish rules through examples

Describe the relevant concepts, relationships, allowed states, and transitions.
For each consequential rule, identify its source, who it applies to, and a
concrete allowed or rejected example. Name invariants that must remain true
across changes, including ownership or timing where relevant.

Distinguish agreed rules, observed implementation, proposed rules, and unknowns.
Code describes current enforcement; it is not automatically the business
policy. If sources conflict, show the conflict and the decision needed rather
than inventing a resolution. Do not create legal, pricing, authorization, or
retention rules from plausible assumptions.

Locate existing enforcement only far enough to guide the work: where the rule
is checked, missing, or inconsistent. Do not prescribe new services, layers,
event systems, or a database migration merely to match the model.

When existing architecture constraints affect this domain, cite the agreed
constraint and connect it to a focused check or existing enforcement tool.
Separate observed violations from proposed design changes. Do not invent
governance, prescribe a new architecture, or treat a diagram as enforcement.

## Return a useful bounded model

Use the smallest form that makes the decision clear: a short vocabulary table,
rule examples, or a state diagram when useful. Include the source and confidence
of important rules, mismatches with current enforcement, and the unresolved
hotspot most likely to change the next action. A hotspot is an uncertainty to
resolve, not a mandate for a larger redesign.

Modeling does not authorize implementation or stakeholder outreach. Save an
artifact only when writing is authorized. A clear model is a proposal or account
of evidence, not proof that the running system follows it.

## Worked example

Synthetic inputs: venue staff use “active pass” for a paid pass; the gate uses
it for a pass not yet scanned. Policy P1 permits one admission per paid pass.
The gate currently checks payment but not prior admission; replacement-pass
handling is undocumented.

| Concept or rule | Resulting model |
| --- | --- |
| “Active” | Keep paid status and unused admission separate; one label hides two meanings. |
| Admission invariant | P1 requires payment and no prior admission; a paid, already-scanned pass is rejected. |
| Enforcement | The current gate checks only payment, leaving the one-admission rule unenforced. |
| Open decision | Replacement-pass handling needs a source-backed rule; do not invent a transfer policy. |

A settled rename of a gate label needs no wider domain model.

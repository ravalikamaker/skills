---
name: plan-implementation
description: Plans a scoped technical approach for settled intent using existing code and behavior, interfaces, data flow, dependencies, and representative end-to-end acceptance. Use before implementation when the technical approach or execution sequence needs definition; does not reopen feature scope or authorize execution.
license: MIT
---

# Plan Implementation

Turn settled intent into an approach that can guide the next implementation slice.
Preserve agreed requirements and explicit choices. Do not add a full design phase
for a literal edit or reopen the beneficiary, investment, or feature scope.

## Inspect the relevant system

Read the outcome, non-goals, current implementation, callers, decisions, and checks.
Trace the affected entry point through its data flow to the observable result.
Use existing capabilities where they satisfy the requirement; justify additions
by a named gap rather than hypothetical future use. Check external facts against
relevant official sources only when those facts affect the approach.

Distinguish facts supported by evidence, unknown information, assumptions used to
proceed, and open decisions. Resolve unknowns that could change the next slice's
approach using available source or authorized non-destructive checks. If a product
rule, authority, or inaccessible input cannot be resolved, name the specific choice
or prerequisite and defer only work that depends on it. Continue independent
planning. Do not mistake a chosen approach for evidence of its feasibility.

## Define the next useful slice

Describe the scoped changes, affected interfaces and data flow, reuse, and the
order of dependencies. Make inputs, outputs, errors, and side effects clear enough
for the next owner. Include compatibility or data-transition needs when the actual
change creates them; do not prescribe layers or migration phases by default.

Choose a representative end-to-end acceptance observation that reaches the promised
result, with rejection or recovery where it changes correctness. Identify focused
checks that cover isolated rules and required project gates. These are planned
checks, not execution proof. Read [planning examples](references/planning-examples.md)
when sequencing an evidence-dependent slice or separating authority from readiness.

Return the approach in the requested form with only the assumptions, open decisions,
risks, and limitations that affect execution. No new report, approval ritual, or
compulsory skill pipeline is required. Planning does not authorize source edits,
publication, or external changes. If execution was already authorized, this plan
preserves that authority without expanding it; mission-lead can coordinate it when
installed, but this skill remains independently useful.

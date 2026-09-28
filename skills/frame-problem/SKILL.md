---
name: frame-problem
description: Clarifies a problem before choosing a solution when a request starts with a proposed fix, an unclear beneficiary, or conflicting goals. Produces a bounded problem frame and decision-changing questions; skips routine tasks with clear outcomes.
license: MIT
---

# Frame Problem

Turn an unclear request into a useful decision frame without taking control of
what the user wants. A proposed solution is a candidate, not evidence of a need.

## Decide whether framing helps

Use this for requests such as “build a dashboard” without an intended decision,
“automate this process” without a named burden, or goals that conflict, such as
faster service and fewer interruptions. For an already clear routine task, act
within its authority instead of adding a discovery phase.

Read the supplied context and preserve explicit choices, constraints, and
non-goals. If the user has already chosen a solution, clarify its purpose without
reopening that choice unless evidence reveals a consequential mismatch.

## Separate the need from the proposed approach

Identify who experiences the problem and who should benefit. Do not assume the
requester, operator, customer, and affected bystander are the same person.
Describe the current difficulty using supplied examples or evidence; distinguish
an observed burden from a plausible explanation. Prefer concrete recent examples
and the current workaround to an abstract complaint; missing evidence stays
missing rather than becoming a discovery mandate.

State the intended benefit in terms of a changed experience, decision, or result.
Keep the proposed approach separate so alternatives can be considered when the
user wants them. Identify the core value that would remain useful if the proposed
interface disappeared. When the approach is still open, compare a few materially
different ways to deliver that value, including a simpler change to the current
process when credible. Do not substitute the agent's preferred goal for the user's.

Capture constraints that affect the decision: scope, time, resources, access,
privacy, and permitted actions when relevant. Name competing goals and tradeoffs
without silently deciding which stakeholder's interest wins.

Expose assumptions that could change the choice. Mark unknown beneficiaries,
baselines, or causes as unknown rather than filling them with invented evidence.
Ask only questions whose answers materially change the frame or next decision;
continue useful work that does not depend on those answers.

## Define useful success

Choose observable success criteria tied to the benefit and available evidence.
If a threshold is not supplied, propose it as a candidate rather than an agreed
requirement. Include relevant adverse effects when they could negate the benefit.
Distinguish deliverable completion from evidence that the real problem improved.

Return the smallest useful frame, usually:

- Beneficiary and current problem, with evidence or uncertainty.
- Intended benefit and observable success criteria.
- Constraints, non-goals, and competing goals.
- Important assumptions and the next decision-changing question or check.

This is a framing result, not approval to implement, collect private data, contact
people, or publish. Use only permitted context; sanitize shared artifacts for
their audience. Save a frame only when writing that artifact is authorized.

## Worked example

Synthetic inputs: “build a kiosk so visitors find their meeting room.” Two supplied
observations show visitors asking reception after room assignments changed; no
wayfinding baseline or cause is established. The venue already sends an arrival
message, and the user requires reception to remain available. No solution is
committed.

Resulting frame: visitors need to reach the current assigned room; a kiosk is one
candidate, alongside updating the existing arrival message. Success would be
finding the correct room with less reception help, with a threshold still proposed.
Constraints: use supplied observations and preserve reception access. Key unknown:
were instructions stale or hard to find? Check that distinction before choosing
the approach. This frame establishes neither a cause nor approval to build.

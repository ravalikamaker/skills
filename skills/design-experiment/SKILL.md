---
name: design-experiment
description: Plans a bounded test of an important uncertain assumption before further investment. Specifies a hypothesis, decisive observation, resource limit, and proceed/change/stop criteria; does not execute the test without authorization.
license: MIT
---

# Design Experiment

Design the smallest credible test that can change a decision. A plan is useful
only if different observations could lead to different next actions.

## Find the decision and uncertainty

Use this when a proposed feature depends on an untested need, a process change
rests on an uncertain cause, or a larger investment depends on feasibility.
Start from the user's decision, intended benefit, and constraints. Do not add an
experiment to a routine task whose relevant uncertainty is already resolved.

Identify the unverified premises the proposed approach relies on, then choose the one
whose failure would most change the decision. Explain that choice briefly.
Do not confuse an implementation check with a test of customer benefit.

State a hypothesis with enough scope to be contradicted. Separate observations
already available from predictions. If several explanations fit the evidence,
identify an observation that would help distinguish them rather than declaring
one cause proven.

## Make the test decisive and bounded

Describe the input, setting, participants or artifacts needed, and observation
that would support or weaken the hypothesis. Use only the data and access the
user permits. Avoid collecting unnecessary private information.

Choose a comparison or baseline when it helps separate the hypothesis from
normal variation or a competing explanation. Account for selection effects,
measurement limits, and adverse effects that matter to the decision. Make the
comparison credible: use comparable tasks, conditions, and outcome definitions;
name unavoidable differences that could explain the result. A small
qualitative test may inform a choice without establishing a population effect.

Set a time or resource limit based on supplied constraints; mark any suggested
limit as proposed. Prefer a reversible test with enough realism to inform the
choice. Avoid an elaborate study when a simpler check can resolve the uncertainty.

Define proceed, change, and stop criteria before observing results. Include an
inconclusive outcome and what it would leave unknown. Do not move thresholds
after seeing results merely to justify the preferred solution.

## Return a plan within authority

Include only the detail needed to carry out and interpret the test:

- Decision, uncertain assumption, and scoped hypothesis.
- Test method, decisive observation, and relevant comparison.
- Required access, time/resource limit, and relevant adverse effects.
- Proceed/change/stop criteria, including inconclusive results.
- Evidence limits and the next action requiring authorization, if any.

Planning does not authorize execution, purchases, outreach, external mutations,
or publication. If execution is already explicitly authorized, stay within that
scope; otherwise return the plan. Do not fabricate results, sample sizes,
statistical significance, or a claim that the hypothesis has been validated.

## Worked example

Synthetic inputs: before investing in a room-finding kiosk, the user permits a
30-minute planning budget and supplies a mockup plus the current arrival message.
No participants have been recruited and no results exist.

Proposed test: use comparable room changes in both formats, define a miss as
choosing the wrong room, and record reception help as an adverse cost. Proposed
criteria before execution: proceed to another bounded trial if misses decrease
without more help; change the approach if misses persist; stop this candidate if
it increases both misses and help. Mixed results or incomparable tasks are
inconclusive, leaving the benefit uncertain. These criteria are candidates,
not an agreed population effect or permission to recruit and run the test.

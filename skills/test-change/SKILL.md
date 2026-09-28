---
name: test-change
description: Selects, writes, and runs the smallest meaningful tests for an authorized code change, using independent expected results and preserving test integrity. Use for targeted coverage or regression proof; overall acceptance belongs to verify-work.
license: MIT
---

# Test Change

Own the testing work within the user's scope: inspect existing coverage, add or
adapt checks when needed, execute them, and interpret the results. A plan-only or
read-only request stays within that limit. Permission to edit tests does not
permit repairing source code or changing the intended behavior.

## Choose evidence that distinguishes a defect

Read the requested behavior, affected interfaces, existing tests, and project test
commands. Identify a plausible defect existing coverage would miss before adding
another test. Derive expected results from accepted requirements, examples, or an
independent reference; do not copy current output into assertions.

Choose the smallest decisive check: unit tests for an isolated rule, integration
checks for wiring or boundaries, and a real journey when connected behavior is the
claim. No test-count quota or universal E2E-only rule applies. Use the project's
existing tools; do not introduce a framework without a concrete need and authority.
Read [testing examples](references/testing-examples.md) for coverage choices,
changed expectations, substituted boundaries, or misleading success signals.

## Write and execute within scope

Preserve meaningful assertions and real boundaries. Do not skip failing checks,
weaken expectations, or replace the boundary under test with an always-successful
mock to obtain green results. Change a stale expectation only against an accepted
requirement, explaining the difference. Preserve unrelated tests and concurrent
work. Include relevant errors and side effects when they distinguish correctness.

For a bug fix, reproduce the failure before correction and success afterward
where practical. If the earlier version cannot run, state that fail-before proof
is missing. A tests-only task may correctly end with a failing regression test:
report the defect and leave source unchanged unless its repair is authorized.

Run accessible checks yourself or through permitted bounded delegation. Inspect
available tools before calling execution unavailable; do not assign routine QA
to the user. Honor required project gates. If CI-only execution needs absent
access or publication authority, inspect what is accessible, name the narrow gap,
and leave that check unresolved. External test records or effects need existing
authority; temporary local artifacts do not grant external mutation permission.

## Interpret the result

Report the targeted requirement, checks actually run and outcomes, and relevant
limits. Distinguish written tests from executed proof and real boundaries from
simulated ones. Retain evidence while its version and assumptions remain valid;
rerun affected checks after corrections and broaden only for a new concern.
A targeted test pass does not establish overall acceptance, hosted delivery, or
live-provider behavior. When installed, verify-work can assess overall completion;
this skill still completes its own testing work independently.

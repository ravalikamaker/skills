---
name: improve-codebase-experience
description: Diagnoses and repairs demonstrated friction developers and coding agents face navigating, setting up, running, changing, or verifying a repository. Use for a scoped development-workflow improvement or read-only DX/AX audit; not docs-only reconciliation, a single failure investigation, feature planning, or security/performance audits.
license: MIT
---

# Improve Codebase Experience

Reduce demonstrated friction in a representative development task. An audit or
diagnosis stays read-only; repair only within existing authority. Instructions
cannot create tools, access, harness capabilities, or permission.

## Observe a development journey

Choose a bounded task from the request: find the affected code, establish the
required environment, run it, make an authorized change, and verify its result as
relevant. Read the repository's actual entry points, conventions, commands, and
current state. Exercise accessible steps before treating an unfamiliar layout or
missing instruction as a defect. Do not manufacture a change for an audit.

For each useful finding, connect the friction to the affected task and evidence:
a failed command, misleading discovery path, uncontrolled state, inaccessible
prerequisite, or repeated avoidable work. Distinguish a setup/runtime/tooling
defect from documentation drift and missing access. Use available checks and name
the narrow prerequisite for blocked steps; unavailable proof is not failure or
success. Prioritize what prevents or distorts the selected journey, not a general
readiness score or speculative future need.

## Repair the supported cause

Use the smallest justified correction within authority, preserving repository
conventions and concurrent work. Reuse existing commands and canonical guidance.
When automation is affected, check relevant working-directory assumptions,
noninteractive operation, exit status, actionable errors, and useful bounded
output. Isolate ports, temporary files, databases, or generated state when shared
resources would interfere with another task. Do not weaken assertions or conceal
failure to make a command appear usable.

Add a helper, dependency, configuration, or instruction only when it remedies a
named gap. Do not impose a package manager, container, MCP integration, output
format, architecture rewrite, documentation tree, or harness installation.
Maintain the affected existing guidance when its contract changes. Read
[boundary examples](references/boundary-examples.md) when command behavior,
documentation drift, or harness limitations need distinguishing.

## Rerun and report

Repeat the affected journey after a repair, including relevant failure behavior
or repeatability when that was the problem. Reuse still-valid evidence and run
required project checks. Report the observed friction, correction or proposed
remedy, and before/after evidence; identify unrun steps and missing prerequisites.

Separate a successful local run from a clean or fresh-environment setup. State
which environment was exercised. A file or script existing does not prove that a
developer or agent can use it; installed instructions do not prove host discovery,
activation, or runtime behavior. Claim only the surfaces actually checked. Use
the requested response or existing artifact; no new report or global policy is
required. Keep private traces and internal lessons out of public examples.

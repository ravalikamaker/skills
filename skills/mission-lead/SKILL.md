---
name: mission-lead
description: "Coordinates workers for multi-step implementation, investigation, and review. Delegates substantial execution, selects models for assigned tasks, manages dependencies, and checks completion; handles trivial self-contained requests directly."
license: MIT
---

# Mission Lead

Default to delegating substantial execution. The lead owns scope, decisions,
coordination, and acceptance; workers own implementation, repairs, and assigned
integration. The lead may inspect and verify without taking over worker edits.
Handle trivial self-contained requests directly. Own authorized execution and
verification through the tools and delegation the current harness actually exposes.
Before handing work to the user, inspect the relevant capability, access, and
evidence; do not assume an old limitation still applies or bypass permissions.

**Leaf guard:** A delegated worker follows its bounded brief, never spawns children,
and does not apply this lead workflow recursively. Return decisions outside the
brief to the lead while continuing independent authorized work inside it.

## Frame and route

Establish the purpose, beneficiary, problem to solve, outcome, non-goals, authorized
actions, dependencies, completion criteria, and evidence needed to check them. Use the
user's clear framing; do not require a separate discovery exercise for routine work.
Respect user and host/workspace instructions; delegation cannot expand authority.
Keep research and review read-only unless fixes are authorized. Distinguish work
ready to execute, work blocked by a concrete prerequisite, and decisions that
need evidence before dependent execution. Continue ready work; investigate
unresolved decisions within scope rather than treating uncertainty as a blocker.
Ask only when a material intent, authority, capability, access, or input gap cannot
be resolved from available evidence.

Read relevant existing decisions and domain rules when they constrain this work.
Clarify shared terms or unresolved rules before assigning work that depends on
them; do not invent business rules from current implementation alone.

Prefer the smallest useful end-to-end increment with an observable result. Split
by coherent deliverables and explicit interfaces, not arbitrary file counts or
separate layers that cannot be checked together. Agree shared inputs, outputs,
error behavior, and ownership before dependent workers start. Keep batches small
enough to integrate and verify before widening scope.

Delegate dependent units sequentially; parallelize independently useful units when
ownership, shared contracts, and runtime resources permit. Tight coupling changes
scheduling, not the default to delegate substantial work. Batch tiny related steps
into one coherent unit instead of paying for many worker starts.

Before dispatch, read only the active harness reference, then the provider
reference for the selected worker. Do not load the whole index. Pass the worker
its selected settings and targeted task context, not every routing reference.

| Read when applicable | Reference |
| --- | --- |
| Active harness: Codex | [Codex](references/codex.md) |
| Active harness: Claude Code | [Claude Code](references/claude-code.md) |
| Active harness: Cursor | [Cursor](references/cursor.md) |
| Active harness: OpenClaw | [OpenClaw](references/openclaw.md) |
| Selected worker provider: OpenAI | [OpenAI models](references/openai-model-routing.md) |
| Selected worker provider: Anthropic | [Claude models](references/claude-model-routing.md) |
| Selected worker provider: xAI | [Grok models](references/grok-model-routing.md) |

Use only available native delegation tools and supported model settings. For an
unlisted harness or provider, inspect exposed capabilities and consult current
official documentation only as needed; never guess tools or model identifiers.
Preserve explicit model and effort choices, including the lead's. Distinguish
requested settings from observed execution; disclose what cannot be verified.

If native delegation is unavailable, explain the limitation and work directly
within existing authority. Do not replace an explicit team/model requirement or
an independence criterion with self-execution: ask narrowly about that dependency
and continue independent permitted work. Do not install a CLI fallback or change
configuration automatically to make delegation possible.

## Brief and coordinate

When readiness, unresolved decisions, shared-interface ownership, interrupted
work, or combined acceptance needs a concrete example, read the relevant section of
[delegation examples](references/delegation-examples.md).

Give each worker the purpose, beneficiary, problem, completion criteria, outcome and
non-goals, relevant facts, owned files or artifacts,
authorized actions, dependencies, checks, when to stop, and leaf guard.
Ask it to report changed paths or findings, evidence, unresolved issues, and limits.
Assign integration explicitly once inputs are ready. The implementation owner
maintains affected existing docs and comments in the same change, favoring the
existing canonical location. A new document should serve a named reader and use;
routine completion does not require new documentation files. Resolve routine in-scope
worker questions, including difficult ones, from available evidence rather than
passing them to the user. Escalate only a concrete missing capability, access,
information, material intent, or authority: ask for the smallest contribution
that removes the blocker, continue independent authorized work, and resume the
blocked work when supplied. Prior authorization persists within its scope.

Use fresh context for a distinct work unit; reuse the same worker for that unit's
corrections or recovery. Give an independent reviewer fresh context and primary
evidence. Avoid overlapping writes, including generated files and shared state;
verify actual isolation rather than assuming subagents have separate workspaces.
Transfer ownership explicitly before another worker edits the same material.

Track worker handles, ownership, decisions, completed checks, and remaining work
in existing context. Send failures and repairs back to the owning worker. Continue
recovery while new evidence or a changed approach makes progress, with concise
progress updates. Stop repeated attempts at the relevant limit or when they no
longer reduce uncertainty; identify the concrete blocker and smallest missing
contribution. Change scope only within the user's authorization. A timeout or
missing reply is not proof that no change occurred. Before replacing a worker,
inspect its output and state, preserving completed work. Before repeating side
effects, reconcile the outcome or establish supported safe replay within its
conditions and authority; use the interrupted-work example for details.

## Accept and report

Inspect artifacts and independently check decisive claims against completion
criteria. Verify the combined result and interactions between units; worker
assertions and silence are not proof. After corrections, rerun affected checks
and retain still-valid evidence. Report the outcome, evidence, and unresolved
limits, separating structural checks, installation/loading, and runtime behavior.

Discover companions by name only when applicable and available; each is optional.
Use `verify-work` to check outcomes and artifact correctness; without it, perform
the checks above. Use `session-handoff` when unfinished work must resume in another
session or with another owner; without it, summarize the state needed to resume.
Use `capture-learning` for a reusable lesson supported by evidence or an explicit
capture request;
without it, present the candidate and its evidence limits.
Do not automatically edit skill instructions or global memories to retain a lesson.

## Worked example

For “add CSV export; local edits only,” first agree the output columns and escaping
rules. Brief one worker to implement the exporter and checks, then brief the UI
owner against that contract. Inspect the combined download result and report the
local checks. Publication remains outside the brief. A delegated leaf implements
its assigned slice without starting another team.

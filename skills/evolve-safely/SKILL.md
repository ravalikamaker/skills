---
name: evolve-safely
description: Plans or implements consequential consumer-contract evolution, data migrations, and compatibility retirement. Preserves required behavior and data meaning with transition and recovery evidence; ordinary internal simplification belongs to simplify-code.
license: MIT
---

# Evolve Safely

Change an existing system with evidence about who depends on it and what must
remain true. Use this for a consequential API or schema evolution, migration,
or compatibility retirement. Ordinary internal simplification without consumer or
data risk needs no migration workflow; simplify-code can support it when installed.

## Discover the current contract

Read the requested outcome, agreed domain and architecture constraints, current
behavior, relevant decisions, and existing project checks. Find affected callers,
data readers and writers, generated clients, or other consumers through the
available evidence. Published docs and examples are part of the affected consumer
contract; identify their applicable version and audience, and maintain them with
the implementation change. Mark unknown consumers and deployment order instead of
assuming one repository contains every dependency.

Before preserving old behavior, identify the actual consumer, retained data,
supported contract, or explicit requirement that needs it. Earlier implementation
alone is no compatibility obligation. Unreleased, unmerged, or greenfield status
also does not rule out preview consumers or retained data. Resolve consequential
unknowns with targeted caller, usage, or data checks; do not invent consumers or
assume there are none.

Identify required inputs, outputs, errors, and data meaning, plus changes explicitly
allowed. Code that compiles does not establish consumer compatibility;
a schema migration that runs does not establish that old data keeps its meaning.

## Choose a transition proportional to the risk

Use existing capability when it satisfies the transition; justify a replacement
by a concrete consumer or data gap. Read [transition examples](references/transition-examples.md)
when choosing atomic change versus coexistence or assessing retirement and recovery.

Use a direct atomic change when relevant consumers and data can move together
safely and no compatibility obligation remains. Do not add aliases, adapters,
fallbacks, dual writes, or migration phases merely because old code exists.
Preserve required validation, security, and data integrity in either approach.
When old and new versions must coexist, consider expanding support,
migrating consumers or data, then removing the old form only after retirement
criteria are met. Do not impose this sequence when it adds no useful protection.

Define the order, ownership, and observable readiness of necessary steps. Cover
mixed-version behavior or resumable data conversion when relevant. Preserve
concurrent writes and unrelated work; use supported migration and retry semantics
rather than assuming every operation can be repeated without harm.

Make retirement criteria concrete: which consumers have moved, what data checks
must pass, and what evidence permits removing compatibility support. A quiet
log alone is insufficient when coverage is unknown. Do not leave a temporary
path permanent by forgetting its owner or removal condition.

## Verify transition and recovery

Check the before/after behavior, relevant consumer contracts, and data invariants
using the project's tools and representative existing data where permitted.
For staged transitions, check coexistence and progress before advancing; for an
atomic contract update, focused consumer and invariant checks may be enough. Retain versioned
evidence and rerun affected checks after corrections.

Choose recovery options before consequential mutation: supported rollback,
restore, forward correction, or stopping at a reversible boundary. Name their
limits. Reverting code does not undo converted data, external effects, or writes
made under the new format. Do not promise recovery that has not been established.

## Preserve execution authority

A planning or review request stays read-only and returns the bounded transition,
checks, open decisions, and recovery limits. A request to implement or migrate
authorizes its stated scope: do the work and verify it within that authority.
Do not ask again for already authorized local work or treat this skill as a
planning-only gate. Publication, destructive retirement, or external mutations
still require the authority that applies to those actions; the plan grants none.

Report what changed, compatibility and migration evidence, retirement status,
and remaining limits. Distinguish a prepared migration from an applied one and
local checks from observed consumer or production behavior.

## Worked example

An API changes an amount from decimal strings to integer minor units while older
clients remain active. Keep the old contract usable during the agreed transition,
verify representative amounts in both forms, and migrate consumers before removal.
Record the evidence required to retire the old form. Reverting the API code alone
would not reverse data already converted to minor units.

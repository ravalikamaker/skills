# Boundary examples

These examples are synthetic. They illustrate decisions, not required tooling.

## A command fails outside its launch directory

The accepted check command takes an absolute script path and promises use from
any directory. It resolves its test directory against the caller's directory and
fails from a neighboring checkout. If repair is authorized, anchor discovery to
the project path and rerun from both locations. Keep the real checks and their
failure exit status. Do not replace them with a success message or merely delete
the valid promise. Test a failing input when exit behavior is part of the claim.

If the command instead intentionally requires the repository root and the guide
alone says otherwise, correct the authorized guide. Establish the accepted
contract before deciding which side is wrong.

## Available setup and missing access

A documented local check runs, but a hosted preview requires an unavailable
account binding. Preserve the local result and name the missing access for that
preview. Do not call the repository broken, invent a receipt, or change access
configuration. A warm checkout with cached dependencies does not prove fresh
installation; use an isolated fresh setup only when it is relevant and permitted.

## Concurrent agents share state

Two otherwise independent checks overwrite the same generated file. Establish
which command owns that state before running both. Use existing configurable
output directories or sequence the checks; add isolation only if needed and
authorized. Separate workers or worktrees do not automatically isolate a database,
port, or external service. A new instruction can explain the supported command,
but cannot create a missing isolation capability.

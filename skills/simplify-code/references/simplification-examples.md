# Simplification examples

## Atomic internal change

Synthetic project: rename a private `normalize_tag` helper to `clean_tag`; its
three callers are in one module, and the agreed inputs and outputs stay the same.
Existing checks cover blank tags, spacing, and ordinary tags. Change the helper
and callers together within local edit authority, then run those focused checks.
No data or independently deployed consumer moves, so a compatibility layer or
multi-phase rollout adds no protection here.

## Where an abstraction's complexity goes

Synthetic refactor: three callers use an amount adapter that converts integer
minor units to the decimal strings required by legacy clients. Removing the adapter
would make each caller repeat conversion and rounding rules. The adapter therefore
concentrates a concrete compatibility rule; fewer files would not remove that
complexity. Check representative amounts through the callers before changing it.

A different wrapper simply forwards one private helper without translating inputs,
outputs, errors, or ownership. Removing that wrapper lets its sole caller invoke
the helper directly and may remove indirection without duplicating a rule. Check
that caller's contract rather than retaining a layer for hypothetical future use.
The thought experiment informs the choice; it neither mandates deletion nor
justifies an unrequested refactor.

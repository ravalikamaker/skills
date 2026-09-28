# Transition examples

## Atomic internal change

Synthetic project: rename a private `normalize_tag` helper to `clean_tag`; its
three callers are in one module, and the agreed inputs and outputs stay the same.
Existing checks cover blank tags, spacing, and ordinary tags. Change the helper
and callers together within local edit authority, then run those focused checks.
No data or independently deployed consumer moves, so a compatibility layer or
multi-phase rollout adds no protection here.

## Coexisting consumers and data

Synthetic request: move `delivery_date` from an unrestricted string to an ISO
date field. An older client still writes the old form; an agreed compatibility
rule maps valid old dates to ISO and reports ambiguous dates for resolution.
One partner integration has not yet been inventoried. This is a transition plan,
not authority to apply a production migration.

| Transition question | Concrete evidence or open decision |
| --- | --- |
| Can versions coexist? | Check agreed old/new reads and writes, including an old client reading a record created by the new client. Ambiguous dates must not silently acquire a meaning. |
| Can data move safely? | Record counts and representative values before/after conversion; verify unresolved values and concurrent writes are accounted for. Determine whether an interrupted conversion is safely resumable. |
| When may the old form retire? | Known clients have moved, the partner integration is resolved, and the agreed data/consumer checks pass. Quiet logs covering known clients do not resolve the unknown partner. |
| Who removes temporary support? | Name the actual owning team if established; otherwise mark ownership open. Removal waits for the retirement evidence and applicable authority. |
| What can recover? | Code revert alone does not restore rewritten dates or subsequent writes. Establish a supported restore, forward correction, or reversible stopping boundary and its limits. |

A passing schema check proves neither date interpretation nor compatibility.
Advance only using the evidence relevant to the chosen transition; do not turn
this example into a required migration sequence for every refactor.

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

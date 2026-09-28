# Transition examples

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

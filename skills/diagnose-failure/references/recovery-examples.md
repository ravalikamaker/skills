# Recovery examples

Synthetic job API: request body `{"document":"D7"}`, original operation key `K7`.
The caller has authority for one recovery attempt. Provider documentation, when
available, guarantees that an identical body with the same key creates at most
one job for ten minutes after the first submission. That guarantee does not
cover a new key, changed body, or expired window.

| Observation and evidence | Decision | Stop or remaining uncertainty |
| --- | --- | --- |
| Status lookup says the original job is running. | Keep that operation; inspect its supported progress rather than submit another. | At the task's waiting limit, report still-running state and next status check. |
| Reply was lost; no trustworthy lookup or replay guarantee exists. | Outcome is unknown. Seek reconciliation within permitted access; do not resend with a fresh key. | Stop blind submissions and name the missing operation evidence. |
| Original submission was two minutes ago; reply was lost; the documented guarantee applies to identical body and key `K7`. | A bounded identical replay is supported within the supplied authority, even without a status endpoint. | Preserve the original key/body and window. Replay success is recovery evidence, not proof of the timeout cause. |
| Original submission was fifteen minutes ago; reply was lost; only the ten-minute guarantee is documented. | The guarantee no longer establishes replay safety. Reconcile or obtain a supported recovery decision. | Do not assume the same key still deduplicates, or invent an extended guarantee. |

A “failed” status is decisive only if its documented meaning establishes what
side effects occurred. “Request failed to return a response” says less than
“job rejected before creation.” Keep that distinction in the diagnostic record.

For a local calculation bug, these operation-status branches may be irrelevant;
use the smallest reproduction and regression checks that distinguish its cause.
Do not introduce a job-state workflow into every diagnosis.

## Reproduce the reported symptom

Synthetic report: after adding an event and navigating away and back, the download
omits the new event. An executable reproduction starts with two known events,
adds a third, returns to the list, downloads, and asserts that the parsed CSV has
all three. Record the version and relevant navigation conditions. Checking the
export helper against a manually supplied three-row list may pass while missing
the reported stale-state failure.

Reduce the scenario by removing unrelated fields and actions while retaining the
add-and-return sequence that triggers the omission. A focused state check can help
locate the cause, but keep the original journey to rerun after an authorized fix.
If the failing environment is inaccessible, inspect available state handling and
compare logs or versions while naming the missing reproduction evidence. A useful
hypothesis is still a hypothesis; a local reduced pass does not prove the original
scenario recovered.

# Delegation examples

These examples use a synthetic project. Adapt the brief to actual ownership and
authority; the file names are examples, not paths to create by default.

## A bounded brief with a shared interface

Request: “Add a local event-list download; no publishing.” The agreed output is
UTF-8 CSV with columns `date,title`, a header even for no rows, and CSV escaping
for commas and quotes. The screen already owns the event list.

A useful exporter brief:

> Implement the agreed event CSV contract in `src/event-csv.ts` and its focused
> checks. You own those files only. Input is the existing list of date/title
> values; output is CSV text, with no fetching or file-system side effects.
> Preserve the supplied field values and ordering. The UI owner will consume
> this interface after it is checked. Do not edit the screen or publish. Return
> changed paths, representative output, checks, and any unresolved input rule.
> Stop and report a contract conflict rather than choosing a new date format.
> You are a leaf; do not spawn workers.

The UI brief owns the existing screen separately and connects the verified
exporter to a download action. This is a dependency, not a reason for both
workers to edit shared files at once.

## Interrupted work and uncertain outcomes

A UI worker stops responding after writing a file. Its silence does not show
whether the edit finished. Inspect the current diff, running handle, and checks
before replacing it; retain valid work and transfer file ownership explicitly.
For an external upload with a lost reply, distinguish confirmed failure,
still-running work, and unknown outcome. Reconcile the original operation or
use documented safe replay within authority. For example, if the guarantee covers
an identical body and original key for ten minutes, preserve both and stay within
that window; a guarantee can support replay without a separate status endpoint.
A fresh upload ID or expired window could duplicate work. If neither status nor
replay semantics are available, report the unknown outcome and the evidence
needed rather than blindly repeating it.

## Acceptance across contributions

Both workers report passing checks, but the screen exports a stale list after
an event is added. The exporter can be correct while the combined journey fails.
Return the stale-input repair to the UI owner and rerun the affected journey.
Acceptance covers the current-list download and agreed CSV behavior; it does
not establish publication or production behavior.

## Routine questions and a real access blocker

A worker asks whether the download should preserve list order. The existing
contract already requires that order. The lead resolves the question and returns
it to the worker; difficulty alone does not require a user decision. If a local
check fails, the owning worker repairs it within the authorized brief, and the
lead checks the combined result using the available shell or browser.

A later hosted check requires an account the current tools cannot access. Inspect
the exposed tools and permitted access first; an earlier session's limitation is
not current evidence. If access is still missing, name the hosted behavior that
remains unverified and request only the account binding or specific observation
needed. Continue local checks, preserve their results, and resume the hosted check
when the prerequisite is supplied. Do not ask the user to perform all QA, install
a fallback, bypass permissions, or repeat approval already granted for the check.

## Ready work, a blocker, and a decision needing evidence

Synthetic request: implement a local event CSV download and verify it on a hosted
test account. Local work and the hosted check are authorized. The columns and
escaping rules are agreed, but the lead has not yet established whether adding an
event invalidates the current list cache. The hosted account is not bound to an
accessible tool.

The exporter is ready: brief its owner and run its checks. The cache question is
an unresolved decision with available evidence, not a reason to stop the exporter
or ask the user to choose a cache strategy. Inspect the existing data flow or use
a local add-and-download check before assigning dependent UI changes. The hosted
check has a real access blocker; inspect current capabilities, then request only
the missing account prerequisite and retain the local evidence.

Keep these states in existing task context, updating them as evidence arrives.
They require neither new tickets nor a fixed timebox or context-size threshold.
If the missing item were a material product rule with no accepted source, ask that
narrow question and continue the independent exporter work.

## Permission does not settle the approach

Request: implement a local cancellation action. The accepted policy permits only
pending reservations, and the lead has source access. A previous note assumes the
UI passes a reservation ID, but the current handler passes a display label.

Inspect the actual caller and API before dispatching dependent work. Preserve the
pending-only rule, establish the shared ID and rejection contract, and assign the
UI/API sequence with file ownership. The assumption is invalidated by source;
reassess the brief rather than sending two workers conflicting interfaces. No new
product decision or approval is needed to use the accepted policy and inspect code.
An independent copy change can proceed if its meaning does not depend on the ID.

If policy instead leaves confirmed cancellation undecided, name that open decision
and ask only about it before assigning the dependent behavior. An agent may inspect
existing behavior but cannot silently adopt it as policy. Local edit authority
and source access do not make an unresolved business rule ready to implement.

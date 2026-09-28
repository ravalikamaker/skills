# Behavior examples

## Observable outcomes and an open ordering rule

Synthetic report rules: an accepted report starts queued; a queued report may
be cancelled without producing a download. Once processing starts, cancellation
is denied and processing continues. No ordering rule exists for simultaneous
start and cancellation.

| Starting condition | Action | Observable outcome | Source or open rule |
| --- | --- | --- | --- |
| Report is queued. | Owner cancels. | State becomes cancelled; no download is produced. | Supplied queued-cancellation rule. |
| Report is processing. | Owner cancels. | Cancellation is denied; processing state remains. | Supplied processing rule. |
| Start and cancellation arrive together. | Both operations compete. | Undecided; contrasting possible orders need an agreed outcome. | Ordering rule is open, not an implementation choice to hide. |

An unresolved outcome is not a passing acceptance criterion. Storage locks and
component names stay out of this specification unless part of the agreed contract.

## Retry behavior at a documented boundary

Synthetic submission contract: an identical body with original key `J4` may be
replayed safely for five minutes after the first submission. Caller authority
permits at most one replay.
Status can report running or completed; the contract gives no replay guarantee
after five minutes.

| Starting condition | Action | Observable outcome | Source or open rule |
| --- | --- | --- | --- |
| Original operation reports running. | Consumer requests recovery. | Continue or inspect the original operation; do not promise a completed result. | Supplied running status. |
| Original submission was two minutes ago; response was lost. | Replay identical body with `J4` once. | No second operation is created under the documented guarantee; an extra status call is not a prerequisite. | Supplied five-minute replay guarantee and one-replay authority. |
| Original submission was eight minutes ago; response was lost. | Consumer requests another submission. | Outcome remains unknown pending reconciliation or a supported recovery decision. | Expired guarantee; no new-key safety rule is supplied. |

These examples specify expected behavior. They do not show that a provider or
implementation passed a check. A synchronous text formatter needs none of these
operation states unless its actual contract introduces them.

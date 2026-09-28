# Acceptance examples

## Documentation can expose a code defect

An accepted API contract and current guide say an expired token creates no job.
The implementation returns an error but creates a job first. Check both the
response and the side effect; changing the guide to allow creation would hide the
defect. Conversely, when an accepted flag rename is implemented correctly, update
the affected usage example or report it as stale. Inspect only the relevant
docs and comments, and do not add a completion report unless requested or useful.

## Independent acceptance

For a consequential combined export, an optional independent acceptance brief
can supply the agreed columns, permissions, current event fixture, and runnable
application without first showing the exporter code or the producer's rationale.
The evaluator exercises the journey and compares the downloaded artifact with
those requirements. This can expose a shared implementation assumption that a
source-led review overlooks.

Choose this separation only when it adds useful evidence and permitted independent
execution is available. It does not require a second reviewer for every task.
After observing a defect, provide source and diagnostic context as needed; keeping
a debugger blind would obstruct the repair. If the boundary cannot be exercised,
report that limit rather than treating independence as proof of correctness.

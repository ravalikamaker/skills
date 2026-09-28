# Planning examples

## Settled export, an unknown data flow

Request: plan a local event download. Columns, escaping, and list order are agreed;
no implementation is authorized. The current screen reads from a cache, and the
existing CSV utility handles quoted values. Whether adding an event refreshes the
cache is unknown.

Inspect the screen's query and mutation paths before choosing UI wiring. Reuse the
CSV utility if it meets the agreed contract. Plan exporter coverage independently,
then resolve cache refresh before assigning the dependent download input. The
acceptance observation is add an event, download through the screen, and inspect
parsed current rows in the agreed order. A ready banner or quoting test alone does
not establish that the downloaded list is current. Do not change columns or build
while planning. Missing cache evidence is not a product choice for the user when
source can answer it.

## Authority and readiness are different

Local cancellation implementation is authorized, but policy does not say whether
confirmed bookings may cancel. Existing code accepts them. That is evidence of
current behavior, not an accepted rule. Plan the independent UI location and trace
the existing state flow; ask for the missing cancellation decision before planning
the dependent policy change. Do not infer a new business rule from source.

Conversely, a complete schema-conversion plan can be technically ready while
production mutation lacks authority. Return the plan and its recovery limitations;
readiness does not grant migration permission. A literal local variable rename
needs neither a transition design nor a formal planning artifact.

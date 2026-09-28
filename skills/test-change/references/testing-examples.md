# Testing decisions

## A suite passes but misses a connected defect

Synthetic export requirement: a team member downloads only their own team's CSV,
including quoted names. Existing unit tests cover quoting; an endpoint test passes
by supplying a team identifier directly. Neither checks whether the signed-in
journey passes the correct identity to the endpoint.

A useful added journey check signs in as team A, downloads through the actual
application, and compares the parsed rows with the independently supplied team A
fixture. This catches identity wiring or another team's data appearing in the
file. A focused integration check can isolate the authorization rule. More quote
variants add little unless they expose a distinct uncovered defect. Replacing the
authorization boundary with an always-allow mock would remove the needed proof.

## A business rule is better isolated directly

Synthetic rule: a discount applies to subtotals of at least 100, excluding delivery.
Given subtotal 99 and delivery 5, a discount of 15 must leave subtotal 99. A focused
rule check detects an incorrect total-including-delivery comparison more clearly
than repeating a full checkout for every boundary. Derive the expectation from
the accepted rule, not the calculator's current output. A representative checkout
can separately check that the rule is connected to the customer's actual total.

If a bug is reproducible, run the distinguishing check before the repair, then
against the corrected artifact. If the old artifact or environment is unavailable,
record that fail-before proof is missing. A simulated payment provider may support
local checkout assertions but leaves real payment execution untested.

## A changed expectation or a failing gate

An accepted requirement now permits cancellation only while pending. Updating an
old test that expects cancellation after confirmation is a legitimate correction
when tied to that decision. Dropping its state assertions merely because the new
code fails them is not. Likewise, local tests passing does not satisfy a required
CI integration gate: trigger and inspect it when authorized and repair within
scope, or report the specific unresolved access or authority gap.

## Apparent success and the promised result

Synthetic note editor: saving displays a success banner. If persistence is promised,
save a distinct permitted value, reopen the note or refresh in a fresh view, and
compare the value read back with the supplied expectation. The banner alone does
not show that storage succeeded. Use a temporary record when authorized; do not
change an external record without authority for that check.

For the CSV journey above, add an event with a recognizable title before another
download, then inspect the parsed file. A cached fixture or stale screen state can
pass the first download while omitting the new event. Changing the input makes
that defect observable. A download notification does not establish file contents;
a generated image or report likewise needs inspection of the result itself.
These checks answer particular claims, not a universal refresh-and-persistence
checklist for stateless artifacts.

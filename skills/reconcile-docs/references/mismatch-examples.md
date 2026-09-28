# Synthetic mismatch examples

Read only the example relevant to the disputed claim or source boundary.

## Current promise, defective code

The accepted export contract says expired tokens are rejected without creating
an export. The current API guide repeats it, but a local test with an expired
token creates a job. This is a code defect, not evidence that the guide should
promise job creation. An audit reports the claim, guide location, observed job,
and repair needed. With code-repair authority, fix the rejection boundary and
check that no job is created, retaining valid-token behavior.

## Superseded units and generated documentation

An accepted version-two decision changed a CLI timeout from seconds to
milliseconds. Version-two parsing uses milliseconds, but its help-source text and
generated command reference still say seconds. Correct the help source and
regenerate through the existing command; check the documented invocation against
the parser. Preserve the version-one guide's seconds contract as historical.
If the version-two parser also used seconds, both code and docs would need
reconciliation with the accepted decision, within their respective authority.

## Conflicting intent without an accepted decision

A current guide promises unlimited retries; a recent draft proposes a limit of
three, and code uses three. No decision or owner confirmation establishes which
policy was accepted. Inspect accessible history and tests for acceptance evidence.
If it remains missing, ask which policy is current and report the conflict;
do not silently bless either document or code. Continue independent corrections,
such as a verified command rename, while leaving the retry limit unresolved.

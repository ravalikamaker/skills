# Context changes the choice

These are synthetic decision examples, not implementation mandates or measurements.

## C# failure contracts

Compare the caller's required outcomes, existing contract, recovery, and diagnostics,
not only whether a failure is called expected or unexpected.

- A form accepts arbitrary numeric text and needs only valid/invalid plus the parsed
  value. `TryParse` can express that contract without exception-driven validation;
  introducing a richer Result type adds no required outcome here.
- A booking operation must distinguish sold-out, policy rejection, and success so
  callers can take different actions. An existing typed Result or outcome contract
  can carry those distinctions. A Boolean alone loses required information. This
  does not justify converting unrelated parsing or infrastructure APIs to Result.
- A file operation already reports I/O failures through exceptions, and a boundary
  can recover from a specific failure or preserve its diagnostic context. Retain
  that contract unless caller needs establish a reason to translate it. Do not
  catch every exception and convert it into an ordinary business rejection;
  cancellation, cleanup, and state after failure still need their own semantics.

[Microsoft's exception guidance](https://learn.microsoft.com/en-us/dotnet/standard/exceptions/best-practices-for-exceptions)
supports avoiding exceptions for routine conditions and using available `Try*`
APIs where they fit. It does not prescribe Result for every failure. The typed
booking outcome above follows the synthetic caller requirements, not a universal
Microsoft recommendation. No additional error-handling library is implied.

Changing valid/invalid validation to require distinct actionable rejection reasons
can change the selected representation. Renaming the screen cannot. Revisit when
the caller contract, recovery needs, or supported platform behavior changes.

## Freshness versus reuse

A public catalog permits five-minute-old content and repeats many reads; an
existing cache with bounded expiry may meet that contract while reducing requests.
A booking confirmation must use current availability at the authoritative write;
reusing that stale catalog value would violate its contract. Evaluate both against
freshness, correctness, request cost, and operational burden, allowing the different
requirements to lead to different choices. A new page title changes neither choice.

If request volume or latency is unknown, do not invent a cache speedup. Recommend
conditionally from the freshness contract and inspect existing access patterns
before claiming performance benefits. Revisit when the allowed staleness, source
invalidation behavior, or observed workload changes.

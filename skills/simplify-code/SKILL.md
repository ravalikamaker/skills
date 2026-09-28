---
name: simplify-code
description: Reduces internal abstraction, duplication, or indirection in a bounded code area while preserving required observable behavior. Use for authorized simplification or its read-only assessment; consumer contract evolution and data migrations belong to evolve-safely.
license: MIT
---

# Simplify Code

Make the requested code easier to understand and change without moving complexity
into its callers. Work in the named area and affected callers; do not turn local
cleanup into an unsolicited repository refactor. Review and plan requests remain
read-only. Implement authorized local simplification and verify it.

## Identify what can disappear

Read the affected implementation, callers, checks, and agreed constraints. Identify
which abstraction, repeated rule, or forwarding layer causes concrete friction.
Ask where its complexity would go if removed: does the layer concentrate a real
rule or merely move indirection? Compare a concrete caller or change scenario;
fewer lines or files alone do not prove a simpler design. Read
[simplification examples](references/simplification-examples.md) when assessing
shared rules, forwarding wrappers, or an atomic internal change.

Prefer the smallest coherent change. Keep useful boundaries and comments that
explain non-obvious invariants, rationale, or contracts. Do not replace duplication
with a generic framework that adds more concepts than it removes. Preserve
unrelated and concurrent work.

## Preserve the observable contract

Identify required inputs, outputs, errors, ordering, side effects, and relevant
performance or architecture constraints before editing. Compare affected behavior
with the prior version or independent accepted examples using the project's checks.
Tests must remain meaningful; do not update expectations to bless accidental drift.
Use focused equivalence checks when they cover the claim and broader checks when
interactions require them. If installed, test-change can help author missing
coverage; testing is still owned and executed within this task's authority.

An internal cleanup does not authorize public API changes, data conversion,
compatibility removal, or changes to independently deployed consumers. If those
are required, stop that expansion, name the contract and separate authority needed,
and complete independent in-scope work. When installed, evolve-safely supports the
consequential transition; it is not required for an ordinary internal simplification.

Report what complexity was removed, behavior evidence, and remaining limits. Do
not describe a shorter diff or passing formatter as behavioral equivalence.

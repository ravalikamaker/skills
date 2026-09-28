# OpenAI worker routing

Last checked: 2026-09-27. Read only when selecting an OpenAI worker.

These are suggested starting routes for this skill, informed by the current
[model guide](https://learn.chatgpt.com/docs/models), not empirical guarantees.
Keep explicit user pins. Confirm availability in the active harness.

| Work unit | Suggested model | Initial effort |
| --- | --- | --- |
| Focused extraction, code mapping, repeatable transformations, bounded fixes | `gpt-6-luna` | `high` |
| General implementation, investigation, research, and integration | `gpt-6-sol` | `medium` |
| Complex correctness review, subtle interactions, demanding edge cases | `gpt-6-sol` | `high` |
| Exceptional uncertainty or consequential multi-step reasoning beyond the preceding routes | `gpt-6-astra` | `low`, then adjust from evidence |

Route by ambiguity and verification difficulty, not job title alone. Start with
the smallest route that can meet the evidence requirement; do not send difficult
review to the lightest model solely to save cost. Higher effort can increase
latency and usage. Use supported levels; cross-model effort labels are not
equivalent. Do not default to Max or Ultra or use automatic delegation to bypass
the leaf guard.

Maintain only recent active models here. Recheck the official guide when a route
is unavailable or model support changes; update this file without expanding the
main skill into a historical catalog.

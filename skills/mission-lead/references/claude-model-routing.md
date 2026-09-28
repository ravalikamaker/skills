# Claude model routing

Checked: 2026-09-27. Load only when selecting a Claude worker. These are task-routing suggestions, not comparative benchmark results. Preserve explicit model choices; the host's available models and supported settings take precedence.

| Task | Suggested current model | Starting effort |
| --- | --- | --- |
| Bounded extraction, classification, mechanical edits with clear checks | Haiku 4.5: `claude-haiku-4-5-20251001` | No effort parameter |
| Routine implementation, scoped research, ordinary debugging | Sonnet 5: `claude-sonnet-5` | `high` (provider default) |
| Difficult integration, consequential review, sustained agentic work | Opus 5.5: `claude-opus-5-5` | `medium` (provider default) |
| Demanding reasoning or long-horizon work that remains inadequate on Opus | Fable 5.1: `claude-fable-5-1` | `high` (provider default) |

The official current lineup still includes Haiku 4.5 as its fastest specialization; it is not a recommendation to fall back through older generations. Fable and Opus use always-on adaptive thinking; Sonnet supports adaptive thinking. Effort support is model-specific: do not translate a host's generic reasoning control into an unsupported API parameter. [Official model lineup and IDs](https://platform.claude.com/docs/en/models/overview).

Start with the smallest capable route for the bounded task, then inspect its result against the acceptance checks. Missing context calls for a better brief; unresolved reasoning difficulty can justify a stronger route. Refresh this reference when availability changes. Provider API IDs may differ from a harness's accepted aliases.

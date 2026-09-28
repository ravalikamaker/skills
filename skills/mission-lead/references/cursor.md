# Cursor delegation

Checked: 2026-09-27. Load for Cursor only. Read just the selected provider's routing reference when needed: [OpenAI](openai-model-routing.md), [Claude](claude-model-routing.md), or [Grok](grok-model-routing.md). A provider model's existence does not guarantee Cursor availability.

Custom subagents live in `.cursor/agents/` for a project or `~/.cursor/agents/` for the user. Files contain YAML frontmatter and a prompt body. Relevant fields include `name`, `description`, `model`, `readonly`, and `is_background`. Existing built-in or custom workers may suffice; creating files is optional.

`model: inherit` is the default; a supported explicit model ID selects another route. Model-specific parameters use an ID followed by bracketed `key=value` options. Only use options supported for that model in Cursor's current model catalog; do not assume provider API parameters work unchanged.

Team restrictions, plan availability, and legacy Max Mode requirements can make Cursor substitute a compatible model. Check available models, plan settings, and observable execution details before claiming the requested route ran. Subagents can be invoked by `/name` or a natural-language delegation request. [Official subagent configuration and fallback behavior](https://cursor.com/docs/subagents).

Use concise, task-specific descriptions and bounded briefs. Read-only review workers should have `readonly: true` where available. Parallel workers need independent ownership; background execution alone does not establish independence. Check the combined result before acceptance. Do not change user or team settings merely to enforce this skill's suggested route.

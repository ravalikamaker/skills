# Codex delegation

Last checked: 2026-09-27. Read only when Codex is the active harness.

Inspect the exposed native tool schemas for spawning, steering, waiting, and
releasing workers. Names and parameters vary by surface; do not invent calls.
Check history-fork restrictions before requesting model or effort overrides.
Confirm workspace sharing or isolation and respect the reported concurrency cap.

Codex supports custom-agent TOML files in `.codex/agents/` (project) and
`~/.codex/agents/` (personal). A file requires `name`, `description`, and
`developer_instructions`; optional `model` and `model_reasoning_effort` select its
route. This is configuration guidance, not an instruction to create files.

For model/effort, custom-agent values override resolved spawn settings. Before
that layer, explicit spawn values precede `[agents]` defaults, then parent values.
Selecting a model without an effort can use the model's default; inspect the
chosen role and returned execution metadata rather than claiming the request won.

Optional `[agents]` configuration includes `enabled`,
`max_concurrent_threads_per_session`, `default_subagent_model`, and
`default_subagent_reasoning_effort`. Leave existing settings alone unless changing
them is part of the user's task. Missing native tools follow the main skill's
fallback boundary.

Source: [OpenAI subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents).
Use the available OpenAI Docs tool first for unresolved details, then official
documentation; current runtime schemas govern callable behavior.

# OpenClaw delegation

Checked: 2026-09-27. Load for OpenClaw only. If selecting a provider, read only its routing reference: [OpenAI](openai-model-routing.md), [Claude](claude-model-routing.md), or [Grok](grok-model-routing.md).

Confirm native `sessions_spawn` availability in the active session; `/tools` shows its effective tools. Configured models or an API connection do not by themselves expose delegation. Tool policy can remove spawn capabilities. Use existing permitted capabilities; this reference does not authorize broadening policy.

For same-agent native children, the active parent model and thinking are inherited unless `agents.defaults.subagents.model` / `.thinking` or per-agent `agents.entries.*.subagents` defaults override them. Explicit spawn `model` and `thinking` take precedence. Cross-agent children use the target agent's configured model; ACP has different defaults. Invalid model overrides can fall back with a warning, so inspect the tool result.

Non-thread native children default to isolated context; thread-bound children can default to forked history. Request `context: "isolated"` for independently briefed work. Fork only when prior conversation is necessary. [Official tool parameters and defaults](https://docs.openclaw.ai/tools/subagents/tool-reference).

Keep worker assignments bounded and leaves for this mission. Save the returned child identity for follow-up, and accept results only after checking evidence. Separate spawn acceptance from completion. If native delegation is absent, disclose that limitation and continue within the mission's authorized fallback; do not present external CLI subprocesses as native children. No global configuration edit is required to apply this guidance.

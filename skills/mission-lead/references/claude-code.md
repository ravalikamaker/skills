# Claude Code delegation

Checked: 2026-09-27. Load for Claude Code only. When selecting a Claude model, additionally read [Claude routing](claude-model-routing.md); do not load other provider references.

Custom subagents use Markdown with YAML frontmatter in `.claude/agents/` (project) or `~/.claude/agents/` (user). Session definitions can use `--agents`. Managed definitions outrank session, project, user, and plugin definitions. Existing definitions may be sufficient; this skill does not require configuration changes.

The `model` field accepts supported family aliases, full IDs, or `inherit`. Normal selection order is invocation override, definition frontmatter, `CLAUDE_CODE_SUBAGENT_MODEL`, then parent model. `inherit` in frontmatter selects the parent directly. The force variable `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` changes this behavior; consult the source for its fork/inheritance exceptions before assuming an override will work.

Organization allowlists can cause substitution. Check `/tasks` for the running model and displayed effort rather than treating configuration as execution proof. Thinking follows the parent; effort is a distinct frontmatter control. [Official subagent configuration and precedence](https://code.claude.com/docs/en/sub-agents).

Give each worker a bounded task, necessary context, permissions, and acceptance checks. Keep this mission's workers as leaves even if the installed host supports nesting. Reuse the task owner for related repairs; use a fresh worker for an independent assignment. If the installed version exposes different controls, follow its actual capabilities and disclose the limitation without changing global settings.

# Install and use

Choose the bundle **or** standalone copies in each host. The bundle is named
`ravalikamaker-skills`; the repository marketplace is `ravalikamaker`. All routes
use the same thirteen directories under `skills/`. These instructions describe
host-supported mechanisms; see the [README status](../README.md#try-a-skill)
for the limits of native checks.
Commands below are actions for you to run; installation uses your host's normal
scope and permission controls.

## Codex

In your terminal:

```sh
codex plugin marketplace add ravalikamaker/skills
codex plugin add ravalikamaker-skills@ravalikamaker
```

For local source, replace `ravalikamaker/skills` with the absolute clone path.
Start Codex, open `/plugins`, and confirm the bundle is installed and enabled.
Start a new session and ask “Use verify-work to check this change against my
requirements,” selecting the bundled skill if needed.

To refresh a Git marketplace, run `codex plugin marketplace upgrade ravalikamaker`,
then repeat `codex plugin add ravalikamaker-skills@ravalikamaker` to refresh the
installed bundle. For a local marketplace, refresh the source clone and repeat
`plugin add` directly; `marketplace upgrade` accepts Git sources only.
Remove it through `/plugins` or
`codex plugin remove ravalikamaker-skills@ravalikamaker`.

If it is missing, inspect `codex plugin list` and the marketplace registration;
restart after installation. The IDE extension does not support plugins: use
[standalone skills](#standalone-skills) in `.agents/skills/` there.

Sources: [OpenAI plugin guide](https://learn.chatgpt.com/docs/plugins),
[CLI reference](https://learn.chatgpt.com/docs/developer-commands).

## Claude Code

In a Claude Code session:

```text
/plugin marketplace add ravalikamaker/skills
/plugin install ravalikamaker-skills@ravalikamaker
```

Use an absolute clone path instead of the repository for a local marketplace.
Choose the desired scope in the install panel. Check the Installed tab in
`/plugin`, then start a fresh session. Try
`/ravalikamaker-skills:verify-work` with a concrete task and its requirements.

Use the Installed tab's **Update now** and **Uninstall** actions for maintenance.
If the bundle is absent, check the marketplace and install scope. If skills are
stale, start a new session or run `/reload-plugins`. The compatibility manifest
lives in `.claude-plugin/`; no root-manifest support is assumed for Claude Code.
For a single skill, use [standalone copies](#standalone-skills) in `.claude/skills/`.

Source: [Claude Code plugin lifecycle](https://code.claude.com/docs/en/discover-plugins).

## Cursor

Until a separate marketplace submission is approved, use a local bundle or
[standalone copies](#standalone-skills). Download or clone this repository. Copy
its `plugin.json` and entire `skills/` directory into a new directory at
`~/.cursor/plugins/local/ravalikamaker-skills/`. Keep `plugin.json` directly
inside that directory.

Run **Developer: Reload Window**, open **Customize**, and check that all thirteen
skills appear. Select the skill there or type `/verify-work` with your task.

To update, replace the local bundle with a fresh reviewed copy and reload. To
uninstall, remove only that local bundle directory and reload. Preserve any
local edits before replacement or removal.

If discovery fails, confirm the folder layout and whether your organization
allows local plugin imports. A symlink pointing outside the local plugins folder
is skipped. An installed marketplace plugin of the same name takes precedence.
Standalone skills belong in `.cursor/skills/` in your project.

Source: [Cursor plugin installation and local testing](https://cursor.com/docs/plugins).

## GitHub Copilot

### Copilot CLI

```sh
copilot plugin install ravalikamaker/skills
copilot plugin list
```

A local clone path can replace the repository. Start a fresh session and ask
“Use verify-work to check this change against my requirements.” Check the skill
catalog as well as the plugin list before treating discovery as successful.

Update with `copilot plugin update ravalikamaker-skills`; uninstall with
`copilot plugin uninstall ravalikamaker-skills`. Use the name reported by
`copilot plugin list` if it differs. If skills are missing, check for a standalone
copy with the same name: project or personal skills can take precedence.

Source: [Copilot CLI plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference).

### Copilot in VS Code

Run **Chat: Install Plugin From Source** and enter
`https://github.com/ravalikamaker/skills`. If already installed through Copilot
CLI, check **Agent Plugins - Installed** first; VS Code discovers those installs.
Use **Chat: Configure Skills** to check discovery, then start a new chat and make
the same explicit request above.

Run **Extensions: Check for Extension Updates** to check updates. Right-click
the bundle in **Agent Plugins - Installed** and choose **Uninstall** to remove it.
If unavailable, check host version, plugin enablement, and organization policy.
For either Copilot surface, [standalone copies](#standalone-skills) go in
`.github/skills/`; the Skills CLI agent name is `github-copilot`.

Sources: [VS Code plugins](https://code.visualstudio.com/docs/agent-customization/agent-plugins),
[standalone skills](https://code.visualstudio.com/docs/agent-customization/agent-skills).

## OpenClaw

From the configured target workspace, install one folder from a separate clone:

```sh
openclaw skills install /absolute/path/to/clone/skills/verify-work
```

Repeat for `frame-problem`, `design-experiment`, `mission-lead`,
`model-domain`, `shape-feature`, `specify-behavior`, `session-handoff`,
`capture-learning`, `prevent-repeat`, `connect-insights`, `diagnose-failure`,
and `evolve-safely`
to install all thirteen. OpenClaw uses individual skills here, not this repository's plugin
manifest. A [manual folder copy](#standalone-skills) is also supported.

Check `openclaw skills list` and `openclaw skills check`, start a new session,
and ask “Use verify-work to check this change against my requirements.”
To update local-source installs, preserve your edits, refresh the clone, and
repeat each install command with `--force`. Reinstalling an existing skill
without it fails. `openclaw skills update` tracks ClawHub installs only. To uninstall copies,
remove only their folders from the active workspace's `skills/` directory.
Preserve local edits first.

If absent, check which workspace the agent uses and check for user-wide copies
in `~/.openclaw/skills/`. Do not use this source repository as the target workspace.
No ClawHub listing is claimed; publication there is a separate step.

Sources: [OpenClaw skills](https://docs.openclaw.ai/tools/skills),
[skill diagnostics](https://docs.openclaw.ai/cli/skills).

## Standalone skills

Download or clone the repository and copy each **whole skill folder**, including
its references, into the host's project destination:

| Host | Project destination |
| --- | --- |
| [Codex](https://learn.chatgpt.com/docs/build-skills) | `.agents/skills/` |
| [Claude Code](https://code.claude.com/docs/en/skills) | `.claude/skills/` |
| [Cursor](https://cursor.com/docs/skills) | `.cursor/skills/` |
| [GitHub Copilot](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) | `.github/skills/` |
| [OpenClaw](https://docs.openclaw.ai/tools/skills) | `skills/` in the configured workspace |

For example, from this clone, copy one skill to a separate Codex project:

```sh
mkdir -p /path/to/project/.agents/skills
cp -R skills/verify-work /path/to/project/.agents/skills/
```

Repeat for the other names, or copy all thirteen folders for the full set. Start a new
session and use a [README example](../README.md#try-a-skill). If missing, check
that the destination is `<skills directory>/<name>/SKILL.md`, not a nested copy
of the repository, and that the host opened the intended project.

To update, download the desired revision and replace only the installed skill
folders after preserving your edits. To uninstall, remove only those folders and
restart the host. For Skills CLI installations, use its `list`, `check`, `update`,
and `remove` commands, reviewing their selected skills and scope first. Native
plugin managers do not manage standalone copies.

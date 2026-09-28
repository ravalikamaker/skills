# Skills

Portable [Agent Skills](https://agentskills.io/specification) by
[ravalikamaker](https://github.com/ravalikamaker) for product and engineering
work, from clarifying problems through delivery and learning.

## Start here

Choose your harness, then install individual skills or the bundle.
Choose **one installation method** per host to avoid duplicate skills.

| Your harness | Individual skills | Bundle |
| --- | --- | --- |
| [Codex](docs/install.md#codex) | Skills CLI or folder copy | Repository plugin marketplace (CLI) |
| [Claude Code](docs/install.md#claude-code) | Skills CLI or folder copy | Repository plugin marketplace |
| [Cursor](docs/install.md#cursor) | Skills CLI or folder copy | Local plugin; not publicly listed |
| [GitHub Copilot CLI / VS Code](docs/install.md#github-copilot) | Skills CLI or folder copy | Direct repository plugin |
| [OpenClaw](docs/install.md#openclaw) | Native skill install or folder copy | Install the skill folders |

For an individual skill, run this in your **target project**, with Node.js and
pnpm available. Change `codex` to `claude-code`, `cursor`, `github-copilot`, or
`openclaw` for your host:

```sh
pnpm dlx skills add ravalikamaker/skills --skill mission-lead --agent codex --copy
```

Replace `mission-lead` with any name below, or `'*'` to copy the full set. You can
also replace `ravalikamaker/skills` with an absolute path to this clone.
The [Skills CLI](https://github.com/vercel-labs/skills) is optional;
[manual installation](docs/install.md#standalone-skills) needs no Node.js or pnpm.

## Try a skill

Start a new host session after installation. Select the skill in your host's
skill picker, or explicitly ask for it by name:

| Skill | What it helps with | Example request |
| --- | --- | --- |
| [frame-problem](skills/frame-problem/SKILL.md) | Clarify an unclear or solution-first request. | “Use frame-problem on our idea to add a dashboard: who benefits, what problem it addresses, and how we would recognize success.” |
| [model-domain](skills/model-domain/SKILL.md) | Clarify domain terms, rules, and state changes from evidence. | “Use model-domain to clarify what confirmed means in this booking flow and which cancellation rules are agreed or unresolved.” |
| [shape-feature](skills/shape-feature/SKILL.md) | Bound a feature for an understood need and investment. | “Use shape-feature on CSV reconciliation export: we have two days; propose the approach, risks, exclusions, and first useful slice.” |
| [specify-behavior](skills/specify-behavior/SKILL.md) | Make expected outcomes concrete before implementation. | “Use specify-behavior for cancellation before payment; show success, rejection, and unresolved boundary examples.” |
| [design-experiment](skills/design-experiment/SKILL.md) | Plan a bounded test before investing in a proposed change. | “Use design-experiment to plan a small test of whether a shorter signup helps new users; include the hypothesis, limits, and decision rule.” |
| [diagnose-failure](skills/diagnose-failure/SKILL.md) | Investigate a failure with competing explanations and decisive checks. | “Use diagnose-failure to investigate these intermittent import failures; separate observations, hypotheses, negative attempts, and the next useful check.” |
| [test-change](skills/test-change/SKILL.md) | Write and execute focused tests for an authorized change. | “Use test-change to add and run regression coverage for this discount boundary; keep source unchanged.” |
| [simplify-code](skills/simplify-code/SKILL.md) | Remove internal complexity while preserving required behavior. | “Use simplify-code to remove this forwarding layer; preserve shared validation, errors, and side effects.” |
| [evolve-safely](skills/evolve-safely/SKILL.md) | Change existing contracts while protecting consumers and data. | “Use evolve-safely to plan the amount-field migration while old clients remain active; include compatibility, retirement criteria, and recovery limits.” |
| [evaluate-options](skills/evaluate-options/SKILL.md) | Choose between viable approaches using requirements, evidence, and scoped tradeoffs. | “Use evaluate-options to compare cached and fresh reads for this flow; recommend an approach and say what evidence would change it. Do not implement.” |
| [plan-implementation](skills/plan-implementation/SKILL.md) | Plan a technical approach and execution sequence for settled intent. | “Use plan-implementation to inspect the current download flow and plan the next local slice, interfaces, dependencies, and acceptance; do not build yet.” |
| [mission-lead](skills/mission-lead/SKILL.md) | Coordinate substantial work and check completion. | “Use mission-lead to implement CSV export in this project, delegate independent work where supported, and verify the result.” |
| [reconcile-docs](skills/reconcile-docs/SKILL.md) | Reconcile docs and implementation against accepted intent in either direction. | “Use reconcile-docs to audit this CLI guide against its current implementation and accepted contract; report stale claims and code defects without edits.” |
| [verify-work](skills/verify-work/SKILL.md) | Check outcomes against independent evidence. | “Use verify-work to review this report against the attached source data and tell me what is still unproven.” |
| [write-clearly](skills/write-clearly/SKILL.md) | Remove filler and clarify substantive prose while preserving meaning and voice. | “Use write-clearly to revise this engineering update; retain all evidence limits, links, and permissions.” |
| [session-handoff](skills/session-handoff/SKILL.md) | Preserve unfinished work for another session. | “Use session-handoff to save a checkpoint in docs/handoff.md with decisions, checks, and the next action.” |
| [capture-learning](skills/capture-learning/SKILL.md) | Save a reusable lesson with its evidence. | “Use capture-learning to record what this retry failure taught us in docs/learning/retries.md.” |
| [prevent-repeat](skills/prevent-repeat/SKILL.md) | Propose prevention for a recurring failure. | “Use prevent-repeat on these repeated missed handoffs; identify a prevention point, proposed owner, and benefit and harm measures.” |
| [connect-insights](skills/connect-insights/SKILL.md) | Compare sources for useful patterns and contradictions. | “Use connect-insights on these interview notes and support reports; trace each pattern to sources and consider alternative explanations.” |

Each skill works independently. No database, memory service, bootstrap, hooks,
or mandatory settings are required. Mission Lead can use the other skills when
installed, with bounded fallbacks when they are absent. Delegation and model
selection depend on the tools your host actually exposes. Writing a handoff or
lesson requires an authorized destination; installation grants no extra authority.

The bundle includes portable Agent Skills and host compatibility manifests.
Packaging and structural validation do not establish installation, discovery,
model-driven activation, or task quality on every host. Check the skills in your
intended host; a public marketplace or directory listing is a separate step.

## Help and contribute

[Installation, updates, removal, and troubleshooting](docs/install.md) ·
[Authoring and validation](docs/authoring.md) · [Contributing](CONTRIBUTING.md)

[Report a bug or propose an improvement](https://github.com/ravalikamaker/skills/issues/new/choose),
ask in [Q&A](https://github.com/ravalikamaker/skills/discussions/categories/q-a),
explore [Ideas](https://github.com/ravalikamaker/skills/discussions/categories/ideas),
or share an experiment in [Show and tell](https://github.com/ravalikamaker/skills/discussions/categories/show-and-tell).
Use synthetic examples and sanitized summaries. Do not post secrets, private
transcripts, customer data, or internal context.

[MIT License](LICENSE).

# Authoring and validation

## Layout

```text
skills/                     # Skill source, each in its own directory
  mission-lead/
    SKILL.md                # Delegation-first mission orchestration
    references/             # On-demand provider and harness guidance
  verify-work/SKILL.md       # Outcome and artifact acceptance
  session-handoff/SKILL.md   # Task continuity
  capture-learning/SKILL.md  # Durable reusable lessons
  frame-problem/SKILL.md     # Beneficiary, problem, constraints, and success
  model-domain/SKILL.md      # Scoped vocabulary, rules, and state transitions
  shape-feature/SKILL.md     # Bounded approach and first useful slice
  specify-behavior/SKILL.md  # Concrete observable outcomes and boundary examples
  design-experiment/SKILL.md # Bounded hypothesis-test planning
  diagnose-failure/SKILL.md  # Evidence-based failure investigation
  evolve-safely/SKILL.md     # Compatibility, migration, and retirement
  reconcile-docs/SKILL.md    # Documentation and implementation drift in either direction
  prevent-repeat/SKILL.md    # Recurring-failure prevention proposals
  connect-insights/SKILL.md  # Multi-source synthesis with provenance
templates/
  SKILL.md.template         # Starting point; excluded from skill discovery
scripts/
  validate_skills.py        # Official spec, local links, and eval structure checks
  validate_package.py       # Plugin manifests, catalogs, and portable package checks
requirements-dev.txt        # Pinned validation dependencies
.github/workflows/
  validate.yml              # Runs the same check on pushes and pull requests
```

A skill lives at `skills/<name>/SKILL.md`, with optional `scripts/`,
`references/`, and `assets/` alongside it. Copy the entire skill folder when
installing so relative references remain intact.

Mission Lead loads only the active harness reference and selected worker's model
provider reference when dispatching. Provider files cover recent active models,
with checked dates and official sources; refresh the relevant file as support
changes instead of accumulating historical model lists. Model routes are suggested
defaults, and installation does not establish delegation or runtime compatibility.

## Author a skill

1. Choose one repeatable task and a lowercase hyphenated name, such as `my-skill`.
   Identify concrete inputs, outputs, and a few user requests before writing instructions.
2. Create `skills/my-skill/` and copy `templates/SKILL.md.template` into it as
   `SKILL.md`.
3. Replace the template metadata and instructions. The `name` must match the
   directory. Describe both what the skill does and when an agent should use it.
   Include likely exclusions so neighboring skills remain distinct. Keep instructions
   short and meaningful; explain decisions an agent would otherwise get wrong. Use
   linked supporting files only when their detail warrants loading on demand, and
   keep them inside that skill's directory. Add
   `evals/evals.json` with `skill_name` and an `evals` array; start with 2–3
   synthetic cases containing `id`, `prompt`, `expected_output`, and `assertions`.
   Add more cases as needed; there is no upper limit.
4. Run the validator, then install the skill in each intended host. Confirm that
   the host discovers it, then exercise its behavior.
   Check both appropriate activation and cases where it should stay inactive; use
   paired behavior evaluations before claiming an improvement.
5. Review the content before committing and publishing. Add the actual skill to
   this README once it exists.

These practices follow the official [OpenAI skill guidance](https://learn.chatgpt.com/guides/best-practices#turn-repeatable-work-into-skills)
and [Anthropic authoring guidance](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate_skills.py
.venv/bin/python scripts/validate_package.py
.venv/bin/python -m unittest discover -s tests -v
```

Validation uses the official `skills-ref` validator pinned in
`requirements-dev.txt`, plus repository checks for a nonempty instruction body,
local Markdown links staying within each skill bundle, and behavioral fixture
structure. An empty catalog fails. The unit tests cover validator regressions.
Passing means structural validation only; host discovery, activation, and runtime
behavior require separate verification. External URLs and link fragments are not
validated.

### Evaluate skills

`evals/trigger-cases.json` contains explicit, implicit, and negative selection
cases: three positive and three near-miss negatives for each of fourteen skills
(84 cases total).
Choose the single best initial skill, or none; later skill use is outside this fixture.
Recheck existing negatives whenever the catalog grows to avoid cross-skill label
collisions. Compare metadata-only skill catalogs with the expected labels withheld,
then score selections against each case's `expected_skill` (or `null`). This
simulation does not establish actual host activation, task behavior, or statistical
improvement. Tests with native host traces remain separate.

Each `skills/<name>/evals/evals.json` contains synthetic task cases and assertions
for behavior evaluation. Follow each case's optional `setup`; paths in `files`
are relative to the skill root. Copy those inputs into a clean temporary workspace
using the destination layout described in `setup`. Mark scenarios with unavailable
prerequisites skipped, not passed. Run matched fresh sessions **with and without the skill**
on the same host/model and starting state; for revisions, also compare old and new
versions. Keep generated results and traces **outside this repository**. Report
host/model versions, source commit, attempts, baseline comparisons, and limits;
separate installation/discovery, observed activation, and runtime outcomes.
Measure actual outcomes and relevant regressions, including rework and user
interventions. Use repeated matched trials for reliability claims and preserve
held-out tasks. Prefer deterministic checks when available; use calibrated
human or model judgment for criteria that require it. Report time and cost only
when observed, with method and limits. An authorized learning note may retain a
negative result with evidence and scope; a failed run is not a permanent rule.
See [Contributing](../CONTRIBUTING.md#evaluate-a-change) for the evaluation workflow.

## Releases

The package version is `0.4.0`; a version bump is not publication evidence. Before publishing a change, bump the
version consistently in `plugin.json`, `.claude-plugin/plugin.json`, and every
marketplace catalog entry that carries it. Both catalogs point at this repository
root and share the same `skills/` tree. Never alter an already published version
or move a release tag; publish a new version instead.

Record the source commit and checks in release notes. Treat structural checks,
host discovery, activation, and task outcomes as separate evidence. Only claim each level of native host
behavior after it has been observed on a named host/version.
Cursor marketplace listing and ClawHub publication are separate submission
steps; repository packaging does not establish either listing.

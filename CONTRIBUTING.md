# Contributing

Small fixes, reproducible feedback, and evaluation cases are welcome. Search
[existing issues](https://github.com/ravalikamaker/skills/issues) and
[discussions](https://github.com/ravalikamaker/skills/discussions) before starting.

## Where to contribute

- Use a [bug or behavior report](https://github.com/ravalikamaker/skills/issues/new?template=bug-behavior.yml)
  for installation failures, missed or unwanted activation, and incorrect outcomes.
- Use an [improvement proposal](https://github.com/ravalikamaker/skills/issues/new?template=improvement.yml)
  for a concrete change with an example and a way to check success.
- Use [Ideas](https://github.com/ravalikamaker/skills/discussions/categories/ideas)
  to explore a direction, [Q&A](https://github.com/ravalikamaker/skills/discussions/categories/q-a)
  for usage questions, or [Show and tell](https://github.com/ravalikamaker/skills/discussions/categories/show-and-tell)
  for experiments and results. If Discussions is unavailable, use an issue.

Use minimal **synthetic examples**. Do not upload secrets, credentials, private
transcripts, customer data, internal context, or identifying local paths. Describe
what happened with a short, sanitized excerpt or a recreated example; avoid raw
session exports. Review attachments and links as carefully as the text.

## Report evidence precisely

Include the skill name and source commit, host name and version, model/provider
and exact model version if exposed, relevant settings, and a synthetic prompt.
Say “unknown” for details the host does not expose. Requested model settings are
not proof of the model that executed the task.

Keep these observations separate: structural validation, installation/discovery,
observed activation (or nonactivation), and runtime task outcomes. A copied folder
or a metadata selection simulation does not prove native host behavior. Include
expected and observed behavior, attempts/failures, and limits to reproduction.

## Evaluate a change

`evals/trigger-cases.json` tests metadata-based selection boundaries. Each skill's
`evals/evals.json` supplies task prompts, expected outcomes, and assertions for
behavior checks; neither is a record of measured success.

1. Choose a relevant fixture or add a small synthetic case. Include a case that
   should activate and a nearby case that should stay inactive when changing
   selection instructions. Define success before inspecting outputs. Keep some
   realistic tasks held out from authoring so revisions do not merely fit known
   fixtures; disclose when a held-out case becomes a regression fixture.
2. Run the same task **with the skill and without the skill**, in separate fresh
   sessions with the same host, model, tools, permissions, and starting files.
   Follow the case's optional `setup`; its `files` paths are relative to the skill
   root. Copy inputs into a clean temporary workspace with the destination layout
   specified by `setup`. Skip and report cases whose prerequisites are unavailable.
   For a revision, also compare the old and new skill. State any unavoidable
   differences, unavailable tools, or unobserved activation.
3. Check the actual outcome and relevant regressions, not just the response
   wording. Record rework, retries, and user interventions needed to reach the
   result. Use deterministic checks where available; for judgment-based criteria,
   use a stated rubric and calibrate human or model judgments against sample
   outputs rather than treating an uncalibrated score as ground truth.
4. Use repeated matched trials when claiming reliability, including failures and
   variance; disclose attempt counts and comparisons. Report time or cost only
   when observed, with the measurement method and limits. One successful run is
   a smoke check, not evidence of a reliable improvement.
5. Keep raw outputs, traces, and generated reports **outside this repository**.
   Share only a reviewed, sanitized summary in the issue, discussion, or PR:
   fixture IDs, versions, baseline versus skill results, and remaining limits.

There is no bundled native-host evaluator. Run behavioral cases in the host you
intend to support; do not claim cross-host compatibility from one host's result.

## Turn feedback into a fix

Maintainers first reproduce a report with a sanitized fixture, then add a
regression evaluation case and make a scoped fix. Compare old and new behavior
on the same case, retain a without-skill baseline where relevant, and publish a
short summary with evidence limits. Consumer reports inform this review; they
are not automatically ingested into skill instructions. Negative results can
inform an authorized `capture-learning` note with its evidence and scope; they
do not automatically become permanent rules, global memory, or policy changes.

## Authoring and releases

See [Authoring and validation](docs/authoring.md) for the layout, checks, and
version policy. Keep published versions immutable and synchronize bundle
manifests and catalog versions when releasing.

## Submit a pull request

Keep the change focused and retain the portable `skills/<name>/SKILL.md` layout.
Keep supporting files inside the skill directory and update relevant fixtures
when changing behavior. Explain the problem, resulting behavior, and evidence
in the PR template; link an existing issue or discussion when useful.

Run the repository's structural validator before submitting:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate_skills.py
.venv/bin/python scripts/validate_package.py
.venv/bin/python -m unittest discover -s tests -v
```

Report checks actually run and anything untested. Documentation-only changes do
not need a fabricated runtime evaluation. Do not commit evaluation outputs or
private reproductions.

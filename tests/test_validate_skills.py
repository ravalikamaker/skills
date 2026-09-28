"""Regression coverage for spec failures and independently installable bundles."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_skills import validate_skill


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.skill = Path(self.temp.name) / "example"
        self.skill.mkdir()
        self.document = self.skill / "SKILL.md"
        self.document.write_text("---\nname: example\ndescription: Synthetic fixture.\nlicense: MIT\n---\nDo the task.\n")
        (self.skill / "evals").mkdir()
        self.evals = self.skill / "evals/evals.json"
        self.data = {"skill_name": "example", "evals": [{"id": 1, "prompt": "Inspect this fixture.", "expected_output": "Evidence-backed finding.", "assertions": ["Does not edit."]}]}
        self.evals.write_text(json.dumps(self.data))

    def errors_after(self, old, new):
        self.document.write_text(self.document.read_text().replace(old, new))
        return "\n".join(validate_skill(self.skill))

    def test_valid_bundle(self):
        self.assertEqual(validate_skill(self.skill), [])

    def test_official_validator_rejects_host_specific_field(self):
        self.assertIn("Unexpected fields", self.errors_after("license: MIT", "license: MIT\nmodel: made-up"))

    def test_official_validator_rejects_directory_mismatch(self):
        self.assertIn("must match", self.errors_after("name: example", "name: different"))

    def test_duplicate_yaml_key_fails(self):
        self.assertIn("YAML", self.errors_after("license: MIT", "license: MIT\nlicense: Apache-2.0"))

    def test_empty_body_fails(self):
        self.assertIn("body must not be empty", self.errors_after("Do the task.", ""))

    def test_malformed_frontmatter_fails_without_crash(self):
        self.assertTrue(self.errors_after("description: Synthetic fixture.", "description:\n  nested: value"))

    def test_inline_and_reference_links_checked(self):
        self.assertIn("missing local link", self.errors_after("Do the task.", "[Guide][guide]\n\n[guide]: references/missing.md"))

    def test_links_with_fragments_and_escaped_spaces(self):
        (self.skill / "guide file.md").write_text("# Intro\n")
        self.assertEqual(self.errors_after("Do the task.", "[Guide](guide%20file.md#intro) [Web](https://example.invalid) [Here](#local)"), "")

    def test_nested_reference_links_checked(self):
        (self.skill / "references").mkdir()
        (self.skill / "references/guide.md").write_text("[Missing](missing.md)")
        self.assertIn("references/guide.md: missing local link", "\n".join(validate_skill(self.skill)))

    def test_escape_and_symlink_outside_bundle_fail(self):
        outside = Path(self.temp.name) / "outside.md"
        outside.write_text("Private fixture")
        (self.skill / "outside.md").symlink_to(outside)
        errors = self.errors_after("Do the task.", "[Parent](../outside.md) [Symlink](outside.md)")
        self.assertEqual(errors.count("escapes skill bundle"), 2)

    def test_code_sample_is_not_treated_as_live_link(self):
        self.assertEqual(self.errors_after("Do the task.", "```markdown\n[Sample](missing.md)\n```"), "")

    def test_missing_evals_fails(self):
        self.evals.unlink()
        self.assertIn("cannot read evals", "\n".join(validate_skill(self.skill)))

    def test_invalid_eval_assertion_and_duplicate_id_fail(self):
        self.data["evals"] *= 2
        self.data["evals"][0]["assertions"] = [""]
        self.evals.write_text(json.dumps(self.data))
        errors = "\n".join(validate_skill(self.skill))
        self.assertIn("unique positive integer", errors)
        self.assertIn("nonempty string assertions", errors)

    def test_more_than_three_cases_allowed(self):
        self.data["evals"] = [dict(self.data["evals"][0], id=i) for i in range(1, 6)]
        self.evals.write_text(json.dumps(self.data))
        self.assertEqual(validate_skill(self.skill), [])

    def test_eval_fixture_paths_checked(self):
        self.data["evals"][0]["files"] = ["evals/missing.txt", "../private.txt"]
        self.evals.write_text(json.dumps(self.data))
        errors = "\n".join(validate_skill(self.skill))
        self.assertIn("missing fixture file", errors)
        self.assertIn("file escapes skill bundle", errors)

    def test_valid_eval_setup_and_fixture(self):
        (self.skill / "evals/input.txt").write_text("Synthetic input")
        self.data["evals"][0].update(setup="Copy input.txt into a temporary workspace.", files=["evals/input.txt"])
        self.evals.write_text(json.dumps(self.data))
        self.assertEqual(validate_skill(self.skill), [])

    def test_cli_fails_on_missing_root(self):
        script = Path(__file__).resolve().parents[1] / "scripts/validate_skills.py"
        result = subprocess.run([sys.executable, str(script), "--root", str(self.skill / "absent")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("does not exist", result.stderr)


if __name__ == "__main__":
    unittest.main()

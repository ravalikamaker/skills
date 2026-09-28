"""Regression checks for the package users actually install."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_package import validate_package

REPO = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for relative in ("plugin.json", ".claude-plugin", ".agents", "skills"):
            source, target = REPO / relative, self.root / relative
            if source.is_dir():
                shutil.copytree(source, target)
            else:
                shutil.copy2(source, target)

    def change(self, relative, mutate):
        path = self.root / relative
        data = json.loads(path.read_text())
        mutate(data)
        path.write_text(json.dumps(data))
        return "\n".join(validate_package(self.root))

    def test_current_package(self):
        self.assertEqual(validate_package(self.root), [])

    def test_official_schema_rejects_extra_core_field(self):
        self.assertIn("official schema", self.change("plugin.json", lambda d: d.update(skills="./elsewhere")))

    def test_official_schema_rejects_invalid_author_type(self):
        self.assertIn("official schema", self.change("plugin.json", lambda d: d.update(author="publisher")))

    def test_version_drift(self):
        self.assertIn("metadata must match", self.change(".claude-plugin/plugin.json", lambda d: d.update(version=d["version"] + "+drift")))

    def test_invalid_versions(self):
        for version in ("latest", "01.2.3", "1.2", "1.2.3-01", "1.2.٣", 1, None):
            with self.subTest(version=version):
                self.assertIn("version must be SemVer", self.change("plugin.json", lambda d: d.update(version=version)))

    def test_catalog_identity_and_source_drift(self):
        for relative in (".claude-plugin/marketplace.json", ".agents/plugins/marketplace.json"):
            with self.subTest(relative=relative):
                self.assertIn("drifted", self.change(relative, lambda d: d["plugins"][0].update(source="./skills/mission-lead")))

    def test_catalog_version_drift(self):
        self.assertIn("drifted", self.change(".claude-plugin/marketplace.json", lambda d: d["plugins"][0].update(version=d["plugins"][0]["version"] + "+drift")))

    def test_catalog_name_drift(self):
        self.assertIn("marketplace name", self.change(".agents/plugins/marketplace.json", lambda d: d.update(name="other")))

    def test_policy_drift(self):
        self.assertIn("drifted", self.change(".agents/plugins/marketplace.json", lambda d: d["plugins"][0]["policy"].update(installation="INSTALLED_BY_DEFAULT")))

    def test_missing_skill(self):
        (self.root / "skills/verify-work/SKILL.md").unlink()
        self.assertIn("missing bundled skill", "\n".join(validate_package(self.root)))

    def test_extra_skill(self):
        (self.root / "skills/accidental").mkdir()
        self.assertIn("expected exactly", "\n".join(validate_package(self.root)))

    def test_misrouted_skill(self):
        shutil.move(self.root / "skills/verify-work", self.root / ".claude-plugin/verify-work")
        self.assertIn("misrouted skills", "\n".join(validate_package(self.root)))

    def test_skill_symlinks(self):
        path = self.root / "skills/verify-work/SKILL.md"
        path.unlink()
        path.symlink_to(REPO / "skills/verify-work/SKILL.md")
        self.assertIn("must not use symlinks", "\n".join(validate_package(self.root)))

    def test_malformed_json_and_catalog_types(self):
        (self.root / "plugin.json").write_text('{"name":')
        self.assertTrue(validate_package(self.root))
        self.assertIn("exactly one", self.change(".claude-plugin/marketplace.json", lambda d: d.update(plugins=[None])))

    def test_missing_root(self):
        self.assertTrue(validate_package(self.root / "absent"))

    def test_duplicate_json_key(self):
        (self.root / "plugin.json").write_text('{"name":"one","name":"two"}')
        self.assertIn("duplicate JSON key", "\n".join(validate_package(self.root)))

#!/usr/bin/env python3
"""Validate the portable plugin and its two host catalogs without network access."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

from jsonschema import Draft202012Validator

SCHEMA = Path(__file__).parent / "vendor/agent-plugins-1.0.0/plugin.schema.json"
SCHEMA_SHA256 = "0a4aad95ce337878ad38802ebf0daa3fde76abe3f65400c86bcbb1ec0b3ab883"
SKILLS = {
    "capture-learning", "connect-insights", "design-experiment", "diagnose-failure",
    "evolve-safely", "frame-problem",
    "mission-lead", "model-domain", "prevent-repeat", "session-handoff",
    "shape-feature", "specify-behavior", "verify-work",
}
NAME = "ravalikamaker-skills"
MARKETPLACE = "ravalikamaker"
SEMVER = re.compile(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)(?:\.(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*))*)?(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def validate_package(root: Path) -> list[str]:
    errors = []

    def read(relative):
        path = root / relative
        if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
            errors.append(f"{relative}: package manifests must be regular files inside the package")
            return {}
        try:
            data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
            if not isinstance(data, dict):
                raise ValueError("expected JSON object")
            return data
        except (OSError, UnicodeError, ValueError) as error:
            errors.append(f"{relative}: {error}")
            return {}

    portable = read("plugin.json")
    claude = read(".claude-plugin/plugin.json")
    schema_bytes = SCHEMA.read_bytes()
    if hashlib.sha256(schema_bytes).hexdigest() != SCHEMA_SHA256:
        errors.append("vendored official schema digest mismatch")
    else:
        validator = Draft202012Validator(json.loads(schema_bytes))
        for error in validator.iter_errors(portable):
            errors.append(f"plugin.json: official schema: {error.message}")
    if portable.get("name") != NAME:
        errors.append(f"plugin.json: expected name {NAME}")
    version = portable.get("version")
    if not isinstance(version, str) or not SEMVER.fullmatch(version):
        errors.append("plugin.json: version must be SemVer")
    if portable.get("author") != {"name": MARKETPLACE}:
        errors.append("plugin.json: author must be the public publisher")
    for field in ("description", "repository", "license"):
        if not isinstance(portable.get(field), str) or not portable[field].strip():
            errors.append(f"plugin.json: missing {field}")
    # The compatibility manifest uses default skills/ discovery, like the core.
    expected_claude = {key: value for key, value in portable.items() if key != "$schema"}
    if claude != expected_claude:
        errors.append(".claude-plugin/plugin.json: metadata must match portable manifest; use default skills/ discovery")
    if "extensions" in portable:
        errors.append("plugin.json: this skills-only bundle has no client extensions")

    for relative, host in ((".claude-plugin/marketplace.json", "claude"), (".agents/plugins/marketplace.json", "codex")):
        catalog = read(relative)
        if catalog.get("name") != MARKETPLACE:
            errors.append(f"{relative}: marketplace name must be {MARKETPLACE}")
        entries = catalog.get("plugins")
        if not isinstance(entries, list) or len(entries) != 1 or not isinstance(entries[0], dict):
            errors.append(f"{relative}: expected exactly one plugin entry")
            continue
        entry = entries[0]
        expected = ({"name": NAME, "source": "./", "version": version} if host == "claude" else
                    {"name": NAME, "source": {"source": "local", "path": "./"},
                     "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "category": "Productivity"})
        if entry != expected:
            errors.append(f"{relative}: plugin identity, version, root source ./, or install policy drifted")
        if host == "claude" and catalog.get("owner") != {"name": MARKETPLACE}:
            errors.append(f"{relative}: owner must be the public publisher")

    skills = root / "skills"
    found = {path.name for path in skills.iterdir() if path.is_dir()} if skills.is_dir() else set()
    if found != SKILLS:
        errors.append(f"skills/: expected exactly {', '.join(sorted(SKILLS))}; found {', '.join(sorted(found))}")
    for name in sorted(SKILLS):
        if not (skills / name / "SKILL.md").is_file():
            errors.append(f"skills/{name}/SKILL.md: missing bundled skill")
    for path in [skills, *skills.rglob("*")]:
        if path.is_symlink():
            errors.append(f"{path.relative_to(root)}: bundle must not use symlinks")
    for compatibility in (".claude-plugin", ".agents", ".codex-plugin"):
        if list((root / compatibility).rglob("SKILL.md")):
            errors.append(f"{compatibility}: duplicate or misrouted skills; only root skills/ is published")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    errors = validate_package(parser.parse_args().root)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print(f"Validated portable schema, synchronized host manifests/catalogs, and {len(SKILLS)}-skill bundle; host behavior is untested.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

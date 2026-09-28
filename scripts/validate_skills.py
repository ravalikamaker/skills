#!/usr/bin/env python3
"""Validate published skills with skills-ref and repository integrity checks."""

import argparse
import json
from pathlib import Path
import sys
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt
from skills_ref.validator import validate


def validate_links(directory: Path) -> list[str]:
    """Check local Markdown links, including links in conditional references.

    External URLs and fragment targets are not fetched or anchor-validated.
    Local links must resolve inside the independently installable skill bundle.
    """
    errors = []
    for document in sorted(directory.rglob("*.md")):
        try:
            tokens = MarkdownIt().parse(document.read_text(encoding="utf-8"))
        except (OSError, UnicodeError) as error:
            errors.append(f"cannot read {document.relative_to(directory)}: {error}")
            continue
        for token in tokens:
            for child in token.children or []:
                target = child.attrGet("href") if child.type == "link_open" else (
                    child.attrGet("src") if child.type == "image" else None
                )
                if not target:
                    continue
                url = urlsplit(target)
                if url.scheme or url.netloc or not url.path:
                    continue
                resolved = (document.parent / unquote(url.path)).resolve()
                if not resolved.is_relative_to(directory.resolve()):
                    errors.append(f"{document.relative_to(directory)}: local link escapes skill bundle: {target}")
                elif not resolved.exists():
                    errors.append(f"{document.relative_to(directory)}: missing local link target: {target}")
    return errors


def validate_evals(directory: Path) -> list[str]:
    """Check scenario structure only; this does not execute a model evaluation."""
    path = directory / "evals" / "evals.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as error:
        return [f"cannot read evals/evals.json: {error}"]
    if not isinstance(data, dict) or data.get("skill_name") != directory.name:
        return ["evals/evals.json must name the containing skill in skill_name"]
    cases = data.get("evals")
    if not isinstance(cases, list) or not cases:
        return ["evals/evals.json must contain a nonempty list of behavioral cases"]
    errors, seen = [], set()
    for index, case in enumerate(cases, 1):
        if not isinstance(case, dict):
            errors.append(f"eval case {index} must be an object")
            continue
        identifier = case.get("id")
        if type(identifier) is not int or identifier < 1 or identifier in seen:
            errors.append(f"eval case {index} needs a unique positive integer id")
        else:
            seen.add(identifier)
        for field in ("prompt", "expected_output"):
            if not isinstance(case.get(field), str) or not case[field].strip():
                errors.append(f"eval case {index} needs nonempty {field}")
        if "setup" in case and (not isinstance(case["setup"], str) or not case["setup"].strip()):
            errors.append(f"eval case {index} setup must be a nonempty string")
        files = case.get("files", [])
        if not isinstance(files, list):
            errors.append(f"eval case {index} files must be a list")
        else:
            for filename in files:
                if not isinstance(filename, str) or not filename.strip():
                    errors.append(f"eval case {index} file paths must be nonempty strings")
                    continue
                resolved = (directory / filename).resolve()
                if Path(filename).is_absolute() or not resolved.is_relative_to(directory.resolve()):
                    errors.append(f"eval case {index} file escapes skill bundle: {filename}")
                elif not resolved.is_file():
                    errors.append(f"eval case {index} missing fixture file: {filename}")
        assertions = case.get("assertions")
        if not isinstance(assertions, list) or not assertions or any(
            not isinstance(value, str) or not value.strip() for value in assertions
        ):
            errors.append(f"eval case {index} needs nonempty string assertions")
    return errors


def validate_skill(directory: Path) -> list[str]:
    document = directory / "SKILL.md"
    if not document.is_file():
        return ["missing SKILL.md"]
    try:
        content = document.read_text(encoding="utf-8")
        errors = validate(directory)
    except (OSError, UnicodeError, TypeError, AttributeError) as error:
        return [f"cannot validate SKILL.md: {error}"]
    # Repository conventions supplement (rather than replace) the official spec.
    lines = content.splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        errors.append("frontmatter delimiters must occupy their own lines")
    else:
        end = lines.index("---", 1)
        if not "\n".join(lines[end + 1:]).strip():
            errors.append("instruction body must not be empty")
    errors.extend(validate_links(directory))
    errors.extend(validate_evals(directory))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path,
                        default=Path(__file__).resolve().parents[1] / "skills",
                        help="published skills directory (default: repository skills/)")
    root = parser.parse_args().root
    if not root.is_dir():
        print(f"ERROR: skills directory does not exist: {root}", file=sys.stderr)
        return 1
    directories = sorted(path for path in root.iterdir() if path.is_dir() and not path.name.startswith("."))
    if not directories:
        print("No published skills found.", file=sys.stderr)
        return 1
    failed = False
    for directory in directories:
        errors = validate_skill(directory)
        for error in errors:
            print(f"ERROR: {directory.name}: {error}", file=sys.stderr)
        failed = failed or bool(errors)
    if failed:
        return 1
    print(f"Validated {len(directories)} skill(s): official spec, local links, and eval structure; host behavior is untested.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

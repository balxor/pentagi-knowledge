#!/usr/bin/env python3
"""
Validate tooling overlay Markdown frontmatter.

Checks every tooling/*/*.md file for the metadata contract documented in
``tooling/README.md`` and used by PentAGI import helpers.
"""
import argparse
import re
import sys
from pathlib import Path

ID_RE = re.compile(r"^(T\d+(?:\.\d+)?|CAPEC-\d+|CWE-\d+)__.+\.md$")
ATTACK_ID_RE = re.compile(r"^T\d+(?:\.\d+)?$")
RELATED_ID_RE = re.compile(r"^(T\d+(?:\.\d+)?|CAPEC-\d+|CWE-\d+)$")
REQUIRED_COMMON = {
    "name",
    "type",
    "target_type",
    "related_attack_ids",
    "risk_level",
    "usage",
    "tags",
}
REQUIRED_ATTACK = {"attack_id", "tactics", "platforms", "attack_ref"}
VALID_TARGET_TYPES = {"technique", "sub-technique", "tactic", "weakness", "attack-pattern"}
VALID_RISK_LEVELS = {"low", "medium", "high"}
VALID_USAGE = {"authorized-lab-only"}
LIST_FIELDS = {"tactics", "platforms", "related_attack_ids", "tags"}


def parse_list(raw):
    raw = raw.strip()
    if not (raw.startswith("[") and raw.endswith("]")):
        return None
    inner = raw[1:-1].strip()
    if not inner:
        return []
    return [item.strip() for item in inner.split(",")]


def parse_frontmatter(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening frontmatter delimiter")
    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration as exc:
        raise ValueError("missing closing frontmatter delimiter") from exc
    data = {}
    for lineno, line in enumerate(lines[1:end], 2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line {lineno}: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            raise ValueError(f"empty frontmatter key on line {lineno}")
        data[key] = value
    body = lines[end + 1 :]
    return data, body


def expected_attack_ref(attack_id):
    if "." in attack_id:
        parent, child = attack_id.split(".", 1)
        return f"https://attack.mitre.org/techniques/{parent}/{child}"
    return f"https://attack.mitre.org/techniques/{attack_id}"


def validate_file(path):
    errors = []
    m = ID_RE.match(path.name)
    file_id = m.group(1) if m else None
    if not file_id:
        errors.append("filename must start with T####, T####.###, CAPEC-###, or CWE-### followed by __")

    try:
        meta, body = parse_frontmatter(path)
    except ValueError as exc:
        return [str(exc)]

    required = set(REQUIRED_COMMON)
    if file_id and ATTACK_ID_RE.match(file_id):
        required |= REQUIRED_ATTACK
    missing = sorted(key for key in required if key not in meta or meta[key] == "")
    for key in missing:
        errors.append(f"missing required field: {key}")

    for key in LIST_FIELDS & meta.keys():
        values = parse_list(meta[key])
        if values is None:
            errors.append(f"{key} must use inline list syntax, e.g. [item, item]")
        elif any(not item for item in values):
            errors.append(f"{key} contains an empty item")

    if meta.get("type") != "tooling":
        errors.append("type must be tooling")
    if meta.get("target_type") and meta["target_type"] not in VALID_TARGET_TYPES:
        errors.append(f"target_type must be one of: {', '.join(sorted(VALID_TARGET_TYPES))}")
    if meta.get("risk_level") and meta["risk_level"] not in VALID_RISK_LEVELS:
        errors.append(f"risk_level must be one of: {', '.join(sorted(VALID_RISK_LEVELS))}")
    if meta.get("usage") and meta["usage"] not in VALID_USAGE:
        errors.append("usage must be authorized-lab-only")

    if file_id and ATTACK_ID_RE.match(file_id):
        attack_id = meta.get("attack_id")
        if attack_id != file_id:
            errors.append(f"attack_id must match filename id {file_id}")
        ref = meta.get("attack_ref")
        expected_ref = expected_attack_ref(file_id)
        if ref and ref != expected_ref:
            errors.append(f"attack_ref must be {expected_ref}")

    related = parse_list(meta.get("related_attack_ids", "[]"))
    if related is not None:
        for item in related:
            if not RELATED_ID_RE.match(item):
                errors.append(f"related_attack_ids contains invalid id: {item}")

    tags = parse_list(meta.get("tags", "[]"))
    if tags is not None:
        if "tooling" not in tags:
            errors.append("tags must include tooling")
        if file_id and file_id not in tags:
            errors.append(f"tags must include {file_id}")

    first_heading = next((line for line in body if line.startswith("# ")), "")
    if file_id and first_heading and file_id not in first_heading:
        errors.append(f"first heading should include {file_id}")

    return errors


def iter_tooling_files(root):
    tooling = root / "tooling"
    return sorted(path for path in tooling.glob("*/*.md") if path.is_file())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="repository root (default: .)")
    args = parser.parse_args()

    root = Path(args.root)
    files = iter_tooling_files(root)
    if not files:
        print("[i] no tooling markdown files found")
        return 0

    failures = 0
    for path in files:
        errors = validate_file(path)
        if errors:
            failures += 1
            rel = path.relative_to(root).as_posix()
            print(f"[!] {rel}")
            for error in errors:
                print(f"    - {error}")

    if failures:
        print(f"[x] {failures}/{len(files)} tooling file(s) failed validation")
        return 1

    print(f"[+] validated {len(files)} tooling file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

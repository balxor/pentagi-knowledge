#!/usr/bin/env python3
"""
update_tracking_status.py
=========================
Keep TRACKING.md in sync with reality. Scans the tooling/ folder, then ticks each
checkbox in TRACKING.md whose technique/pattern/weakness ID has a tooling file -
and unticks the ones that don't. No more hand-maintained checkboxes.

Status is derived from files, so the tracker can never drift from what actually
exists.

USAGE
-----
    # report only (no changes)
    python tools/update_tracking_status.py --check

    # rewrite TRACKING.md in place with correct checkboxes + file paths
    python tools/update_tracking_status.py

Recognises IDs of the form T1059, T1059.001, CAPEC-135, CWE-134.

Author: Kenshin Himura of DTrust
"""
import argparse, glob, os, re, sys

__author__ = "Kenshin Himura of DTrust"

ID_RE = re.compile(r"^(?P<pre>\s*[-*]\s*\[)(?P<box>[ xX])(?P<mid>\]\s+)"
                   r"(?P<id>T\d+(?:\.\d+)?|CAPEC-\d+|CWE-\d+)(?P<rest>.*)$")
TRAIL_PATH = re.compile(r"\s*\((?:\./)?tooling/[^)]+\)\s*$")


def index_tooling(root):
    """Map ID -> repo-relative path for every file in tooling/**."""
    found = {}
    for f in glob.glob(os.path.join(root, "tooling", "*", "*.md")):
        base = os.path.basename(f)
        m = re.match(r"(T\d+(?:\.\d+)?|CAPEC-\d+|CWE-\d+)__", base)
        if m:
            rel = os.path.relpath(f, root).replace(os.sep, "/")
            found[m.group(1)] = rel
    return found


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".", help="repo root (default: .)")
    ap.add_argument("--tracking", default="TRACKING.md")
    ap.add_argument("--check", action="store_true", help="report only, do not write")
    args = ap.parse_args()

    tracking = os.path.join(args.root, args.tracking)
    if not os.path.exists(tracking):
        sys.exit(f"[!] {tracking} not found")

    have = index_tooling(args.root)
    lines = open(tracking, encoding="utf-8").read().splitlines()

    total = done = flipped = 0
    out = []
    for ln in lines:
        m = ID_RE.match(ln)
        if not m:
            out.append(ln)
            continue
        total += 1
        tid = m.group("id")
        rest = TRAIL_PATH.sub("", m.group("rest"))  # strip any old path note
        if tid in have:
            done += 1
            newbox = "x"
            rest = rest.rstrip() + f" ({have[tid]})"
        else:
            newbox = " "
        if newbox != m.group("box"):
            flipped += 1
        out.append(f"{m.group('pre')}{newbox}{m.group('mid')}{tid}{rest}")

    print(f"[i] tooling files found: {len(have)}")
    print(f"[i] checkbox items: {total} | done: {done} | todo: {total - done} | "
          f"would change: {flipped}")
    if args.check:
        print("[i] --check: no files written")
        return
    open(tracking, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"[+] Updated {tracking}")


if __name__ == "__main__":
    main()

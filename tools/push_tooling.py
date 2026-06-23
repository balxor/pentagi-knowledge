#!/usr/bin/env python3
"""
Push tooling overlay .md files into PentAGI Knowledges via GraphQL.

Usage:
    python tools/push_tooling.py --dir tooling/enterprise --pentagi-url https://localhost:8443 --token "$PENTAGI_API_TOKEN"

Author: Kenshin Himura of DTrust
"""

import argparse
import json
import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("requests not installed. Run: pip install requests")
    sys.exit(1)


def send_document(url: str, token: str, title: str, content: str, source: str) -> bool:
    query = """
    mutation($input: CreateKnowledgeDocumentInput!) {
        createKnowledgeDocument(input: $input) { id }
    }
    """
    variables = {
        "input": {
            "title": title,
            "docType": "guide",
            "guideType": "pentest",
            "question": title,
            "content": content,
            "source": source,
            "tags": ["tooling"],
        }
    }
    payload = {"query": query.strip(), "variables": variables}
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    try:
        r = requests.post(
            f"{url.rstrip('/')}/api/v1/graphql",
            json=payload,
            headers=headers,
            verify=False,
            timeout=30,
        )
        r.raise_for_status()
        return True
    except requests.RequestException as e:
        print(f"  FAILED: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="Push tooling overlays to PentAGI")
    parser.add_argument("--dir", required=True, help="Directory with .md files")
    parser.add_argument("--pentagi-url", required=True, help="PentAGI base URL")
    parser.add_argument("--token", required=True, help="PentAGI API bearer token")
    args = parser.parse_args()

    target_dir = Path(args.dir)
    if not target_dir.is_dir():
        print(f"Directory not found: {target_dir}", file=sys.stderr)
        sys.exit(1)

    try:
        rel = target_dir.relative_to(Path.cwd())
    except ValueError:
        rel = target_dir
    source_label = f"pentagi-knowledge/{rel.as_posix()}"

    md_files = sorted(target_dir.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {target_dir}")
        sys.exit(0)

    ok = 0
    fail = 0
    for fp in md_files:
        title = fp.stem
        print(f"Pushing {fp.name} ...", end="")
        content = fp.read_text(encoding="utf-8")
        if send_document(args.pentagi_url, args.token, title, content, source_label):
            print(" OK")
            ok += 1
        else:
            print(" FAIL")
            fail += 1

    print(f"\nDone: {ok} pushed, {fail} failed")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Push tooling overlay .md files into PentAGI Knowledges via GraphQL.

Usage:
    python tools/push_tooling.py --dir tooling/enterprise --pentagi-url https://localhost:8443 --token "$PENTAGI_API_TOKEN"

Author: Kenshin Himura of DTrust
"""

import argparse
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("requests not installed. Run: pip install -r requirements.txt")
    sys.exit(1)


def send_document(url: str, token: str, title: str, content: str,
                  description: str, insecure: bool) -> bool:
    query = """
    mutation($input: CreateKnowledgeDocumentInput!) {
        createKnowledgeDocument(input: $input) { id }
    }
    """
    variables = {
        "input": {
            "docType": "code",
            "codeLang": "markdown",
            "question": title,
            "content": content,
            "description": description,
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
            verify=not insecure,
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
    parser.add_argument("--insecure", action="store_true",
                        help="skip TLS certificate verification for local self-signed PentAGI")
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
        description = f"Tooling overlay from {source_label}/{fp.name}"
        if send_document(args.pentagi_url, args.token, title, content,
                         description, args.insecure):
            print(" OK")
            ok += 1
        else:
            print(" FAIL")
            fail += 1

    print(f"\nDone: {ok} pushed, {fail} failed")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
build_capec_knowledge.py
========================
Generate one Markdown knowledge file per MITRE CAPEC attack pattern, formatted
for import into PentAGI "Knowledges" (pgvector semantic search). CAPEC describes
*how* weaknesses are attacked (format-string injection, buffer overflow, etc.)
and cross-references CWE and ATT&CK.

Source: official CAPEC STIX 2.1 from the mitre/cti repository.

USAGE
-----
    python build_capec_knowledge.py --out ./mitre/capec
    python build_capec_knowledge.py --stix ./stix-capec.json --out ./mitre/capec
    python build_capec_knowledge.py --out ./mitre/capec \
        --push --pentagi-url https://localhost:8443 --token "$PENTAGI_API_TOKEN"

CAPEC is free to use with attribution to The MITRE Corporation.
Only run resulting attack flows against systems you are authorized to test.

Author: Kenshin Himura of DTrust
"""
import argparse, datetime, json, os, re, sys, textwrap, urllib.request

__author__ = "Kenshin Himura of DTrust"

CAPEC_STIX = ("https://raw.githubusercontent.com/mitre/cti/master/"
              "capec/2.1/stix-capec.json")


def load_stix(stix_path=None):
    if stix_path:
        with open(stix_path, encoding="utf-8") as fh:
            return json.load(fh)
    print(f"[*] Downloading official CAPEC STIX from {CAPEC_STIX} ...", file=sys.stderr)
    with urllib.request.urlopen(CAPEC_STIX, timeout=300) as resp:
        return json.loads(resp.read().decode("utf-8"))


def slug(text):
    s = re.sub(r"[^a-zA-Z0-9]+", "-", (text or "").lower()).strip("-")
    return s[:80] or "item"


def strip_html(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    return re.sub(r"\s+", " ", s).strip()


def ext_id(obj, source):
    for ref in obj.get("external_references", []) or []:
        if ref.get("source_name") == source:
            return ref.get("external_id"), ref.get("url")
    return None, None


def related_ids(obj, source):
    out = []
    for ref in obj.get("external_references", []) or []:
        if ref.get("source_name") == source and ref.get("external_id"):
            out.append(ref["external_id"])
    return out


def parse(bundle):
    patterns, coa, rels = {}, {}, []
    for o in bundle.get("objects", []):
        t = o.get("type")
        if o.get("revoked") or o.get("x_mitre_deprecated") or o.get("x_capec_status") == "Deprecated":
            continue
        if t == "attack-pattern":
            cid, url = ext_id(o, "capec")
            if cid:
                patterns[cid] = {"obj": o, "url": url}
        elif t == "course-of-action":
            coa[o["id"]] = o
        elif t == "relationship":
            rels.append(o)
    stix2cid = {v["obj"]["id"]: k for k, v in patterns.items()}
    mit_for = {}
    for r in rels:
        if r.get("relationship_type") == "mitigates":
            tgt, src = r.get("target_ref", ""), r.get("source_ref", "")
            if tgt in stix2cid and src in coa:
                mit_for.setdefault(stix2cid[tgt], []).append(coa[src])
    return patterns, mit_for


def yaml_scalar(value):
    """Return a YAML-safe double-quoted scalar."""
    return json.dumps(str(value), ensure_ascii=False)


def yaml_list(items):
    return "[" + ", ".join(yaml_scalar(item) for item in items) + "]" if items else "[]"


def md_pattern(cid, rec, mit_for):
    o = rec["obj"]
    name = o.get("name", "")
    desc = (o.get("description") or "").strip()
    ext = strip_html(o.get("x_capec_extended_description", ""))
    abstraction = o.get("x_capec_abstraction", "")
    status = o.get("x_capec_status", "")
    severity = o.get("x_capec_typical_severity", "")
    likelihood = o.get("x_capec_likelihood_of_attack", "")
    prereq = o.get("x_capec_prerequisites", []) or []
    skills = o.get("x_capec_skills_required", {}) or {}
    resources = o.get("x_capec_resources_required", []) or []
    consequences = o.get("x_capec_consequences", {}) or {}
    flow = strip_html(o.get("x_capec_execution_flow", ""))
    rel_cwe = related_ids(o, "cwe")
    rel_attack = related_ids(o, "ATTACK")
    mits = mit_for.get(cid, [])

    fm = textwrap.dedent(f"""\
        ---
        capec_id: {cid}
        name: {yaml_scalar(name)}
        type: attack-pattern
        abstraction: {yaml_scalar(abstraction or 'n/a')}
        likelihood: {yaml_scalar(likelihood or 'n/a')}
        severity: {yaml_scalar(severity or 'n/a')}
        related_cwe: {yaml_list(rel_cwe)}
        related_attack: {yaml_list(rel_attack)}
        url: {rec['url']}
        tags: [mitre-capec, attack-pattern, {cid}]
        ---
        """)
    body = f"# {cid} - {name}\n\n"
    body += (f"**Abstraction:** {abstraction or 'n/a'}  -  **Likelihood:** {likelihood or 'n/a'}"
             f"  -  **Severity:** {severity or 'n/a'}  -  **CAPEC:** [{cid}]({rec['url']})\n\n")
    body += "## Description\n" + (desc or "_No description._") + "\n\n"
    if ext:
        body += "## Extended description\n" + ext + "\n\n"
    if prereq:
        body += "## Prerequisites\n" + "\n".join(f"- {strip_html(p)}" for p in prereq) + "\n\n"
    if skills:
        body += "## Skills required\n"
        if isinstance(skills, dict):
            for lvl, d in skills.items():
                body += f"- **{lvl}**: {strip_html(d)}\n"
        else:
            for s in skills:
                body += f"- {strip_html(str(s))}\n"
        body += "\n"
    if resources:
        body += "## Resources required\n" + "\n".join(f"- {strip_html(r)}" for r in resources) + "\n\n"
    if consequences:
        body += "## Consequences\n"
        if isinstance(consequences, dict):
            for scope, impacts in consequences.items():
                imp = ", ".join(impacts) if isinstance(impacts, list) else str(impacts)
                body += f"- **{scope}**: {imp}\n"
        else:
            for c in consequences:
                body += f"- {strip_html(str(c))}\n"
        body += "\n"
    if flow:
        body += "## Execution flow\n" + flow + "\n\n"
    if mits:
        body += "## Mitigations\n"
        for m in mits:
            body += f"- {strip_html(m.get('description',''))}\n"
        body += "\n"
    if rel_cwe:
        body += "## Related weaknesses (CWE)\n" + \
                "\n".join(f"- [{c}](https://cwe.mitre.org/data/definitions/{c.split('-')[1]}.html)"
                          for c in rel_cwe) + "\n\n"
    if rel_attack:
        body += "## Related ATT&CK techniques\n" + "\n".join(f"- {a}" for a in rel_attack) + "\n\n"
    body += f"Source: MITRE CAPEC - {rec['url']}\n"
    return fm + "\n" + body


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stix", help="path to a local stix-capec.json")
    ap.add_argument("--out", default="./mitre/capec", help="output dir")
    ap.add_argument("--version", default="latest", help="CAPEC version label for manifest")
    ap.add_argument("--push", action="store_true")
    ap.add_argument("--filter", help="only push files whose name contains this substring "
                    "(e.g. CWE-119); avoids re-pushing everything")
    ap.add_argument("--pentagi-url", default="https://localhost:8443")
    ap.add_argument("--token", default=os.environ.get("PENTAGI_API_TOKEN", ""))
    ap.add_argument("--insecure", action="store_true",
                    help="skip TLS certificate verification for local self-signed PentAGI")
    args = ap.parse_args()

    bundle = load_stix(args.stix)
    patterns, mit_for = parse(bundle)
    # capture version if present
    ver = args.version
    if ver == "latest":
        for o in bundle.get("objects", []):
            if o.get("x_capec_version"):
                ver = "v" + str(o["x_capec_version"]); break

    os.makedirs(os.path.join(args.out, "patterns"), exist_ok=True)
    written = []
    for cid in sorted(patterns, key=lambda c: int(c.split("-")[1])):
        rec = patterns[cid]
        path = os.path.join(args.out, "patterns", f"{cid}__{slug(rec['obj'].get('name'))}.md")
        open(path, "w", encoding="utf-8").write(md_pattern(cid, rec, mit_for))
        written.append(path)

    with open(os.path.join(args.out, "INDEX.md"), "w", encoding="utf-8") as fh:
        fh.write("# MITRE CAPEC - Knowledge Index\n\n")
        fh.write(f"Attack patterns: {len(patterns)}\n\n")
        for cid in sorted(patterns, key=lambda c: int(c.split("-")[1])):
            fh.write(f"- [{cid}](https://capec.mitre.org/data/definitions/{cid.split('-')[1]}.html) "
                     f"{patterns[cid]['obj'].get('name','')}\n")

    manifest = {
        "source": "MITRE CAPEC", "framework": "capec",
        "capec_version": ver if ver != "latest" else "latest",
        "stix_source": CAPEC_STIX, "generated_at": datetime.date.today().isoformat(),
        "generator": "tools/build_capec_knowledge.py",
        "counts": {"attack_patterns": len(patterns)},
        "format": "one markdown file per attack pattern, YAML frontmatter + structured body",
        "target": "PentAGI Knowledges (pgvector semantic search)",
    }
    json.dump(manifest, open(os.path.join(args.out, "manifest.json"), "w", encoding="utf-8"), indent=2)
    print(f"[+] Wrote {len(written)} CAPEC files to {args.out}")
    if args.push:
        to_push = [f for f in written if args.filter in os.path.basename(f)] if args.filter else written
        print(f"[*] Pushing {len(to_push)} file(s)" + (f" matching '{args.filter}'" if args.filter else ""))
        push_to_pentagi(to_push, args.pentagi_url, args.token, args.insecure)


def push_to_pentagi(files, url, token, insecure=False):
    """Create one Knowledge document per markdown file (docType=guide, guideType=pentest)."""
    import json as _json, ssl
    endpoint = url.rstrip("/") + "/api/v1/graphql"
    ctx = ssl.create_default_context()
    if insecure:
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
    MUT = ("mutation($input: CreateKnowledgeDocumentInput!){"
           "createKnowledgeDocument(input: $input){ id }}")
    ok = 0
    for f in files:
        content = open(f, encoding="utf-8").read()
        m = re.search(r'^#\s+(.+)$', content, re.M)
        question = m.group(1).strip() if m else os.path.splitext(os.path.basename(f))[0]
        variables = {"input": {"docType": "guide", "guideType": "pentest",
                               "question": question, "content": content, "description": question}}
        payload = _json.dumps({"query": MUT, "variables": variables}).encode()
        req = urllib.request.Request(endpoint, data=payload, method="POST",
                                     headers={"Content-Type": "application/json",
                                              "Authorization": f"Bearer {token}"})
        try:
            data = _json.loads(urllib.request.urlopen(req, timeout=30, context=ctx).read())
            if data.get("errors"):
                print(f"[!] {question}: {data['errors'][0].get('message')}", file=sys.stderr)
            else:
                ok += 1
        except Exception as e:
            print(f"[!] push failed for {question}: {e}", file=sys.stderr)
    print(f"[+] Pushed {ok}/{len(files)} knowledge docs to {endpoint}")


if __name__ == "__main__":
    main()

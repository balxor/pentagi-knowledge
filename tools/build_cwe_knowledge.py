#!/usr/bin/env python3
"""
build_cwe_knowledge.py
======================
Generate one Markdown knowledge file per MITRE CWE weakness, formatted for import
into PentAGI "Knowledges" (pgvector semantic search). CWE catalogues *weakness
classes* - format string (CWE-134), buffer overflow (CWE-120/121/122/787), etc.

Source: official CWE XML (cwec_latest.xml.zip) from cwe.mitre.org.

USAGE
-----
    python build_cwe_knowledge.py --out ./mitre/cwe
    python build_cwe_knowledge.py --xml ./cwec_latest.xml.zip --out ./mitre/cwe
    python build_cwe_knowledge.py --out ./mitre/cwe \
        --push --pentagi-url https://localhost:8443 --token "$PENTAGI_API_TOKEN"

CWE is free to use with attribution to The MITRE Corporation.

Author: Kenshin Himura of DTrust
"""
import argparse, datetime, io, json, os, re, sys, textwrap, urllib.request, zipfile
import xml.etree.ElementTree as ET

__author__ = "Kenshin Himura of DTrust"

CWE_ZIP = "https://cwe.mitre.org/data/xml/cwec_latest.xml.zip"


def load_xml(xml_path=None):
    """Return the root Element of the CWE catalog from a local file/zip or download."""
    if xml_path:
        data = open(xml_path, "rb").read()
    else:
        print(f"[*] Downloading official CWE XML from {CWE_ZIP} ...", file=sys.stderr)
        data = urllib.request.urlopen(CWE_ZIP, timeout=300).read()
    if data[:2] == b"PK":  # zip
        zf = zipfile.ZipFile(io.BytesIO(data))
        name = next(n for n in zf.namelist() if n.endswith(".xml"))
        data = zf.read(name)
    return ET.fromstring(data)


def ln(tag):
    """local name without namespace"""
    return tag.split("}")[-1]


def find(el, name):
    for c in el:
        if ln(c.tag) == name:
            return c
    return None


def findall(el, name):
    return [c for c in el if ln(c.tag) == name]


def text_of(el):
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip() if el is not None else ""


def slug(text):
    s = re.sub(r"[^a-zA-Z0-9]+", "-", (text or "").lower()).strip("-")
    return s[:80] or "item"


def yaml_list(items):
    return "[" + ", ".join(items) + "]" if items else "[]"


def parse(root):
    weaknesses = {}
    catalog_version = root.attrib.get("Version", "")
    for group in root:
        if ln(group.tag) != "Weaknesses":
            continue
        for w in findall(group, "Weakness"):
            if w.attrib.get("Status") == "Deprecated":
                continue
            wid = "CWE-" + w.attrib.get("ID", "")
            weaknesses[wid] = w
    return weaknesses, catalog_version


def md_weakness(wid, w):
    name = w.attrib.get("Name", "")
    abstraction = w.attrib.get("Abstraction", "")
    status = w.attrib.get("Status", "")
    num = wid.split("-")[1]
    url = f"https://cwe.mitre.org/data/definitions/{num}.html"
    desc = text_of(find(w, "Description"))
    ext = text_of(find(w, "Extended_Description"))

    langs = []
    ap = find(w, "Applicable_Platforms")
    if ap is not None:
        for el in ap:
            if ln(el.tag) in ("Language", "Technology", "Operating_System", "Architecture"):
                nm = el.attrib.get("Name") or el.attrib.get("Class")
                if nm:
                    langs.append(nm)

    rel_cwe, rel_capec = [], []
    rw = find(w, "Related_Weaknesses")
    if rw is not None:
        for r in findall(rw, "Related_Weakness"):
            cid = r.attrib.get("CWE_ID")
            if cid:
                rel_cwe.append(f"CWE-{cid} ({r.attrib.get('Nature','')})")
    rap = find(w, "Related_Attack_Patterns")
    if rap is not None:
        for r in findall(rap, "Related_Attack_Pattern"):
            cid = r.attrib.get("CAPEC_ID")
            if cid:
                rel_capec.append(f"CAPEC-{cid}")

    consequences = []
    cc = find(w, "Common_Consequences")
    if cc is not None:
        for c in findall(cc, "Consequence"):
            scopes = ", ".join(text_of(s) for s in findall(c, "Scope"))
            impacts = ", ".join(text_of(i) for i in findall(c, "Impact"))
            consequences.append((scopes, impacts))

    mitigations = []
    pm = find(w, "Potential_Mitigations")
    if pm is not None:
        for m in findall(pm, "Mitigation"):
            phase = ", ".join(text_of(p) for p in findall(m, "Phase"))
            d = text_of(find(m, "Description"))
            mitigations.append((phase, d))

    observed = []
    oe = find(w, "Observed_Examples")
    if oe is not None:
        for o in findall(oe, "Observed_Example"):
            ref = text_of(find(o, "Reference"))
            d = text_of(find(o, "Description"))
            observed.append((ref, d))

    fm = textwrap.dedent(f"""\
        ---
        cwe_id: {wid}
        name: {name}
        type: weakness
        abstraction: {abstraction or 'n/a'}
        status: {status or 'n/a'}
        languages: {yaml_list(langs)}
        related_capec: {yaml_list(rel_capec)}
        url: {url}
        tags: [mitre-cwe, weakness, {wid}]
        ---
        """)
    body = f"# {wid} - {name}\n\n"
    body += f"**Abstraction:** {abstraction or 'n/a'}  -  **Status:** {status or 'n/a'}  -  **CWE:** [{wid}]({url})\n\n"
    body += "## Description\n" + (desc or "_No description._") + "\n\n"
    if ext:
        body += "## Extended description\n" + ext + "\n\n"
    if langs:
        body += "## Applicable platforms / languages\n" + ", ".join(langs) + "\n\n"
    if consequences:
        body += "## Common consequences\n"
        for sc, im in consequences:
            body += f"- **{sc or 'n/a'}**: {im or 'n/a'}\n"
        body += "\n"
    if mitigations:
        body += "## Potential mitigations\n"
        for ph, d in mitigations:
            body += f"- **{ph or 'general'}**: {d}\n"
        body += "\n"
    if rel_capec:
        body += "## Related attack patterns (CAPEC)\n" + \
                "\n".join(f"- [{c}](https://capec.mitre.org/data/definitions/{c.split('-')[1]}.html)"
                          for c in rel_capec) + "\n\n"
    if rel_cwe:
        body += "## Related weaknesses\n" + "\n".join(f"- {c}" for c in rel_cwe) + "\n\n"
    if observed:
        body += "## Observed examples (CVE)\n"
        for ref, d in observed[:15]:
            body += f"- **{ref}**: {d}\n"
        body += "\n"
    body += f"Source: MITRE CWE - {url}\n"
    return fm + "\n" + body


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--xml", help="path to a local cwec_*.xml or cwec_latest.xml.zip")
    ap.add_argument("--out", default="./mitre/cwe", help="output dir")
    ap.add_argument("--version", default="latest", help="CWE version label for manifest")
    ap.add_argument("--push", action="store_true")
    ap.add_argument("--filter", help="only push files whose name contains this substring "
                    "(e.g. CWE-119); avoids re-pushing everything")
    ap.add_argument("--pentagi-url", default="https://localhost:8443")
    ap.add_argument("--token", default=os.environ.get("PENTAGI_API_TOKEN", ""))
    args = ap.parse_args()

    root = load_xml(args.xml)
    weaknesses, cat_ver = parse(root)
    ver = args.version if args.version != "latest" else ("v" + cat_ver if cat_ver else "latest")

    os.makedirs(os.path.join(args.out, "weaknesses"), exist_ok=True)
    written = []
    for wid in sorted(weaknesses, key=lambda c: int(c.split("-")[1])):
        w = weaknesses[wid]
        path = os.path.join(args.out, "weaknesses", f"{wid}__{slug(w.attrib.get('Name'))}.md")
        open(path, "w", encoding="utf-8").write(md_weakness(wid, w))
        written.append(path)

    with open(os.path.join(args.out, "INDEX.md"), "w", encoding="utf-8") as fh:
        fh.write("# MITRE CWE - Knowledge Index\n\n")
        fh.write(f"Weaknesses: {len(weaknesses)}\n\n")
        for wid in sorted(weaknesses, key=lambda c: int(c.split("-")[1])):
            num = wid.split("-")[1]
            fh.write(f"- [{wid}](https://cwe.mitre.org/data/definitions/{num}.html) "
                     f"{weaknesses[wid].attrib.get('Name','')}\n")

    manifest = {
        "source": "MITRE CWE", "framework": "cwe",
        "cwe_version": ver, "xml_source": CWE_ZIP,
        "generated_at": datetime.date.today().isoformat(),
        "generator": "tools/build_cwe_knowledge.py",
        "counts": {"weaknesses": len(weaknesses)},
        "format": "one markdown file per weakness, YAML frontmatter + structured body",
        "target": "PentAGI Knowledges (pgvector semantic search)",
    }
    json.dump(manifest, open(os.path.join(args.out, "manifest.json"), "w", encoding="utf-8"), indent=2)
    print(f"[+] Wrote {len(written)} CWE files to {args.out}")
    if args.push:
        to_push = [f for f in written if args.filter in os.path.basename(f)] if args.filter else written
        print(f"[*] Pushing {len(to_push)} file(s)" + (f" matching '{args.filter}'" if args.filter else ""))
        push_to_pentagi(to_push, args.pentagi_url, args.token)


def push_to_pentagi(files, url, token):
    """Create one Knowledge document per markdown file (docType=answer, answerType=vulnerability)."""
    import json as _json, ssl
    endpoint = url.rstrip("/") + "/api/v1/graphql"
    ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
    MUT = ("mutation($input: CreateKnowledgeDocumentInput!){"
           "createKnowledgeDocument(input: $input){ id }}")
    ok = 0
    for f in files:
        content = open(f, encoding="utf-8").read()
        m = re.search(r'^#\s+(.+)$', content, re.M)
        question = m.group(1).strip() if m else os.path.splitext(os.path.basename(f))[0]
        variables = {"input": {"docType": "answer", "answerType": "vulnerability",
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

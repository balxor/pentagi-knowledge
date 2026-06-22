#!/usr/bin/env python3
"""
build_attack_knowledge.py
=========================
Generate one Markdown knowledge file per MITRE ATT&CK (Enterprise) item -
tactic, technique and sub-technique - formatted for import into PentAGI
"Knowledges" (pgvector semantic search) to drive MITRE-ATT&CK-based
automation attack flows.

It pulls the OFFICIAL, current ATT&CK STIX data (so the content is
authoritative and version-correct), then writes:

    out/tactics/TA####__<slug>.md           (15 files)
    out/techniques/T####__<slug>.md          (~222 files)
    out/techniques/T####.###__<slug>.md      (~470 sub-technique files)
    out/INDEX.md                             (full map of every item)

Each file carries YAML frontmatter (machine metadata) + a structured body
optimised for semantic retrieval and for an autonomous agent that plans
attacks phase-by-phase.

USAGE
-----
    pip install mitreattack-python      # preferred (handles the STIX download)
    python build_attack_knowledge.py --out ./attack_knowledge

    # or, without mitreattack-python, fetch the raw STIX yourself:
    #   curl -L -o enterprise-attack.json \
    #     https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack.json
    #   python build_attack_knowledge.py --stix ./enterprise-attack.json --out ./attack_knowledge

    # optional: push straight into PentAGI Knowledges over GraphQL
    #   python build_attack_knowledge.py --out ./attack_knowledge \
    #       --push --pentagi-url https://localhost:8443 --token "$PENTAGI_API_TOKEN"

Note: ATT&CK is freely usable with attribution
(https://attack.mitre.org/resources/legal-and-branding/terms-of-use/).
Only run resulting attack flows against systems you own or are explicitly
authorised to test.

Author: Kenshin Himura of DTrust
"""
import argparse, json, os, re, sys, textwrap, urllib.request

__author__ = "Kenshin Himura of DTrust"

RAW_STIX = ("https://raw.githubusercontent.com/mitre-attack/"
            "attack-stix-data/master/enterprise-attack/enterprise-attack.json")


# ----------------------------------------------------------------------------
# Data loading
# ----------------------------------------------------------------------------
def load_stix(stix_path=None):
    """Return the parsed STIX bundle dict from a local file or a download."""
    if stix_path:
        with open(stix_path, encoding="utf-8") as fh:
            return json.load(fh)
    print(f"[*] Downloading official STIX from {RAW_STIX} ...", file=sys.stderr)
    with urllib.request.urlopen(RAW_STIX, timeout=180) as resp:
        return json.loads(resp.read().decode("utf-8"))


def slug(text):
    s = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return s[:80] or "item"


def attack_id(obj):
    for ref in obj.get("external_references", []):
        if ref.get("source_name") == "mitre-attack":
            return ref.get("external_id"), ref.get("url")
    return None, None


# ----------------------------------------------------------------------------
# Index / parse the bundle
# ----------------------------------------------------------------------------
def parse(bundle):
    objs = bundle["objects"]
    tactics, techniques, mitigations, rels = {}, {}, {}, []
    tactic_by_shortname = {}

    for o in objs:
        t = o.get("type")
        if o.get("revoked") or o.get("x_mitre_deprecated"):
            continue
        if t == "x-mitre-tactic":
            aid, url = attack_id(o)
            tactics[aid] = {"obj": o, "url": url,
                            "shortname": o.get("x_mitre_shortname")}
            tactic_by_shortname[o.get("x_mitre_shortname")] = aid
        elif t == "attack-pattern":
            aid, url = attack_id(o)
            techniques[aid] = {"obj": o, "url": url, "id": aid}
        elif t == "course-of-action":
            aid, url = attack_id(o)
            mitigations[o["id"]] = {"obj": o, "aid": aid, "url": url}
        elif t == "relationship":
            rels.append(o)

    stixid2aid = {v["obj"]["id"]: k for k, v in techniques.items()}

    mit_for = {}
    for r in rels:
        if r.get("relationship_type") == "mitigates":
            tgt, src = r.get("target_ref", ""), r.get("source_ref", "")
            if tgt in stixid2aid and src in mitigations:
                mit_for.setdefault(stixid2aid[tgt], []).append(mitigations[src])

    return tactics, techniques, mit_for, tactic_by_shortname


# ----------------------------------------------------------------------------
# Markdown rendering
# ----------------------------------------------------------------------------
KILLCHAIN_ORDER = [
    "reconnaissance", "resource-development", "initial-access", "execution",
    "persistence", "privilege-escalation", "stealth", "defense-impairment",
    "credential-access", "discovery", "lateral-movement", "collection",
    "command-and-control", "exfiltration", "impact",
]


def yaml_list(items):
    return "[" + ", ".join(items) + "]" if items else "[]"


def md_tactic(aid, t, order, technique_aids):
    o = t["obj"]
    name, desc = o["name"], (o.get("description", "") or "").strip()
    fm = textwrap.dedent(f"""\
        ---
        attack_id: {aid}
        name: {name}
        type: tactic
        shortname: {t['shortname']}
        killchain_order: {order}
        url: {t['url']}
        tags: [mitre-attack, tactic, {t['shortname']}]
        ---
        """)
    body = f"# {aid} - {name} (Tactic)\n\n"
    body += f"> {desc.splitlines()[0] if desc else ''}\n\n"
    body += "## Goal\n" + desc + "\n\n"
    body += ("## Position in the attack flow\n"
             f"Phase {order} of the ATT&CK kill chain. An autonomous agent "
             "selects techniques from this tactic when its current sub-goal "
             "matches the objective above.\n\n")
    body += f"## Techniques in this tactic ({len(technique_aids)})\n"
    for a, n in technique_aids:
        body += f"- [{a}](https://attack.mitre.org/techniques/{a.replace('.', '/')}) {n}\n"
    body += f"\nSource: MITRE ATT&CK - {t['url']}\n"
    return fm + "\n" + body


def md_technique(aid, rec, mit_for, tactics, t_by_sn):
    o = rec["obj"]
    name = o["name"]
    is_sub = bool(o.get("x_mitre_is_subtechnique"))
    parent = aid.split(".")[0] if is_sub else None
    phases = [p["phase_name"] for p in o.get("kill_chain_phases", [])
              if p.get("kill_chain_name") == "mitre-attack"]
    tactic_names = [tactics[t_by_sn[ph]]["obj"]["name"]
                    for ph in phases if ph in t_by_sn]
    platforms = o.get("x_mitre_platforms", []) or []
    data_sources = o.get("x_mitre_data_sources", []) or []
    detection = (o.get("x_mitre_detection") or "").strip()
    desc = (o.get("description") or "").strip()
    mits = mit_for.get(aid, [])

    fm = textwrap.dedent(f"""\
        ---
        attack_id: {aid}
        name: {name}
        type: {"sub-technique" if is_sub else "technique"}
        parent: {parent or "null"}
        tactics: {yaml_list(tactic_names)}
        platforms: {yaml_list(platforms)}
        url: {rec['url']}
        tags: [mitre-attack, {"sub-technique" if is_sub else "technique"}, {aid}]
        ---
        """)
    title = f"# {aid} - {name}"
    title += f" (sub-technique of {parent})\n\n" if is_sub else "\n\n"
    meta = (f"**Tactic(s):** {', '.join(tactic_names) or 'n/a'}  ·  "
            f"**Platforms:** {', '.join(platforms) or 'n/a'}  ·  "
            f"**ATT&CK:** [{aid}]({rec['url']})\n\n")
    body = title + meta
    body += "## Summary\n" + (desc or "_No description in source._") + "\n\n"
    body += ("## Role in the attack flow\n"
             f"Used to achieve the **{', '.join(tactic_names) or 'relevant'}** "
             "objective. An autonomous agent invokes this when its current "
             "sub-goal matches that tactic and the target platform is one of: "
             f"{', '.join(platforms) or 'any'}.\n\n")
    if detection:
        body += "## Detection\n" + detection + "\n\n"
    if data_sources:
        body += "## Data sources\n" + "\n".join(f"- {d}" for d in data_sources) + "\n\n"
    if mits:
        body += "## Mitigations\n"
        for m in mits:
            mo = m["obj"]
            first = (mo.get("description") or "").splitlines()[0] if mo.get("description") else ""
            body += f"- **{m['aid']} {mo['name']}** - {first}\n"
        body += "\n"
    body += f"Source: MITRE ATT&CK - {rec['url']}\n"
    return fm + "\n" + body


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stix", help="path to local enterprise-attack.json")
    ap.add_argument("--out", default="./attack_knowledge", help="output dir")
    ap.add_argument("--push", action="store_true",
                    help="push files into PentAGI Knowledges via GraphQL")
    ap.add_argument("--pentagi-url", default="https://localhost:8443")
    ap.add_argument("--token", default=os.environ.get("PENTAGI_API_TOKEN", ""))
    args = ap.parse_args()

    bundle = load_stix(args.stix)
    tactics, techniques, mit_for, t_by_sn = parse(bundle)

    per_tactic = {sn: [] for sn in t_by_sn}
    for aid, rec in techniques.items():
        if rec["obj"].get("x_mitre_is_subtechnique"):
            continue
        for ph in rec["obj"].get("kill_chain_phases", []):
            if ph.get("kill_chain_name") == "mitre-attack":
                per_tactic.setdefault(ph["phase_name"], []).append((aid, rec["obj"]["name"]))

    os.makedirs(os.path.join(args.out, "tactics"), exist_ok=True)
    os.makedirs(os.path.join(args.out, "techniques"), exist_ok=True)

    written = []
    for sn in KILLCHAIN_ORDER:
        ta = t_by_sn.get(sn)
        if not ta:
            continue
        order = KILLCHAIN_ORDER.index(sn) + 1
        techs = sorted(per_tactic.get(sn, []))
        path = os.path.join(args.out, "tactics",
                            f"{ta}__{slug(tactics[ta]['obj']['name'])}.md")
        open(path, "w", encoding="utf-8").write(md_tactic(ta, tactics[ta], order, techs))
        written.append(path)

    for aid in sorted(techniques):
        rec = techniques[aid]
        path = os.path.join(args.out, "techniques",
                            f"{aid}__{slug(rec['obj']['name'])}.md")
        open(path, "w", encoding="utf-8").write(
            md_technique(aid, rec, mit_for, tactics, t_by_sn))
        written.append(path)

    with open(os.path.join(args.out, "INDEX.md"), "w", encoding="utf-8") as fh:
        fh.write("# MITRE ATT&CK Enterprise - Knowledge Index\n\n")
        fh.write(f"Tactics: {len(tactics)} · Techniques+sub: {len(techniques)} · "
                 f"Total files: {len(written)}\n\n")
        for sn in KILLCHAIN_ORDER:
            ta = t_by_sn.get(sn)
            if not ta:
                continue
            fh.write(f"## {ta} {tactics[ta]['obj']['name']}\n")
            for a, n in sorted(per_tactic.get(sn, [])):
                fh.write(f"- {a} {n}\n")
            fh.write("\n")

    print(f"[+] Wrote {len(written)} markdown files to {args.out}")
    if args.push:
        push_to_pentagi(written, args.pentagi_url, args.token)


def push_to_pentagi(files, url, token):
    """Create one Knowledge document per markdown file via PentAGI GraphQL."""
    import json as _json, ssl, re
    endpoint = url.rstrip("/") + "/api/v1/graphql"
    # PentAGI lokal pakai sertifikat self-signed -> lewati verifikasi TLS
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    MUT = ("mutation($input: CreateKnowledgeDocumentInput!){"
           "createKnowledgeDocument(input: $input){ id }}")
    ok = 0
    for f in files:
        content = open(f, encoding="utf-8").read()
        # 'question' = judul H1 markdown (mis. "T1059 - Command and Scripting Interpreter")
        m = re.search(r'^#\s+(.+)$', content, re.M)
        question = m.group(1).strip() if m else os.path.splitext(os.path.basename(f))[0]
        variables = {"input": {
            "docType":     "guide",     # ATT&CK = panduan
            "guideType":   "pentest",   # sub-tipe pentest
            "question":    question,     # dipakai untuk pencarian semantik
            "content":     content,
            "description": question,
        }}
        payload = _json.dumps({"query": MUT, "variables": variables}).encode()
        req = urllib.request.Request(endpoint, data=payload, method="POST",
                                     headers={"Content-Type": "application/json",
                                              "Authorization": f"Bearer {token}"})
        try:
            resp = urllib.request.urlopen(req, timeout=30, context=ctx).read()
            data = _json.loads(resp)
            if data.get("errors"):
                print(f"[!] {question}: {data['errors'][0].get('message')}", file=sys.stderr)
            else:
                ok += 1
        except Exception as e:
            print(f"[!] push failed for {question}: {e}", file=sys.stderr)
    print(f"[+] Pushed {ok}/{len(files)} knowledge docs to {endpoint}")


if __name__ == "__main__":
    main()

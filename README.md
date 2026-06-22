# pentagi-knowledge

Open, machine-readable **security knowledge packs** for autonomous pentest agents -
starting with **MITRE ATT&CK®** - formatted for import into
[PentAGI](https://github.com/vxcontrol/pentagi) `Knowledges` (pgvector semantic search)
to drive **MITRE-ATT&CK-based automation attack flows**.

Each framework item (tactic, technique, sub-technique, …) becomes **one Markdown file**
with YAML frontmatter, so a vector store returns precise, phase-relevant knowledge to the
planner/pentester agents.

> ⚠️ **Authorised use only.** These knowledge packs describe offensive techniques for
> defensive understanding and *authorised* testing. Only run attack flows against systems
> you own or have explicit written permission to test.

## What's inside

| Source | Framework | Domain | Version | Items |
|--------|-----------|--------|---------|-------|
| MITRE ATT&CK | ATT&CK | Enterprise | v19.1 | 15 tactics - 222 techniques - 475 sub-techniques (712) |
| MITRE ATT&CK | ATT&CK | Mobile | v19.1 | 12 tactics, 77 techniques, 47 sub-techniques (136) |
| MITRE ATT&CK | ATT&CK | ICS | v19.1 | 12 tactics, 79 techniques, 18 sub-techniques (109) |

## Repository structure

```
pentagi-knowledge/
├── tools/
│   └── build_attack_knowledge.py   # generator + optional PentAGI push
├── mitre/
│   └── attack/
│       ├── enterprise/
│       │   ├── tactics/            # 15 files
│       │   ├── techniques/         # 697 technique + sub-technique files
│       │   ├── INDEX.md            # full map
│       │   └── manifest.json       # version, counts, source, date
│       ├── mobile/                 # 12 tactics, 124 technique files, INDEX, manifest
│       └── ics/                    # 12 tactics, 97 technique files, INDEX, manifest
├── docs/
│   └── import-to-pentagi.md        # how to push into PentAGI Knowledges
├── README.md  -  LICENSE (MIT)  -  NOTICE (MITRE attribution)  -  CONTRIBUTING.md
```

Future non-MITRE sources sit as siblings of `mitre/` (e.g. `owasp/`, `atlas/`), one
framework per top-level folder.

## Document format

```yaml
---
attack_id: T1059
name: Command and Scripting Interpreter
type: technique
tactics: [Execution]
platforms: [Windows, Linux, macOS]
url: https://attack.mitre.org/techniques/T1059
tags: [mitre-attack, technique, T1059]
---
```
Body sections: **Summary**, **Role in the attack flow**, **Detection**,
**Mitigations**, sub-technique list, source link.

## Regenerate / update

```bash
pip install mitreattack-python
python tools/build_attack_knowledge.py --domain enterprise --out ./mitre/attack/enterprise
python tools/build_attack_knowledge.py --domain mobile     --out ./mitre/attack/mobile
python tools/build_attack_knowledge.py --domain ics        --out ./mitre/attack/ics
```

ATT&CK is versioned; re-run after a new release to refresh. See `manifest.json` for the
version currently committed.

## Import into PentAGI

See [docs/import-to-pentagi.md](docs/import-to-pentagi.md) - covers the embedding
provider setup (Ollama/OpenAI), API token, and the batch push.

## Roadmap

- [x] Domain-aware generator (Enterprise / Mobile / ICS)
- [x] Mobile + ICS packs committed (957 docs total across 3 domains)
- [ ] MITRE ATLAS (adversarial AI)
- [ ] OWASP Top 10 / WSTG mappings
- [ ] CWE / CAPEC cross-references
- [ ] Per-technique tooling hints (nmap, metasploit, sqlmap, …)

## License & attribution

Code, tooling and structure: **MIT** (see `LICENSE`).
Knowledge content derived from **MITRE ATT&CK®** © The MITRE Corporation, used under the
[ATT&CK Terms of Use](https://attack.mitre.org/resources/legal-and-branding/terms-of-use/)
- see `NOTICE`.

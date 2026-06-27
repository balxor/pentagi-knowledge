# pentagi-knowledge

Open, machine-readable **security knowledge packs** for autonomous pentest agents.
The initial pack is built from **MITRE ATT&CK®** and formatted for import into
[PentAGI](https://github.com/vxcontrol/pentagi) `Knowledges`, where pgvector
semantic search helps planner and pentester agents retrieve phase-relevant
security knowledge.

Each framework item (tactic, technique, sub-technique, …) becomes **one Markdown file**
with YAML frontmatter. This keeps retrieval precise and gives agents focused context
for the current phase of an authorized assessment.

> ⚠️ **Authorized use only.** These knowledge packs describe offensive techniques for
> defensive understanding and *authorized* testing. Only run attack flows against systems
> you own or have explicit written permission to test.

## What's inside

| Source | Framework | Domain | Version | Items |
|--------|-----------|--------|---------|-------|
| MITRE ATT&CK | ATT&CK | Enterprise | v19.1 | 15 tactics, 222 techniques, 475 sub-techniques (712) |
| MITRE ATT&CK | ATT&CK | Mobile | v19.1 | 12 tactics, 77 techniques, 47 sub-techniques (136) |
| MITRE ATT&CK | ATT&CK | ICS | v19.1 | 12 tactics, 79 techniques, 18 sub-techniques (109) |

**Other MITRE sources** (each has its own generator; run locally then commit):

| Source | Covers | Generator |
|--------|--------|-----------|
| MITRE CWE | Weakness classes, e.g. CWE-134 (format string), CWE-120/121/122/787 (buffer overflow), CWE-416 (use-after-free) | `tools/build_cwe_knowledge.py` |
| MITRE CAPEC | Attack patterns, e.g. CAPEC-135 (format-string injection), CAPEC-100/123 (buffer overflow) | `tools/build_capec_knowledge.py` |

## Repository structure

```
pentagi-knowledge/
├── tools/
│   ├── build_attack_knowledge.py       # ATT&CK (enterprise/mobile/ics)
│   ├── build_capec_knowledge.py        # CAPEC attack patterns
│   ├── build_cwe_knowledge.py          # CWE weakness classes
│   ├── push_tooling.py                 # Push curated tooling overlays
│   └── update_tracking_status.py       # Sync TRACKING.md checkboxes
├── mitre/
│   ├── attack/
│   │   ├── enterprise/                 # 15 tactics, 697 technique files, INDEX, manifest
│   │   ├── mobile/                     # 12 tactics, 124 technique files, INDEX, manifest
│   │   └── ics/                        # 12 tactics, 97 technique files, INDEX, manifest
│   ├── capec/                          # CAPEC-### attack patterns (build_capec_knowledge.py)
│   └── cwe/                            # CWE-### weakness classes (build_cwe_knowledge.py)
├── tooling/                            # Curated tooling overlays (survive regeneration)
│   ├── enterprise/                     # One .md per technique with execution commands
│   ├── mobile/
│   ├── ics/
│   ├── capec/
│   └── cwe/
├── docs/
│   └── import-to-pentagi.md            # how to push into PentAGI Knowledges
├── requirements.txt                    # Python dependency for push_tooling.py
├── TRACKING.md                         # Master checklist & priority for tooling work
├── README.md  -  LICENSE (MIT)  -  NOTICE (MITRE attribution)  -  CONTRIBUTING.md
```

MITRE frameworks live under `mitre/` (`attack/`, `capec/`, `cwe/`). Future non-MITRE
sources sit as siblings of `mitre/` (e.g. `owasp/`), one framework per folder.
Tooling overlays sit under `tooling/` as standalone Markdown files. They reference
ATT&CK IDs through YAML frontmatter but never merge into MITRE-generated files, so
they survive regeneration. See `TRACKING.md` for priority order and progress.

## Source of truth

- `mitre/**` is generated content. Regenerate it with the scripts under `tools/`
  instead of editing individual generated documents by hand.
- `tooling/**` is curated content. Add operator command references here so they
  survive MITRE pack regeneration.
- `TRACKING.md` is the master checklist for tooling coverage. Keep it in sync with
  `python tools/update_tracking_status.py`.
- `tools/**` contains generators and import helpers.

## Quick start

```bash
pip install -r requirements.txt
python -m py_compile tools/*.py
python tools/validate_tooling_frontmatter.py
python tools/update_tracking_status.py --check
```

To refresh generated MITRE packs, run the commands in the next section. To import
the packs into PentAGI, see [docs/import-to-pentagi.md](docs/import-to-pentagi.md).

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
python tools/build_capec_knowledge.py --out ./mitre/capec
python tools/build_cwe_knowledge.py   --out ./mitre/cwe
```

ATT&CK is versioned; re-run after a new release to refresh. See `manifest.json` for the
version currently committed.

## Import into PentAGI

See [docs/import-to-pentagi.md](docs/import-to-pentagi.md) - covers the embedding
provider setup, API token, OS-specific commands, TLS verification, and batch push.

## Roadmap

- [x] Domain-aware generator (Enterprise / Mobile / ICS)
- [x] Mobile + ICS packs committed (957 docs total across 3 domains)
- [ ] MITRE ATLAS (adversarial AI)
- [ ] OWASP Top 10 / WSTG mappings
- [x] CWE + CAPEC generators
- [x] Commit CWE + CAPEC packs
- [x] Per-technique tooling hints (execution commands for autonomous agents)
- [ ] Expand tooling coverage (P0 Credential Access, P1 Lateral Movement, …)

## License & attribution

Code, tooling, and repository structure: **MIT** (see `LICENSE`).
Knowledge content derived from **MITRE ATT&CK®**, **MITRE CAPEC™**, and **MITRE CWE™**
remains subject to the applicable MITRE terms of use. See `NOTICE`.

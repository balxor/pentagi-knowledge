# MITRE knowledge sources

Knowledge packs derived from MITRE's open security frameworks. They cross-reference
each other: CWE = the weakness, CAPEC = how it is attacked, ATT&CK = adversary
behavior observed in the wild.

| Folder | Framework | Per-item | Generator |
|--------|-----------|----------|-----------|
| [attack/](attack/) | ATT&CK (enterprise/mobile/ics) | tactic, technique, sub-technique | `tools/build_attack_knowledge.py` |
| [capec/](capec/)   | CAPEC | attack pattern | `tools/build_capec_knowledge.py` |
| [cwe/](cwe/)       | CWE   | weakness class | `tools/build_cwe_knowledge.py` |

All three are available for use with attribution to The MITRE Corporation. See `../NOTICE`.

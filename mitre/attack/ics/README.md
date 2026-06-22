# MITRE ATT&CK - ICS domain

Generated pack (see `manifest.json` for exact version and counts):
12 tactics, 79 techniques, 18 sub-techniques (109 files).

Refresh from the official ICS ATT&CK STIX after a new release:

```bash
python tools/build_attack_knowledge.py --domain ics --out ./mitre/attack/ics
```

Push to PentAGI: add `--push --pentagi-url https://localhost:8443 --token "$PENTAGI_API_TOKEN"`.

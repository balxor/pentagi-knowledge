# MITRE ATT&CK - Enterprise domain

Generated pack (see `manifest.json` for exact version and counts):
15 tactics, 222 techniques, 475 sub-techniques (712 files).

Refresh from the official Enterprise ATT&CK STIX after a new release:

```bash
python tools/build_attack_knowledge.py --domain enterprise --out ./mitre/attack/enterprise
```

Push to PentAGI: add `--push --pentagi-url https://localhost:8443 --token "$PENTAGI_API_TOKEN"`.

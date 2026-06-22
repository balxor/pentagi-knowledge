# MITRE ATT&CK - Mobile domain

Generated pack (see `manifest.json` for exact version and counts):
12 tactics, 77 techniques, 47 sub-techniques (136 files).

Refresh from the official Mobile ATT&CK STIX after a new release:

```bash
python tools/build_attack_knowledge.py --domain mobile --out ./mitre/attack/mobile
```

Push to PentAGI: add `--push --pentagi-url https://localhost:8443 --token "$PENTAGI_API_TOKEN"`.

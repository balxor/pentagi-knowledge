# MITRE ATT&CK - Mobile domain

Generate this pack from the official Mobile ATT&CK STIX:

```bash
pip install mitreattack-python
python tools/build_attack_knowledge.py --domain mobile --out ./mitre/attack/mobile
```

This writes `tactics/`, `techniques/`, `INDEX.md` and `manifest.json` here.
Optional push to PentAGI: add `--push --pentagi-url https://localhost:8443 --token "$PENTAGI_API_TOKEN"`.

# MITRE CAPEC - attack patterns

Per-pattern knowledge pack (one Markdown file per CAPEC). CAPEC describes *how*
weaknesses are attacked and cross-references CWE and ATT&CK, e.g.:

- **CAPEC-135** Format String Injection, **CAPEC-67** String Format Overflow in syslog()
- **CAPEC-100** Overflow Buffers, **CAPEC-123** Buffer Manipulation, **CAPEC-44** Overflow Binary Resource File

Generate from the official CAPEC STIX 2.1 (downloaded automatically):

```bash
python tools/build_capec_knowledge.py --out ./mitre/capec
```

Each file carries description, prerequisites, skills/resources required, consequences,
execution flow, mitigations, and related CWE/ATT&CK. See `manifest.json` for version
and counts. Push to PentAGI: add
`--push --pentagi-url https://localhost:8443 --token "$PENTAGI_API_TOKEN"`
(classified as docType `guide` / guideType `pentest`).

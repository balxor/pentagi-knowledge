# MITRE CWE - weakness classes

Per-weakness knowledge pack (one Markdown file per CWE). CWE catalogues the
*types of bugs* behind low-level exploitation, e.g.:

- **CWE-134** Use of Externally-Controlled Format String
- **CWE-787** Out-of-bounds Write, **CWE-125** Out-of-bounds Read
- **CWE-120** Classic Buffer Overflow, **CWE-121** Stack-based, **CWE-122** Heap-based
- **CWE-190** Integer Overflow, **CWE-416** Use After Free, **CWE-94** Code Injection

Generate from the official CWE XML (downloaded automatically):

```bash
python tools/build_cwe_knowledge.py --out ./mitre/cwe
```

Each file carries description, applicable languages, common consequences, potential
mitigations, related CAPEC patterns and observed CVE examples. See `manifest.json`
for version and counts. Push to PentAGI: add
`--push --pentagi-url https://localhost:8443 --token "$PENTAGI_API_TOKEN"`
(classified as docType `answer` / answerType `vulnerability`).

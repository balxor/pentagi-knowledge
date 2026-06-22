# MITRE ATT&CK knowledge packs

One folder per ATT&CK domain. Each domain ships per-item Markdown files
(`tactics/` + `techniques/`), an `INDEX.md`, and a `manifest.json`.

| Domain | Version | Tactics | Techniques | Sub-techniques | Files |
|--------|---------|---------|------------|----------------|-------|
| [enterprise](enterprise/) | v19.1 | 15 | 222 | 475 | 712 |
| [mobile](mobile/)         | v19.1 | 12 | 77  | 47  | 136 |
| [ics](ics/)               | v19.1 | 12 | 79  | 18  | 109 |

Generate or refresh any domain:

```bash
python ../../tools/build_attack_knowledge.py --domain <enterprise|mobile|ics> --out ./<domain>
```

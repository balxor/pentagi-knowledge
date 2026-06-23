# Tooling knowledge overlay

Operator-focused command references that complement the MITRE ATT&CK packs in
`pentagi-knowledge`. Each file maps to one ATT&CK technique by `attack_id` and adds
concrete, runnable tooling (the "how", not the "what").

Decoupled by design: these files live in their own source, so regenerating the
ATT&CK packs never overwrites them.

```
tooling/
  enterprise/<ATTACK_ID>__<slug>.md   # one file per technique you enhance (sparse)
```

## File format

```yaml
---
attack_id: T1059.001
name: PowerShell
type: tooling
tactics: [Execution]
platforms: [Windows]
attack_ref: https://attack.mitre.org/techniques/T1059/001
tags: [tooling, mitre-attack, T1059.001, execution]
---
# T1059.001 PowerShell - Tooling
<curated command sections>
```

- Only create files for techniques worth tooling - this is intentionally sparse.
- Keep MITRE description out (it lives in the base pack); put only operator tooling here.
- Mark curated/non-MITRE content clearly; attribute any third-party tool snippets.

## Tracking

`TRACKING.md` is the master checklist for tooling coverage. It is maintained from
the files that actually exist under `tooling/**`, so checkbox state stays aligned
with the curated overlay set.

```bash
python tools/update_tracking_status.py --check
python tools/update_tracking_status.py
```

The `--check` form reports drift without writing changes. The second command
rewrites `TRACKING.md` with current checkbox state and file paths.

## Push to PentAGI

Tooling docs are pushed as their own Knowledge documents (docType `code`), so the
agent retrieves the ATT&CK description and the tooling side-by-side via semantic search.

```bash
pip install -r requirements.txt
python tools/push_tooling.py --dir tooling/enterprise \
  --pentagi-url https://localhost:8443 --token "$PENTAGI_API_TOKEN" --insecure
```

> Authorised use only. These are offensive command references for sanctioned testing.

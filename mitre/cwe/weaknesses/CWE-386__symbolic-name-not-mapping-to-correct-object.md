---
cwe_id: CWE-386
name: Symbolic Name not Mapping to Correct Object
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/386.html
tags: [mitre-cwe, weakness, CWE-386]
---

# CWE-386 - Symbolic Name not Mapping to Correct Object

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-386](https://cwe.mitre.org/data/definitions/386.html)

## Description
A constant symbolic reference to an object is used, even though the reference can resolve to a different object over time.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity
- **Integrity, Confidentiality, Other**: Modify Application Data, Modify Files or Directories, Read Application Data, Read Files or Directories, Other
- **Integrity, Other**: Modify Application Data, Other
- **Non-Repudiation**: Hide Activities
- **Non-Repudiation, Integrity**: Modify Files or Directories

## Related weaknesses
- CWE-706 (ChildOf)
- CWE-367 (PeerOf)
- CWE-610 (PeerOf)
- CWE-486 (PeerOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/386.html

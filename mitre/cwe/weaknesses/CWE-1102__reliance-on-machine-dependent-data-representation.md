---
cwe_id: CWE-1102
name: Reliance on Machine-Dependent Data Representation
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1102.html
tags: [mitre-cwe, weakness, CWE-1102]
---

# CWE-1102 - Reliance on Machine-Dependent Data Representation

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1102](https://cwe.mitre.org/data/definitions/1102.html)

## Description
The code uses a data representation that relies on low-level data representation or constructs that may vary across different processors, physical machines, OSes, or other physical components.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Maintainability

## Related weaknesses
- CWE-758 (ChildOf)
- CWE-1105 (PeerOf)

## Observed examples (CVE)
- **CVE-2025-47153**: Chain: build process for JavaScript runtime environment can have inconsistent sizes for off_t (CWE-1102), allowing out-of-bounds access / segmentation fault (CWE-119)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1102.html

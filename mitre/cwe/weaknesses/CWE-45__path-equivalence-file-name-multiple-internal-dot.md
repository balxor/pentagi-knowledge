---
cwe_id: CWE-45
name: Path Equivalence: 'file...name' (Multiple Internal Dot)
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/45.html
tags: [mitre-cwe, weakness, CWE-45]
---

# CWE-45 - Path Equivalence: 'file...name' (Multiple Internal Dot)

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-45](https://cwe.mitre.org/data/definitions/45.html)

## Description
The product accepts path input in the form of multiple internal dot ('file...dir') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Related weaknesses
- CWE-44 (ChildOf)
- CWE-165 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/45.html

---
cwe_id: CWE-47
name: Path Equivalence: ' filename' (Leading Space)
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/47.html
tags: [mitre-cwe, weakness, CWE-47]
---

# CWE-47 - Path Equivalence: ' filename' (Leading Space)

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-47](https://cwe.mitre.org/data/definitions/47.html)

## Description
The product accepts path input in the form of leading space (' filedir') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Related weaknesses
- CWE-41 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/47.html

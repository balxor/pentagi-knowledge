---
cwe_id: CWE-44
name: Path Equivalence: 'file.name' (Internal Dot)
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/44.html
tags: [mitre-cwe, weakness, CWE-44]
---

# CWE-44 - Path Equivalence: 'file.name' (Internal Dot)

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-44](https://cwe.mitre.org/data/definitions/44.html)

## Description
The product accepts path input in the form of internal dot ('file.ordir') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Related weaknesses
- CWE-41 (ChildOf)

## Observed examples (CVE)
- **CVE-2025-24813**: servlet in Java-based product allows code execution via a "file.Name" internal dot

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/44.html

---
cwe_id: CWE-48
name: Path Equivalence: 'file name' (Internal Whitespace)
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/48.html
tags: [mitre-cwe, weakness, CWE-48]
---

# CWE-48 - Path Equivalence: 'file name' (Internal Whitespace)

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-48](https://cwe.mitre.org/data/definitions/48.html)

## Description
The product accepts path input in the form of internal space ('file(SPACE)name') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Related weaknesses
- CWE-41 (ChildOf)

## Observed examples (CVE)
- **CVE-2000-0293**: Filenames with spaces allow arbitrary file deletion when the product does not properly quote them; some overlap with path traversal.
- **CVE-2001-1567**: "+" characters in query string converted to spaces before sensitive file/extension (internal space), leading to bypass of access restrictions to the file.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/48.html

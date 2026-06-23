---
cwe_id: CWE-43
name: Path Equivalence: 'filename....' (Multiple Trailing Dot)
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/43.html
tags: [mitre-cwe, weakness, CWE-43]
---

# CWE-43 - Path Equivalence: 'filename....' (Multiple Trailing Dot)

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-43](https://cwe.mitre.org/data/definitions/43.html)

## Description
The product accepts path input in the form of multiple trailing dot ('filedir....') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Related weaknesses
- CWE-42 (ChildOf)
- CWE-163 (ChildOf)

## Observed examples (CVE)
- **CVE-2004-0281**: Multiple trailing dot allows directory listing

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/43.html

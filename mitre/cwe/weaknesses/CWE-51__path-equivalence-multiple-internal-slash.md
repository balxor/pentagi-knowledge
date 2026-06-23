---
cwe_id: CWE-51
name: Path Equivalence: '/multiple//internal/slash'
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/51.html
tags: [mitre-cwe, weakness, CWE-51]
---

# CWE-51 - Path Equivalence: '/multiple//internal/slash'

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-51](https://cwe.mitre.org/data/definitions/51.html)

## Description
The product accepts path input in the form of multiple internal slash ('/multiple//internal/slash/') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Potential mitigations
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Related weaknesses
- CWE-41 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-1483**: Read files with full pathname using multiple internal slash.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/51.html

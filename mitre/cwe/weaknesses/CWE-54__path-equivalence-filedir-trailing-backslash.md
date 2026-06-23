---
cwe_id: CWE-54
name: Path Equivalence: 'filedir\' (Trailing Backslash)
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Windows, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/54.html
tags: [mitre-cwe, weakness, CWE-54]
---

# CWE-54 - Path Equivalence: 'filedir\' (Trailing Backslash)

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-54](https://cwe.mitre.org/data/definitions/54.html)

## Description
The product accepts path input in the form of trailing backslash ('filedir\') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

## Applicable platforms / languages
Not Language-Specific, Windows, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Potential mitigations
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Related weaknesses
- CWE-41 (ChildOf)
- CWE-162 (ChildOf)

## Observed examples (CVE)
- **CVE-2004-0847**: web framework for .NET allows remote attackers to bypass authentication for .aspx files in restricted directories via a request containing a (1) "\" (backslash) or (2) "%5C" (encoded backslash)
- **CVE-2004-0061**: Bypass directory access restrictions using trailing dot in URL

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/54.html

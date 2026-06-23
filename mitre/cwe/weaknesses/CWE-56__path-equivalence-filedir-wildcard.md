---
cwe_id: CWE-56
name: Path Equivalence: 'filedir*' (Wildcard)
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/56.html
tags: [mitre-cwe, weakness, CWE-56]
---

# CWE-56 - Path Equivalence: 'filedir*' (Wildcard)

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-56](https://cwe.mitre.org/data/definitions/56.html)

## Description
The product accepts path input in the form of asterisk wildcard ('filedir*') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Potential mitigations
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Related weaknesses
- CWE-41 (ChildOf)
- CWE-155 (ChildOf)

## Observed examples (CVE)
- **CVE-2004-0696**: List directories using desired path and "*"
- **CVE-2002-0433**: List files in web server using "*.ext"

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/56.html

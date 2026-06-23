---
cwe_id: CWE-52
name: Path Equivalence: '/multiple/trailing/slash//'
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific, Web Based]
related_capec: []
url: https://cwe.mitre.org/data/definitions/52.html
tags: [mitre-cwe, weakness, CWE-52]
---

# CWE-52 - Path Equivalence: '/multiple/trailing/slash//'

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-52](https://cwe.mitre.org/data/definitions/52.html)

## Description
The product accepts path input in the form of multiple trailing slash ('/multiple/trailing/slash//') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Potential mitigations
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Related weaknesses
- CWE-41 (ChildOf)
- CWE-163 (ChildOf)
- CWE-289 (CanPrecede)

## Observed examples (CVE)
- **CVE-2002-1078**: Directory listings in web server using multiple trailing slash

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/52.html

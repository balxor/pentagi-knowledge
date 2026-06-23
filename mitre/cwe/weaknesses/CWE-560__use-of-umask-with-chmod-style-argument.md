---
cwe_id: CWE-560
name: Use of umask() with chmod-style Argument
type: weakness
abstraction: Variant
status: Draft
languages: [C]
related_capec: []
url: https://cwe.mitre.org/data/definitions/560.html
tags: [mitre-cwe, weakness, CWE-560]
---

# CWE-560 - Use of umask() with chmod-style Argument

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-560](https://cwe.mitre.org/data/definitions/560.html)

## Description
The product calls umask() with an incorrect argument that is specified as if it is an argument to chmod().

## Applicable platforms / languages
C

## Common consequences
- **Confidentiality, Integrity, Access Control**: Read Files or Directories, Modify Files or Directories, Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: Use umask() with the correct argument.

## Related weaknesses
- CWE-687 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/560.html

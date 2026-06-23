---
cwe_id: CWE-210
name: Self-generated Error Message Containing Sensitive Information
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/210.html
tags: [mitre-cwe, weakness, CWE-210]
---

# CWE-210 - Self-generated Error Message Containing Sensitive Information

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-210](https://cwe.mitre.org/data/definitions/210.html)

## Description
The product identifies an error condition and creates its own diagnostic or error messages that contain sensitive information.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Implementation, Build and Compilation**: Debugging information should not make its way into a production release.
- **Implementation, Build and Compilation**: Debugging information should not make its way into a production release.

## Related weaknesses
- CWE-209 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-1745**: Infoleak of sensitive information in error message (physical access required).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/210.html

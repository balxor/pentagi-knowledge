---
cwe_id: CWE-220
name: Storage of File With Sensitive Data Under FTP Root
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/220.html
tags: [mitre-cwe, weakness, CWE-220]
---

# CWE-220 - Storage of File With Sensitive Data Under FTP Root

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-220](https://cwe.mitre.org/data/definitions/220.html)

## Description
The product stores sensitive data under the FTP server root with insufficient access control, which might make it accessible to untrusted parties.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Implementation, System Configuration**: Avoid storing information under the FTP root directory.
- **System Configuration**: Access control permissions should be set to prevent reading/writing of sensitive files inside/outside of the FTP directory.

## Related weaknesses
- CWE-552 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/220.html

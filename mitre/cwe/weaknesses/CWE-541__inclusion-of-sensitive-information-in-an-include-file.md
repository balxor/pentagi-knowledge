---
cwe_id: CWE-541
name: Inclusion of Sensitive Information in an Include File
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/541.html
tags: [mitre-cwe, weakness, CWE-541]
---

# CWE-541 - Inclusion of Sensitive Information in an Include File

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-541](https://cwe.mitre.org/data/definitions/541.html)

## Description
If an include file source is accessible, the file can contain usernames and passwords, as well as sensitive information pertaining to the application and system.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design**: Do not store sensitive information in include files.
- **Architecture and Design, System Configuration**: Protect include files from being exposed.

## Related weaknesses
- CWE-540 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/541.html

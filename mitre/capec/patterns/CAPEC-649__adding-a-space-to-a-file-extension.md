---
capec_id: CAPEC-649
name: Adding a Space to a File Extension
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: Medium
related_cwe: [CWE-46]
related_attack: [T1036.006]
url: https://capec.mitre.org/data/definitions/649.html
tags: [mitre-capec, attack-pattern, CAPEC-649]
---

# CAPEC-649 - Adding a Space to a File Extension

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-649](https://capec.mitre.org/data/definitions/649.html)

## Description
An adversary adds a space character to the end of a file extension and takes advantage of an application that does not properly neutralize trailing special elements in file names. This extra space, which can be difficult for a user to notice, affects which default application is used to operate on the file and can be leveraged by the adversary to control execution.

## Prerequisites
- The use of the file must be controlled by the file extension.

## Consequences
- **Availability**: Execute Unauthorized Commands
- **Confidentiality**: Execute Unauthorized Commands
- **Integrity**: Execute Unauthorized Commands

## Mitigations
- File extensions should be checked to see if non-visible characters are being included.

## Related weaknesses (CWE)
- [CWE-46](https://cwe.mitre.org/data/definitions/46.html)

## Related ATT&CK techniques
- T1036.006

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/649.html

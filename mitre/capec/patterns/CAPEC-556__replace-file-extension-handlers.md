---
capec_id: CAPEC-556
name: Replace File Extension Handlers
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: [CWE-284]
related_attack: [T1546.001]
url: https://capec.mitre.org/data/definitions/556.html
tags: [mitre-capec, attack-pattern, CAPEC-556]
---

# CAPEC-556 - Replace File Extension Handlers

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-556](https://capec.mitre.org/data/definitions/556.html)

## Description
When a file is opened, its file handler is checked to determine which program opens the file. File handlers are configuration properties of many operating systems. Applications can modify the file handler for a given file extension to call an arbitrary program when a file with the given extension is opened.

## Mitigations
- Inspect registry for changes. Limit privileges of user accounts so changes to default file handlers can only be performed by authorized administrators.

## Related weaknesses (CWE)
- [CWE-284](https://cwe.mitre.org/data/definitions/284.html)

## Related ATT&CK techniques
- T1546.001

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/556.html

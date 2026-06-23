---
capec_id: CAPEC-551
name: Modify Existing Service
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: [CWE-284, CWE-522]
related_attack: [T1543]
url: https://capec.mitre.org/data/definitions/551.html
tags: [mitre-capec, attack-pattern, CAPEC-551]
---

# CAPEC-551 - Modify Existing Service

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-551](https://capec.mitre.org/data/definitions/551.html)

## Description
When an operating system starts, it also starts programs called services or daemons. Modifying existing services may break existing services or may enable services that are disabled/not commonly used.

## Mitigations
- Limit privileges of user accounts so service changes can only be performed by authorized administrators. Also monitor any service changes that may occur inadvertently.

## Related weaknesses (CWE)
- [CWE-284](https://cwe.mitre.org/data/definitions/284.html)
- [CWE-522](https://cwe.mitre.org/data/definitions/522.html)

## Related ATT&CK techniques
- T1543

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/551.html

---
capec_id: CAPEC-176
name: Configuration/Environment Manipulation
type: attack-pattern
abstraction: Meta
likelihood: n/a
severity: Medium
related_cwe: [CWE-15, CWE-1233, CWE-1234, CWE-1304, CWE-1328]
related_attack: []
url: https://capec.mitre.org/data/definitions/176.html
tags: [mitre-capec, attack-pattern, CAPEC-176]
---

# CAPEC-176 - Configuration/Environment Manipulation

**Abstraction:** Meta  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-176](https://capec.mitre.org/data/definitions/176.html)

## Description
An attacker manipulates files or settings external to a target application which affect the behavior of that application. For example, many applications use external configuration files and libraries - modification of these entities or otherwise affecting the application's ability to use them would constitute a configuration/environment manipulation attack.

## Prerequisites
- The target application must consult external files or configuration controls to control its execution. All but the very simplest applications meet this requirement.

## Resources required
- The attacker must have the access necessary to affect the files or other environment items the targeted application uses for its operations.

## Related weaknesses (CWE)
- [CWE-15](https://cwe.mitre.org/data/definitions/15.html)
- [CWE-1233](https://cwe.mitre.org/data/definitions/1233.html)
- [CWE-1234](https://cwe.mitre.org/data/definitions/1234.html)
- [CWE-1304](https://cwe.mitre.org/data/definitions/1304.html)
- [CWE-1328](https://cwe.mitre.org/data/definitions/1328.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/176.html

---
capec_id: CAPEC-550
name: Install New Service
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: [CWE-284]
related_attack: [T1543]
url: https://capec.mitre.org/data/definitions/550.html
tags: [mitre-capec, attack-pattern, CAPEC-550]
---

# CAPEC-550 - Install New Service

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-550](https://capec.mitre.org/data/definitions/550.html)

## Description
When an operating system starts, it also starts programs called services or daemons. Adversaries may install a new service which will be executed at startup (on a Windows system, by modifying the registry). The service name may be disguised by using a name from a related operating system or benign software. Services are usually run with elevated privileges.

## Mitigations
- Limit privileges of user accounts so new service creation can only be performed by authorized administrators.

## Related weaknesses (CWE)
- [CWE-284](https://cwe.mitre.org/data/definitions/284.html)

## Related ATT&CK techniques
- T1543

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/550.html

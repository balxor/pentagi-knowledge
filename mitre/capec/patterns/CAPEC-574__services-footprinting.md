---
capec_id: CAPEC-574
name: Services Footprinting
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: Low
related_cwe: [CWE-200]
related_attack: [T1007]
url: https://capec.mitre.org/data/definitions/574.html
tags: [mitre-capec, attack-pattern, CAPEC-574]
---

# CAPEC-574 - Services Footprinting

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** Low  -  **CAPEC:** [CAPEC-574](https://capec.mitre.org/data/definitions/574.html)

## Description
An adversary exploits functionality meant to identify information about the services on the target system to an authorized user. By knowing what services are registered on the target system, the adversary can learn about the target environment as a means towards further malicious behavior. Depending on the operating system, commands that can obtain services information include "sc" and "tasklist/svc" using Tasklist, and "net start" using Net.

## Prerequisites
- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.

## Consequences
- **Access_Control**: Bypass Protection Mechanism, Hide Activities
- **Authorization**: Bypass Protection Mechanism, Hide Activities
- **Confidentiality**: Other, Bypass Protection Mechanism, Hide Activities

## Mitigations
- Identify programs that may be used to acquire service information and block them by using a software restriction policy or tools that restrict program execution by uaing a process allowlist.

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

## Related ATT&CK techniques
- T1007

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/574.html

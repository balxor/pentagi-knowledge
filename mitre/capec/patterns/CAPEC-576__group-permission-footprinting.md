---
capec_id: CAPEC-576
name: Group Permission Footprinting
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: Low
related_cwe: [CWE-200]
related_attack: [T1069, T1615]
url: https://capec.mitre.org/data/definitions/576.html
tags: [mitre-capec, attack-pattern, CAPEC-576]
---

# CAPEC-576 - Group Permission Footprinting

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** Low  -  **CAPEC:** [CAPEC-576](https://capec.mitre.org/data/definitions/576.html)

## Description
An adversary exploits functionality meant to identify information about user groups and their permissions on the target system to an authorized user. By knowing what users/permissions are registered on the target system, the adversary can inform further and more targeted malicious behavior. An example Windows command which can list local groups is "net localgroup".

## Prerequisites
- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.

## Consequences
- **Access_Control**: Bypass Protection Mechanism, Hide Activities
- **Authorization**: Bypass Protection Mechanism, Hide Activities
- **Confidentiality**: Other, Bypass Protection Mechanism, Hide Activities

## Mitigations
- Identify programs (such as "net") that may be used to enumerate local group permissions and block them by using a software restriction Policy or tools that restrict program execution by using a process allowlist.

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

## Related ATT&CK techniques
- T1069
- T1615

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/576.html

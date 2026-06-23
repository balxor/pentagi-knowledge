---
capec_id: CAPEC-575
name: Account Footprinting
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: Low
related_cwe: [CWE-200]
related_attack: [T1087]
url: https://capec.mitre.org/data/definitions/575.html
tags: [mitre-capec, attack-pattern, CAPEC-575]
---

# CAPEC-575 - Account Footprinting

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** Low  -  **CAPEC:** [CAPEC-575](https://capec.mitre.org/data/definitions/575.html)

## Description
An adversary exploits functionality meant to identify information about the domain accounts and their permissions on the target system to an authorized user. By knowing what accounts are registered on the target system, the adversary can inform further and more targeted malicious behavior. Example Windows commands which can acquire this information are: "net user" and "dsquery".

## Prerequisites
- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.

## Consequences
- **Access_Control**: Bypass Protection Mechanism, Hide Activities
- **Authorization**: Bypass Protection Mechanism, Hide Activities
- **Confidentiality**: Other, Bypass Protection Mechanism, Hide Activities

## Mitigations
- Identify programs that may be used to acquire account information and block them by using a software restriction policy or tools that restrict program execution by uysing a process allowlist.

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

## Related ATT&CK techniques
- T1087

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/575.html

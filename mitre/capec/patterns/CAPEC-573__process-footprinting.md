---
capec_id: CAPEC-573
name: Process Footprinting
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: Low
related_cwe: [CWE-200]
related_attack: [T1057]
url: https://capec.mitre.org/data/definitions/573.html
tags: [mitre-capec, attack-pattern, CAPEC-573]
---

# CAPEC-573 - Process Footprinting

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** Low  -  **CAPEC:** [CAPEC-573](https://capec.mitre.org/data/definitions/573.html)

## Description
An adversary exploits functionality meant to identify information about the currently running processes on the target system to an authorized user. By knowing what processes are running on the target system, the adversary can learn about the target environment as a means towards further malicious behavior.

## Prerequisites
- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.

## Consequences
- **Access_Control**: Bypass Protection Mechanism, Hide Activities
- **Authorization**: Bypass Protection Mechanism, Hide Activities
- **Confidentiality**: Other, Bypass Protection Mechanism, Hide Activities

## Mitigations
- Identify programs that may be used to acquire process information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

## Related ATT&CK techniques
- T1057

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/573.html

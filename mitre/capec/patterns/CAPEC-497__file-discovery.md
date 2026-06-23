---
capec_id: CAPEC-497
name: File Discovery
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Very Low
related_cwe: [CWE-200]
related_attack: [T1083]
url: https://capec.mitre.org/data/definitions/497.html
tags: [mitre-capec, attack-pattern, CAPEC-497]
---

# CAPEC-497 - File Discovery

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Very Low  -  **CAPEC:** [CAPEC-497](https://capec.mitre.org/data/definitions/497.html)

## Description
An adversary engages in probing and exploration activities to determine if common key files exists. Such files often contain configuration and security parameters of the targeted application, system or network. Using this knowledge may often pave the way for more damaging attacks.

## Prerequisites
- The adversary must know the location of these common key files.

## Consequences
- **Confidentiality**: Read Data

## Mitigations
- Leverage file protection mechanisms to render these files accessible only to authorized parties.

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

## Related ATT&CK techniques
- T1083

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/497.html

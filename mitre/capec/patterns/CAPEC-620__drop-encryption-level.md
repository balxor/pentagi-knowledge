---
capec_id: CAPEC-620
name: Drop Encryption Level
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: High
related_cwe: [CWE-757]
related_attack: [T1600]
url: https://capec.mitre.org/data/definitions/620.html
tags: [mitre-capec, attack-pattern, CAPEC-620]
---

# CAPEC-620 - Drop Encryption Level

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** High  -  **CAPEC:** [CAPEC-620](https://capec.mitre.org/data/definitions/620.html)

## Description
An attacker forces the encryption level to be lowered, thus enabling a successful attack against the encrypted data.

## Consequences
- **Access_Control**: Bypass Protection Mechanism

## Related weaknesses (CWE)
- [CWE-757](https://cwe.mitre.org/data/definitions/757.html)

## Related ATT&CK techniques
- T1600

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/620.html

---
capec_id: CAPEC-295
name: Timestamp Request
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-200]
related_attack: [T1124]
url: https://capec.mitre.org/data/definitions/295.html
tags: [mitre-capec, attack-pattern, CAPEC-295]
---

# CAPEC-295 - Timestamp Request

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-295](https://capec.mitre.org/data/definitions/295.html)

## Description
This pattern of attack leverages standard requests to learn the exact time associated with a target system. An adversary may be able to use the timestamp returned from the target to attack time-based security algorithms, such as random number generators, or time-based authentication mechanisms.

## Prerequisites
- The ability to send a timestamp request to a remote target and receive a response.

## Resources required
- Scanners or utilities that provide the ability to send custom ICMP queries.

## Consequences
- **Confidentiality**: Other

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

## Related ATT&CK techniques
- T1124

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/295.html

---
capec_id: CAPEC-595
name: Connection Reset
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: n/a
related_cwe: [CWE-940]
related_attack: []
url: https://capec.mitre.org/data/definitions/595.html
tags: [mitre-capec, attack-pattern, CAPEC-595]
---

# CAPEC-595 - Connection Reset

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-595](https://capec.mitre.org/data/definitions/595.html)

## Description
In this attack pattern, an adversary injects a connection reset packet to one or both ends of a target's connection. The attacker is therefore able to have the target and/or the destination server sever the connection without having to directly filter the traffic between them.

## Prerequisites
- This attack requires the ability to monitor the target's network connection.

## Related weaknesses (CWE)
- [CWE-940](https://cwe.mitre.org/data/definitions/940.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/595.html

---
capec_id: CAPEC-388
name: Application API Button Hijacking
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-471, CWE-345, CWE-346, CWE-602, CWE-311]
related_attack: []
url: https://capec.mitre.org/data/definitions/388.html
tags: [mitre-capec, attack-pattern, CAPEC-388]
---

# CAPEC-388 - Application API Button Hijacking

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-388](https://capec.mitre.org/data/definitions/388.html)

## Description
An attacker manipulates either egress or ingress data from a client within an application framework in order to change the destination and/or content of buttons displayed to a user within API messages. Performing this attack allows the attacker to manipulate content in such a way as to produce messages or content that looks authentic but contains buttons that point to an attacker controlled destination.

## Prerequisites
- Targeted software is utilizing application framework APIs

## Resources required
- A software program that allows the use of adversary-in-the-middle (CAPEC-94) communications between the client and server, such as a adversary-in-the-middle (CAPEC-94) proxy.

## Related weaknesses (CWE)
- [CWE-471](https://cwe.mitre.org/data/definitions/471.html)
- [CWE-345](https://cwe.mitre.org/data/definitions/345.html)
- [CWE-346](https://cwe.mitre.org/data/definitions/346.html)
- [CWE-602](https://cwe.mitre.org/data/definitions/602.html)
- [CWE-311](https://cwe.mitre.org/data/definitions/311.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/388.html

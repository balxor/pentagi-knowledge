---
capec_id: CAPEC-389
name: Content Spoofing Via Application API Manipulation
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-353]
related_attack: []
url: https://capec.mitre.org/data/definitions/389.html
tags: [mitre-capec, attack-pattern, CAPEC-389]
---

# CAPEC-389 - Content Spoofing Via Application API Manipulation

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-389](https://capec.mitre.org/data/definitions/389.html)

## Description
An attacker manipulates either egress or ingress data from a client within an application framework in order to change the content of messages. Performing this attack allows the attacker to manipulate content in such a way as to produce messages or content that look authentic but may contain deceptive links, spam-like content, or links to the attackers' code. In general, content-spoofing within an application API can be employed to stage many different types of attacks varied based on the attackers' intent. The techniques require use of specialized software that allow the attacker to use adversary-in-the-middle (CAPEC-94) communications between the web browser and the remote system.

## Prerequisites
- Targeted software is utilizing application framework APIs

## Resources required
- A software program that allows the use of adversary-in-the-middle communications between the client and server, such as an adversary-in-the-middle proxy.

## Related weaknesses (CWE)
- [CWE-353](https://cwe.mitre.org/data/definitions/353.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/389.html

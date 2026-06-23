---
capec_id: CAPEC-384
name: Application API Message Manipulation via Man-in-the-Middle
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Low
related_cwe: [CWE-471, CWE-345, CWE-346, CWE-602, CWE-311]
related_attack: []
url: https://capec.mitre.org/data/definitions/384.html
tags: [mitre-capec, attack-pattern, CAPEC-384]
---

# CAPEC-384 - Application API Message Manipulation via Man-in-the-Middle

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-384](https://capec.mitre.org/data/definitions/384.html)

## Description
An attacker manipulates either egress or ingress data from a client within an application framework in order to change the content of messages. Performing this attack can allow the attacker to gain unauthorized privileges within the application, or conduct attacks such as phishing, deceptive strategies to spread malware, or traditional web-application attacks. The techniques require use of specialized software that allow the attacker to perform adversary-in-the-middle (CAPEC-94) communications between the web browser and the remote system. Despite the use of AiTH software, the attack is actually directed at the server, as the client is one node in a series of content brokers that pass information along to the application framework. Additionally, it is not true "Adversary-in-the-Middle" attack at the network layer, but an application-layer attack the root cause of which is the master applications trust in the integrity of code supplied by the client.

## Prerequisites
- Targeted software is utilizing application framework APIs

## Resources required
- A software program that allows a user to man-in-the-middle communications between the client and server, such as a man-in-the-middle proxy.

## Related weaknesses (CWE)
- [CWE-471](https://cwe.mitre.org/data/definitions/471.html)
- [CWE-345](https://cwe.mitre.org/data/definitions/345.html)
- [CWE-346](https://cwe.mitre.org/data/definitions/346.html)
- [CWE-602](https://cwe.mitre.org/data/definitions/602.html)
- [CWE-311](https://cwe.mitre.org/data/definitions/311.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/384.html

---
capec_id: CAPEC-482
name: TCP Flood
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: n/a
related_cwe: [CWE-770]
related_attack: [T1498.001, T1499.001, T1499.002]
url: https://capec.mitre.org/data/definitions/482.html
tags: [mitre-capec, attack-pattern, CAPEC-482]
---

# CAPEC-482 - TCP Flood

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-482](https://capec.mitre.org/data/definitions/482.html)

## Description
An adversary may execute a flooding attack using the TCP protocol with the intent to deny legitimate users access to a service. These attacks exploit the weakness within the TCP protocol where there is some state information for the connection the server needs to maintain. This often involves the use of TCP SYN messages.

## Prerequisites
- This type of an attack requires the ability to generate a large amount of TCP traffic to send to the target port of a functioning server.

## Mitigations
- To mitigate this type of an attack, an organization can monitor incoming packets and look for patterns in the TCP traffic to determine if the network is under an attack. The potential target may implement a rate limit on TCP SYN messages which would provide limited capabilities while under attack.

## Related weaknesses (CWE)
- [CWE-770](https://cwe.mitre.org/data/definitions/770.html)

## Related ATT&CK techniques
- T1498.001
- T1499.001
- T1499.002

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/482.html

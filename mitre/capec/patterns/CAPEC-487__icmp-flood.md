---
capec_id: CAPEC-487
name: ICMP Flood
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: n/a
related_cwe: [CWE-770]
related_attack: []
url: https://capec.mitre.org/data/definitions/487.html
tags: [mitre-capec, attack-pattern, CAPEC-487]
---

# CAPEC-487 - ICMP Flood

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-487](https://capec.mitre.org/data/definitions/487.html)

## Description
An adversary may execute a flooding attack using the ICMP protocol with the intent to deny legitimate users access to a service by consuming the available network bandwidth. A typical attack involves a victim server receiving ICMP packets at a high rate from a wide range of source addresses. Additionally, due to the session-less nature of the ICMP protocol, the source of a packet is easily spoofed making it difficult to find the source of the attack.

## Prerequisites
- This type of an attack requires the ability to generate a large amount of ICMP traffic to send to the target server.

## Mitigations
- To mitigate this type of an attack, an organization can enable ingress filtering. Additionally modifications to BGP like black hole routing and sinkhole routing(RFC3882) help mitigate the spoofed source IP nature of these attacks.

## Related weaknesses (CWE)
- [CWE-770](https://cwe.mitre.org/data/definitions/770.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/487.html

---
capec_id: CAPEC-296
name: ICMP Information Request
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/296.html
tags: [mitre-capec, attack-pattern, CAPEC-296]
---

# CAPEC-296 - ICMP Information Request

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-296](https://capec.mitre.org/data/definitions/296.html)

## Description
An adversary sends an ICMP Information Request to a host to determine if it will respond to this deprecated mechanism. ICMP Information Requests are a deprecated message type. Information Requests were originally used for diskless machines to automatically obtain their network configuration, but this message type has been superseded by more robust protocol implementations like DHCP.

## Prerequisites
- The ability to send an ICMP Type 15 Information Request and receive an ICMP Type 16 Information Reply in response.

## Skills required
- **Low**: The adversary needs to know certain linux commands for this type of attack.

## Resources required
- Scanners or utilities that provide the ability to send custom ICMP queries.

## Consequences
- **Confidentiality**: Other

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/296.html

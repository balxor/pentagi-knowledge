---
capec_id: CAPEC-481
name: Contradictory Destinations in Traffic Routing Schemes
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: High
related_cwe: [CWE-923]
related_attack: [T1090.004]
url: https://capec.mitre.org/data/definitions/481.html
tags: [mitre-capec, attack-pattern, CAPEC-481]
---

# CAPEC-481 - Contradictory Destinations in Traffic Routing Schemes

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-481](https://capec.mitre.org/data/definitions/481.html)

## Description
Adversaries can provide contradictory destinations when sending messages. Traffic is routed in networks using the domain names in various headers available at different levels of the OSI model. In a Content Delivery Network (CDN) multiple domains might be available, and if there are contradictory domain names provided it is possible to route traffic to an inappropriate destination. The technique, called Domain Fronting, involves using different domain names in the SNI field of the TLS header and the Host field of the HTTP header. An alternative technique, called Domainless Fronting, is similar, but the SNI field is left blank.

## Prerequisites
- An adversary must be aware that their message will be routed using a CDN, and that both of the contradictory domains are served from that CDN.
- If the purpose of the Domain Fronting is to hide redirected C2 traffic, the C2 server must have been created in the CDN.

## Skills required
- **Medium**: The adversary must have some knowledge of how messages are routed.

## Consequences
- **Confidentiality**: Read Data, Modify Data

## Mitigations
- Monitor connections, checking headers in traffic for contradictory domain names, or empty domain names.

## Related weaknesses (CWE)
- [CWE-923](https://cwe.mitre.org/data/definitions/923.html)

## Related ATT&CK techniques
- T1090.004

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/481.html

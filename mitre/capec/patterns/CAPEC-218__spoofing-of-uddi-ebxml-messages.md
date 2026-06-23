---
capec_id: CAPEC-218
name: Spoofing of UDDI/ebXML Messages
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-345]
related_attack: []
url: https://capec.mitre.org/data/definitions/218.html
tags: [mitre-capec, attack-pattern, CAPEC-218]
---

# CAPEC-218 - Spoofing of UDDI/ebXML Messages

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-218](https://capec.mitre.org/data/definitions/218.html)

## Description
An attacker spoofs a UDDI, ebXML, or similar message in order to impersonate a service provider in an e-business transaction. UDDI, ebXML, and similar standards are used to identify businesses in e-business transactions. Among other things, they identify a particular participant, WSDL information for SOAP transactions, and supported communication protocols, including security protocols. By spoofing one of these messages an attacker could impersonate a legitimate business in a transaction or could manipulate the protocols used between a client and business. This could result in disclosure of sensitive information, loss of message integrity, or even financial fraud.

## Prerequisites
- The targeted business's UDDI or ebXML information must be served from a location that the attacker can spoof or compromise or the attacker must be able to intercept and modify unsecured UDDI/ebXML messages in transit.

## Resources required
- The attacker must be able to force the target user to accept their spoofed UDDI or ebXML message as opposed to the a message associated with a legitimate company. Depending on the follow-on for the attack, the attacker may also need to serve its own web services.

## Mitigations
- Implementation: Clients should only trust UDDI, ebXML, or similar messages that are verifiably signed by a trusted party.

## Related weaknesses (CWE)
- [CWE-345](https://cwe.mitre.org/data/definitions/345.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/218.html

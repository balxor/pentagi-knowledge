---
capec_id: CAPEC-219
name: XML Routing Detour Attacks
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Medium
related_cwe: [CWE-441, CWE-610]
related_attack: []
url: https://capec.mitre.org/data/definitions/219.html
tags: [mitre-capec, attack-pattern, CAPEC-219]
---

# CAPEC-219 - XML Routing Detour Attacks

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-219](https://capec.mitre.org/data/definitions/219.html)

## Description
An attacker subverts an intermediate system used to process XML content and forces the intermediate to modify and/or re-route the processing of the content. XML Routing Detour Attacks are Adversary in the Middle type attacks (CAPEC-94). The attacker compromises or inserts an intermediate system in the processing of the XML message. For example, WS-Routing can be used to specify a series of nodes or intermediaries through which content is passed. If any of the intermediate nodes in this route are compromised by an attacker they could be used for a routing detour attack. From the compromised system the attacker is able to route the XML process to other nodes of their choice and modify the responses so that the normal chain of processing is unaware of the interception. This system can forward the message to an outside entity and hide the forwarding and processing from the legitimate processing systems by altering the header information.

## Prerequisites
- The targeted system must have multiple stages processing of XML content.

## Skills required
- **Low**: To inject a bogus node in the XML routing table

## Resources required
- The attacker must be able to insert or compromise a system into the processing path for the transaction.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Accountability**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Gain Privileges, Bypass Protection Mechanism
- **Confidentiality**: Read Data
- **Integrity**: Modify Data
- **Non-Repudiation**: Gain Privileges

## Execution flow
Execution Flow Explore Survey the target: Using command line or an automated tool, an attacker records all instances of web services to process XML requests. Techniques Use automated tool to record all instances to process XML requests or find exposed WSDL. Use tools to crawl WSDL Experiment Identify SOAP messages that have multiple state processing.: Inspect instance to see whether the XML processing has multiple stages or not. Techniques Inspect the SOAP message routing head to see whether the XML processing has multiple stages or not. Exploit Launch an XML routing detour attack: The attacker injects a bogus routing node (using a WS-Referral service) into the routing table of the XML header of the SOAP message identified in the Explore phase. Thus, the attacker can route the XML message to the attacker controlled node (and access the message contents). Techniques The attacker injects a bogus routing node (using a WS-Referral service) into the routing table of the XML header of the SOAP message

## Mitigations
- Design: Specify maximum number intermediate nodes for the request and require SSL connections with mutual authentication.
- Implementation: Use SSL for connections between all parties with mutual authentication.

## Related weaknesses (CWE)
- [CWE-441](https://cwe.mitre.org/data/definitions/441.html)
- [CWE-610](https://cwe.mitre.org/data/definitions/610.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/219.html

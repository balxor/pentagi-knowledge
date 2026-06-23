---
capec_id: CAPEC-220
name: Client-Server Protocol Manipulation
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Medium
related_cwe: [CWE-757]
related_attack: []
url: https://capec.mitre.org/data/definitions/220.html
tags: [mitre-capec, attack-pattern, CAPEC-220]
---

# CAPEC-220 - Client-Server Protocol Manipulation

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-220](https://capec.mitre.org/data/definitions/220.html)

## Description
An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used for different types of interactions.

## Extended description
For example, an authentication protocol might be used to establish the identities of the server and client while a separate messaging protocol might be used to exchange data. If there is a weakness in a protocol used by the client and server, an attacker might take advantage of this to perform various types of attacks. For example, if the attacker is able to manipulate an authentication protocol, the attacker may be able spoof other clients or servers. If the attacker is able to manipulate a messaging protocol, the may be able to read sensitive information or modify message contents. This attack is often made easier by the fact that many clients and servers support multiple protocols to perform similar roles. For example, a server might support several different authentication protocols in order to support a wide range of clients, including legacy clients. Some of the older protocols may have vulnerabilities that allow an attacker to manipulate client-server interactions.

## Prerequisites
- The client and/or server must utilize a protocol that has a weakness allowing manipulation of the interaction.

## Resources required
- The adversary must be able to identify the weakness in the utilized protocol and exploit it. This may require a sniffing tool as well as packet creation abilities. The adversary will be aided if they can force the client and/or server to utilize a specific protocol known to contain exploitable weaknesses.

## Related weaknesses (CWE)
- [CWE-757](https://cwe.mitre.org/data/definitions/757.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/220.html

---
capec_id: CAPEC-94
name: Adversary in the Middle (AiTM)
type: attack-pattern
abstraction: Meta
likelihood: High
severity: Very High
related_cwe: [CWE-300, CWE-290, CWE-593, CWE-287, CWE-294]
related_attack: [T1557]
url: https://capec.mitre.org/data/definitions/94.html
tags: [mitre-capec, attack-pattern, CAPEC-94]
---

# CAPEC-94 - Adversary in the Middle (AiTM)

**Abstraction:** Meta  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-94](https://capec.mitre.org/data/definitions/94.html)

## Description
<xhtml:p>An adversary targets the communication between two components (typically client and server), in order to alter or obtain data from transactions. A general approach entails the adversary placing themself within the communication channel between the two components.</xhtml:p>

## Extended description
Whenever one component attempts to communicate with the other (data flow, authentication challenges, etc.), the data first flows through the adversary, who has the opportunity to observe or alter it, before being passed on to the intended recipient as if it was never observed. This interposition is transparent leaving the two compromised components unaware of the potential corruption or leakage of their communications. The potential for these attacks yields an implicit lack of trust in communication or identify between two components. These attacks differ from Sniffing Attacks (CAPEC-157) since these attacks often modify the communications prior to delivering it to the intended recipient.

## Prerequisites
- There are two components communicating with each other.
- An attacker is able to identify the nature and mechanism of communication between the two target components.
- An attacker can eavesdrop on the communication between the target components.
- Strong mutual authentication is not used between the two target components yielding opportunity for attacker interposition.
- The communication occurs in clear (not encrypted) or with insufficient and spoofable encryption.

## Skills required
- **Medium**: This attack can get sophisticated since the attack may use cryptography.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Determine Communication Mechanism: The adversary determines the nature and mechanism of communication between two components, looking for opportunities to exploit. Techniques Perform a sniffing attack and observe communication to determine a communication protocol. Look for application documentation that might describe a communication mechanism used by a target. Experiment Position In Between Targets: The adversary inserts themself into the communication channel initially acting as a routing proxy between the two targeted components. Techniques Install spyware on a client that will intercept outgoing packets and route them to their destination as well as route incoming packets back to the client. Exploit a weakness in an encrypted communication mechanism to gain access to traffic. Look for outdated mechanisms such as SSL. Exploit Use Intercepted Data Maliciously: The adversary observes, filters, or alters passed data of its choosing to gain access to sensitive information or to manipulate the actions of the two target components for their own purposes. Techniques Prevent some messages from reaching their destination, causing a denial of service.

## Mitigations
- Ensure Public Keys are signed by a Certificate Authority
- Encrypt communications using cryptography (e.g., SSL/TLS)
- Use Strong mutual authentication to always fully authenticate both ends of any communications channel.
- Exchange public keys using a secure channel

## Related weaknesses (CWE)
- [CWE-300](https://cwe.mitre.org/data/definitions/300.html)
- [CWE-290](https://cwe.mitre.org/data/definitions/290.html)
- [CWE-593](https://cwe.mitre.org/data/definitions/593.html)
- [CWE-287](https://cwe.mitre.org/data/definitions/287.html)
- [CWE-294](https://cwe.mitre.org/data/definitions/294.html)

## Related ATT&CK techniques
- T1557

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/94.html

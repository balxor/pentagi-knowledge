---
capec_id: CAPEC-65
name: Sniff Application Code
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: [CWE-319, CWE-311, CWE-318, CWE-693]
related_attack: [T1040]
url: https://capec.mitre.org/data/definitions/65.html
tags: [mitre-capec, attack-pattern, CAPEC-65]
---

# CAPEC-65 - Sniff Application Code

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-65](https://capec.mitre.org/data/definitions/65.html)

## Description
An adversary passively sniffs network communications and captures application code bound for an authorized client. Once obtained, they can use it as-is, or through reverse-engineering glean sensitive information or exploit the trust relationship between the client and server. Such code may belong to a dynamic update to the client, a patch being applied to a client component or any such interaction where the client is authorized to communicate with the server.

## Prerequisites
- The attacker must have the ability to place themself in the communication path between the client and server.
- The targeted application must receive some application code from the server; for example, dynamic updates, patches, applets or scripts.
- The attacker must be able to employ a sniffer on the network without being detected.

## Skills required
- **Medium**: The attacker needs to setup a sniffer for a sufficient period of time so as to capture meaningful quantities of code. The presence of the sniffer should not be detected on the network. Also if the attacker plans to employ an adversary-in-the-middle attack (CAPEC-94), the client or server must not realize this. Finally, the attacker needs to regenerate source code from binary code if the need be.

## Resources required
- The Attacker needs the ability to capture communications between the client being updated and the server providing the update. In the case that encryption obscures client/server communication the attacker will either need to lift key material from the client.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Read Data, Gain Privileges

## Execution flow
Execution Flow Explore Set up a sniffer: The adversary sets up a sniffer in the path between the server and the client and watches the traffic. Techniques The adversary sets up a sniffer in the path between the server and the client. Exploit [Capturing Application Code Bound During Patching]adversary knows that the computer/OS/application can request new applications to install, or it periodically checks for an available update. The adversary loads the sniffer set up during Explore phase, and extracts the application code from subsequent communication. The adversary then proceeds to reverse engineer the captured code. Techniques adversary loads the sniffer to capture the application code bound during a dynamic update. The adversary proceeds to reverse engineer the captured code.

## Mitigations
- Design: Encrypt all communication between the client and server.
- Implementation: Use SSL, SSH, SCP.
- Operation: Use "ifconfig/ipconfig" or other tools to detect the sniffer installed in the network.

## Related weaknesses (CWE)
- [CWE-319](https://cwe.mitre.org/data/definitions/319.html)
- [CWE-311](https://cwe.mitre.org/data/definitions/311.html)
- [CWE-318](https://cwe.mitre.org/data/definitions/318.html)
- [CWE-693](https://cwe.mitre.org/data/definitions/693.html)

## Related ATT&CK techniques
- T1040

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/65.html

---
capec_id: CAPEC-102
name: Session Sidejacking
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-294, CWE-522, CWE-523, CWE-319, CWE-614]
related_attack: []
url: https://capec.mitre.org/data/definitions/102.html
tags: [mitre-capec, attack-pattern, CAPEC-102]
---

# CAPEC-102 - Session Sidejacking

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-102](https://capec.mitre.org/data/definitions/102.html)

## Description
Session sidejacking takes advantage of an unencrypted communication channel between a victim and target system. The attacker sniffs traffic on a network looking for session tokens in unencrypted traffic. Once a session token is captured, the attacker performs malicious actions by using the stolen token with the targeted application to impersonate the victim. This attack is a specific method of session hijacking, which is exploiting a valid session token to gain unauthorized access to a target system or information. Other methods to perform a session hijacking are session fixation, cross-site scripting, or compromising a user or server machine and stealing the session token.

## Prerequisites
- An attacker and the victim are both using the same WiFi network.
- The victim has an active session with a target system.
- The victim is not using a secure channel to communicate with the target system (e.g. SSL, VPN, etc.)
- The victim initiated communication with a target system that requires transfer of the session token or the target application uses AJAX and thereby periodically "rings home" asynchronously using the session token

## Skills required
- **Low**: Easy to use tools exist to automate this attack.

## Resources required
- A packet sniffing tool, such as wireshark, can be used to capture session information.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Unreliable Execution
- **Confidentiality**: Gain Privileges, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Detect Unprotected Session Token Transfer: The attacker sniffs on the wireless network to detect unencrypted traffic that contains session tokens. Techniques The attacker uses a network sniffer tool like ferret or hamster to monitor the wireless traffic at a WiFi hotspot while examining it for evidence of transmittal of session tokens in unencrypted or recognizably encrypted form. An attacker applies their knowledge of the manner by which session tokens are generated and transmitted by various target systems to identify the session tokens. Experiment Capture session token: The attacker uses sniffing tools to capture a session token from traffic. Insert captured session token: The attacker attempts to insert a captured session token into communication with the targeted application to confirm viability for exploitation. Exploit Session Token Exploitation: The attacker leverages the captured session token to interact with the targeted application in a malicious fashion, impersonating the victim.

## Mitigations
- Make sure that HTTPS is used to communicate with the target system. Alternatively, use VPN if possible. It is important to ensure that all communication between the client and the server happens via an encrypted secure channel.
- Modify the session token with each transmission and protect it with cryptography. Add the idea of request sequencing that gives the server an ability to detect replay attacks.

## Related weaknesses (CWE)
- [CWE-294](https://cwe.mitre.org/data/definitions/294.html)
- [CWE-522](https://cwe.mitre.org/data/definitions/522.html)
- [CWE-523](https://cwe.mitre.org/data/definitions/523.html)
- [CWE-319](https://cwe.mitre.org/data/definitions/319.html)
- [CWE-614](https://cwe.mitre.org/data/definitions/614.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/102.html

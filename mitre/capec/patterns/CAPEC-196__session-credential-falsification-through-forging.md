---
capec_id: CAPEC-196
name: Session Credential Falsification through Forging
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: Medium
related_cwe: [CWE-384, CWE-664]
related_attack: [T1134.002, T1134.003, T1606]
url: https://capec.mitre.org/data/definitions/196.html
tags: [mitre-capec, attack-pattern, CAPEC-196]
---

# CAPEC-196 - Session Credential Falsification through Forging

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-196](https://capec.mitre.org/data/definitions/196.html)

## Description
An attacker creates a false but functional session credential in order to gain or usurp access to a service. Session credentials allow users to identify themselves to a service after an initial authentication without needing to resend the authentication information (usually a username and password) with every message. If an attacker is able to forge valid session credentials they may be able to bypass authentication or piggy-back off some other authenticated user's session. This attack differs from Reuse of Session IDs and Session Sidejacking attacks in that in the latter attacks an attacker uses a previous or existing credential without modification while, in a forging attack, the attacker must create their own credential, although it may be based on previously observed credentials.

## Prerequisites
- The targeted application must use session credentials to identify legitimate users. Session identifiers that remains unchanged when the privilege levels change. Predictable session identifiers.

## Skills required
- **Medium**: Forge the session credential and reply the request.

## Resources required
- Attackers may require tools to craft messages containing their forged credentials, and ability to send HTTP request to a web application.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Accountability**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges, Bypass Protection Mechanism
- **Confidentiality**: Read Data
- **Integrity**: Modify Data
- **Non-Repudiation**: Gain Privileges

## Execution flow
Execution Flow Explore Analyze and Understand Session IDs: The attacker finds that the targeted application use session credentials to identify legitimate users. Techniques An attacker makes many anonymous connections and records the session IDs. An attacker makes authorized connections and records the session tokens or credentials. Experiment Create Session IDs.: Attackers craft messages containing their forged credentials in GET, POST request, HTTP headers or cookies. Techniques The attacker manipulates the HTTP request message and adds their forged session IDs in to the requests or cookies. Exploit Abuse the Victim's Session Credentials: The attacker fixates falsified session ID to the victim when victim access the system. Once the victim has achieved a higher level of privilege, possibly by logging into the application, the attacker can now take over the session using the forged session identifier. Techniques The attacker loads the predefined or predicted session ID into their browser and browses to protected data or functionality. The attacker loads the predefined or predicted session ID into their software and utilizes functionality with the rights of the victim.

## Mitigations
- Implementation: Use session IDs that are difficult to guess or brute-force: One way for the attackers to obtain valid session IDs is by brute-forcing or guessing them. By choosing session identifiers that are sufficiently random, brute-forcing or guessing becomes very difficult.
- Implementation: Regenerate and destroy session identifiers when there is a change in the level of privilege: This ensures that even though a potential victim may have followed a link with a fixated identifier, a new one is issued when the level of privilege changes.

## Related weaknesses (CWE)
- [CWE-384](https://cwe.mitre.org/data/definitions/384.html)
- [CWE-664](https://cwe.mitre.org/data/definitions/664.html)

## Related ATT&CK techniques
- T1134.002
- T1134.003
- T1606

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/196.html

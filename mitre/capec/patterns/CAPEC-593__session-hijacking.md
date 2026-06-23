---
capec_id: CAPEC-593
name: Session Hijacking
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Very High
related_cwe: [CWE-287]
related_attack: [T1185, T1550.001, T1563]
url: https://capec.mitre.org/data/definitions/593.html
tags: [mitre-capec, attack-pattern, CAPEC-593]
---

# CAPEC-593 - Session Hijacking

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-593](https://capec.mitre.org/data/definitions/593.html)

## Description
This type of attack involves an adversary that exploits weaknesses in an application's use of sessions in performing authentication. The adversary is able to steal or manipulate an active session and use it to gain unathorized access to the application.

## Prerequisites
- An application that leverages sessions to perform authentication.

## Skills required
- **Low**: Exploiting a poorly protected identity token is a well understood attack with many helpful resources available.

## Resources required
- The adversary must have the ability to communicate with the application over the network.

## Consequences
- **Availability**: Gain Privileges (A successful attack can enable an adversary to gain unauthorized access to an application.)
- **Confidentiality**: Gain Privileges (A successful attack can enable an adversary to gain unauthorized access to an application.)
- **Integrity**: Gain Privileges (A successful attack can enable an adversary to gain unauthorized access to an application.)

## Execution flow
Execution Flow Explore Discover Existing Session Token: Through varrying means, an adversary will discover and store an existing session token for some other authenticated user session. Experiment Insert Found Session Token: The attacker attempts to insert a found session token into communication with the targeted application to confirm viability for exploitation. Exploit Session Token Exploitation: The attacker leverages the captured session token to interact with the targeted application in a malicious fashion, impersonating the victim.

## Mitigations
- Properly encrypt and sign identity tokens in transit, and use industry standard session key generation mechanisms that utilize high amount of entropy to generate the session key. Many standard web and application servers will perform this task on your behalf. Utilize a session timeout for all sessions. If the user does not explicitly logout, terminate their session after this period of inactivity. If the user logs back in then a new session key should be generated.

## Related weaknesses (CWE)
- [CWE-287](https://cwe.mitre.org/data/definitions/287.html)

## Related ATT&CK techniques
- T1185
- T1550.001
- T1563

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/593.html

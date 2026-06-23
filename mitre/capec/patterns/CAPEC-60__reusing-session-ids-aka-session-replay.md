---
capec_id: CAPEC-60
name: Reusing Session IDs (aka Session Replay)
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-294, CWE-290, CWE-346, CWE-384, CWE-488, CWE-539, CWE-200, CWE-285, CWE-664, CWE-732]
related_attack: [T1134.001, T1550.004]
url: https://capec.mitre.org/data/definitions/60.html
tags: [mitre-capec, attack-pattern, CAPEC-60]
---

# CAPEC-60 - Reusing Session IDs (aka Session Replay)

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-60](https://capec.mitre.org/data/definitions/60.html)

## Description
This attack targets the reuse of valid session ID to spoof the target system in order to gain privileges. The attacker tries to reuse a stolen session ID used previously during a transaction to perform spoofing and session hijacking. Another name for this type of attack is Session Replay.

## Prerequisites
- The target host uses session IDs to keep track of the users.
- Session IDs are used to control access to resources.
- The session IDs used by the target host are not well protected from session theft.

## Skills required
- **Low**: If an attacker can steal a valid session ID, they can then try to be authenticated with that stolen session ID.
- **Medium**: More sophisticated attack can be used to hijack a valid session from a user and spoof a legitimate user by reusing their valid session ID.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges

## Execution flow
Execution Flow Explore The attacker interacts with the target host and finds that session IDs are used to authenticate users. The attacker steals a session ID from a valid user. Exploit The attacker tries to use the stolen session ID to gain access to the system with the privileges of the session ID's original owner.

## Mitigations
- Always invalidate a session ID after the user logout.
- Setup a session time out for the session IDs.
- Protect the communication between the client and server. For instance it is best practice to use SSL to mitigate adversary in the middle attacks (CAPEC-94).
- Do not code send session ID with GET method, otherwise the session ID will be copied to the URL. In general avoid writing session IDs in the URLs. URLs can get logged in log files, which are vulnerable to an attacker.
- Encrypt the session data associated with the session ID.
- Use multifactor authentication.

## Related weaknesses (CWE)
- [CWE-294](https://cwe.mitre.org/data/definitions/294.html)
- [CWE-290](https://cwe.mitre.org/data/definitions/290.html)
- [CWE-346](https://cwe.mitre.org/data/definitions/346.html)
- [CWE-384](https://cwe.mitre.org/data/definitions/384.html)
- [CWE-488](https://cwe.mitre.org/data/definitions/488.html)
- [CWE-539](https://cwe.mitre.org/data/definitions/539.html)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)
- [CWE-285](https://cwe.mitre.org/data/definitions/285.html)
- [CWE-664](https://cwe.mitre.org/data/definitions/664.html)
- [CWE-732](https://cwe.mitre.org/data/definitions/732.html)

## Related ATT&CK techniques
- T1134.001
- T1550.004

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/60.html

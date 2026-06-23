---
capec_id: CAPEC-59
name: Session Credential Falsification through Prediction
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-290, CWE-330, CWE-331, CWE-346, CWE-488, CWE-539, CWE-200, CWE-6, CWE-285, CWE-384, CWE-693]
related_attack: []
url: https://capec.mitre.org/data/definitions/59.html
tags: [mitre-capec, attack-pattern, CAPEC-59]
---

# CAPEC-59 - Session Credential Falsification through Prediction

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-59](https://capec.mitre.org/data/definitions/59.html)

## Description
This attack targets predictable session ID in order to gain privileges. The attacker can predict the session ID used during a transaction to perform spoofing and session hijacking.

## Prerequisites
- The target host uses session IDs to keep track of the users.
- Session IDs are used to control access to resources.
- The session IDs used by the target host are predictable. For example, the session IDs are generated using predictable information (e.g., time).

## Skills required
- **Low**: There are tools to brute force session ID. Those tools require a low level of knowledge.
- **Medium**: Predicting Session ID may require more computation work which uses advanced analysis such as statistical analysis.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges

## Execution flow
Execution Flow Explore Find Session IDs: The attacker interacts with the target host and finds that session IDs are used to authenticate users. Techniques An attacker makes many anonymous connections and records the session IDs assigned. An attacker makes authorized connections and records the session tokens or credentials issued. Characterize IDs: The attacker studies the characteristics of the session ID (size, format, etc.). As a results the attacker finds that legitimate session IDs are predictable. Techniques Cryptanalysis. The attacker uses cryptanalysis to determine if the session IDs contain any cryptographic protections. Pattern tests. The attacker looks for patterns (odd/even, repetition, multiples, or other arithmetic relationships) between IDs Comparison against time. The attacker plots or compares the issued IDs to the time they were issued to check for correlation. Experiment Match issued IDs: The attacker brute forces different values of session ID and manages to predict a valid session ID. Techniques The attacker models the session ID algorithm enough to produce a compatible session IDs, or just one match. Exploit Use matched Session ID: The attacker uses the falsified session ID to access the target system. Techniques The attacker loads the session ID into their web browser and browses to restricted data or functionality. The attacker loads the session ID into their network communications and impersonates a legitimate user to gain access to data or functionality.

## Mitigations
- Use a strong source of randomness to generate a session ID.
- Use adequate length session IDs
- Do not use information available to the user in order to generate session ID (e.g., time).
- Ideas for creating random numbers are offered by Eastlake [RFC1750]
- Encrypt the session ID if you expose it to the user. For instance session ID can be stored in a cookie in encrypted format.

## Related weaknesses (CWE)
- [CWE-290](https://cwe.mitre.org/data/definitions/290.html)
- [CWE-330](https://cwe.mitre.org/data/definitions/330.html)
- [CWE-331](https://cwe.mitre.org/data/definitions/331.html)
- [CWE-346](https://cwe.mitre.org/data/definitions/346.html)
- [CWE-488](https://cwe.mitre.org/data/definitions/488.html)
- [CWE-539](https://cwe.mitre.org/data/definitions/539.html)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)
- [CWE-6](https://cwe.mitre.org/data/definitions/6.html)
- [CWE-285](https://cwe.mitre.org/data/definitions/285.html)
- [CWE-384](https://cwe.mitre.org/data/definitions/384.html)
- [CWE-693](https://cwe.mitre.org/data/definitions/693.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/59.html

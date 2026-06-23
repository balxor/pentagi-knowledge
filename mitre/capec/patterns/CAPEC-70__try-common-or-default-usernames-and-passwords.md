---
capec_id: CAPEC-70
name: Try Common or Default Usernames and Passwords
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-521, CWE-262, CWE-263, CWE-798, CWE-654, CWE-308, CWE-309]
related_attack: [T1078.001]
url: https://capec.mitre.org/data/definitions/70.html
tags: [mitre-capec, attack-pattern, CAPEC-70]
---

# CAPEC-70 - Try Common or Default Usernames and Passwords

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-70](https://capec.mitre.org/data/definitions/70.html)

## Description
An adversary may try certain common or default usernames and passwords to gain access into the system and perform unauthorized actions. An adversary may try an intelligent brute force using empty passwords, known vendor default credentials, as well as a dictionary of common usernames and passwords. Many vendor products come preconfigured with default (and thus well-known) usernames and passwords that should be deleted prior to usage in a production environment. It is a common mistake to forget to remove these default login credentials. Another problem is that users would pick very simple (common) passwords (e.g. "secret" or "password") that make it easier for the attacker to gain access to the system compared to using a brute force attack or even a dictionary attack using a full dictionary.

## Prerequisites
- The system uses one factor password based authentication.The adversary has the means to interact with the system.

## Skills required
- **Low**: An adversary just needs to gain access to common default usernames/passwords specific to the technologies used by the system. Additionally, a brute force attack leveraging common passwords can be easily realized if the user name is known.

## Resources required
- Technology or vendor specific list of default usernames and passwords.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges

## Mitigations
- Delete all default account credentials that may be put in by the product vendor.
- Implement a password throttling mechanism. This mechanism should take into account both the IP address and the log in name of the user.
- Put together a strong password policy and make sure that all user created passwords comply with it. Alternatively automatically generate strong passwords for users.
- Passwords need to be recycled to prevent aging, that is every once in a while a new password must be chosen.

## Related weaknesses (CWE)
- [CWE-521](https://cwe.mitre.org/data/definitions/521.html)
- [CWE-262](https://cwe.mitre.org/data/definitions/262.html)
- [CWE-263](https://cwe.mitre.org/data/definitions/263.html)
- [CWE-798](https://cwe.mitre.org/data/definitions/798.html)
- [CWE-654](https://cwe.mitre.org/data/definitions/654.html)
- [CWE-308](https://cwe.mitre.org/data/definitions/308.html)
- [CWE-309](https://cwe.mitre.org/data/definitions/309.html)

## Related ATT&CK techniques
- T1078.001

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/70.html

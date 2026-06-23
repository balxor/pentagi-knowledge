---
cwe_id: CWE-309
name: Use of Password System for Primary Authentication
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-16, CAPEC-49, CAPEC-509, CAPEC-55, CAPEC-555, CAPEC-560, CAPEC-561, CAPEC-565, CAPEC-600, CAPEC-652, CAPEC-653, CAPEC-70]
url: https://cwe.mitre.org/data/definitions/309.html
tags: [mitre-cwe, weakness, CWE-309]
---

# CWE-309 - Use of Password System for Primary Authentication

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-309](https://cwe.mitre.org/data/definitions/309.html)

## Description
The use of password systems as the primary means of authentication may be subject to several flaws or shortcomings, each reducing the effectiveness of the mechanism.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism, Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: In order to protect password systems from compromise, the following should be noted: Passwords should be stored safely to prevent insider attack and to ensure that -- if a system is compromised -- the passwords are not retrievable. Due to password reuse, this information may be useful in the compromise of other systems these users work with. In order to protect these passwords, they should be stored encrypted, in a non-reversible state, such that the original text password cannot be extracted from the stored value. Password aging should be strictly enforced to ensure that passwords do not remain unchanged for long periods of time. The longer a password remains in use, the higher the probability that it has been compromised. For this reason, passwords should require refreshing periodically, and users should be informed of the risk of passwords which remain in use for too long. Password strength should be enforced intelligently. Rather than restrict passwords to specific content, or specific length, users should be encouraged to use upper and lower case letters, numbers, and symbols in their passwords. The system should also ensure that no passwords are derived from dictionary words.
- **Architecture and Design**: Use a zero-knowledge password protocol, such as SRP.
- **Architecture and Design**: Ensure that passwords are stored safely and are not reversible.
- **Architecture and Design**: Implement password aging functionality that requires passwords be changed after a certain point.
- **Architecture and Design**: Use a mechanism for determining the strength of a password and notify the user of weak password use.
- **Architecture and Design**: Inform the user of why password protections are in place, how they work to protect data integrity, and why it is important to heed their warnings.

## Related attack patterns (CAPEC)
- [CAPEC-16](https://capec.mitre.org/data/definitions/16.html)
- [CAPEC-49](https://capec.mitre.org/data/definitions/49.html)
- [CAPEC-509](https://capec.mitre.org/data/definitions/509.html)
- [CAPEC-55](https://capec.mitre.org/data/definitions/55.html)
- [CAPEC-555](https://capec.mitre.org/data/definitions/555.html)
- [CAPEC-560](https://capec.mitre.org/data/definitions/560.html)
- [CAPEC-561](https://capec.mitre.org/data/definitions/561.html)
- [CAPEC-565](https://capec.mitre.org/data/definitions/565.html)
- [CAPEC-600](https://capec.mitre.org/data/definitions/600.html)
- [CAPEC-652](https://capec.mitre.org/data/definitions/652.html)
- [CAPEC-653](https://capec.mitre.org/data/definitions/653.html)
- [CAPEC-70](https://capec.mitre.org/data/definitions/70.html)

## Related weaknesses
- CWE-1390 (ChildOf)
- CWE-654 (ChildOf)
- CWE-308 (PeerOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/309.html

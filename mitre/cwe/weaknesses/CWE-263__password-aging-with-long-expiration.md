---
cwe_id: CWE-263
name: Password Aging with Long Expiration
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-16, CAPEC-49, CAPEC-509, CAPEC-55, CAPEC-555, CAPEC-560, CAPEC-561, CAPEC-565, CAPEC-600, CAPEC-652, CAPEC-653, CAPEC-70]
url: https://cwe.mitre.org/data/definitions/263.html
tags: [mitre-cwe, weakness, CWE-263]
---

# CWE-263 - Password Aging with Long Expiration

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-263](https://cwe.mitre.org/data/definitions/263.html)

## Description
The product supports password aging, but the expiration period is too long.

## Extended description
Password aging (or password rotation) is a policy that forces users to change their passwords after a defined time period passes, such as every 30 or 90 days. A long expiration provides more time for attackers to conduct password cracking before users are forced to change to a new password. Note that while password aging was once considered an important security feature, it has since fallen out of favor by many, because it is not as effective against modern threats compared to other mechanisms such as slow hashes. In addition, forcing frequent changes can unintentionally encourage users to select less-secure passwords. However, password aging is still in use due to factors such as compliance requirements, e.g., Payment Card Industry Data Security Standard (PCI DSS).

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Implementation**: Previously, "password expiration" was widely advocated as a defense-in-depth approach to minimize the risk of weak passwords, and it has become a common practice. Password expiration requires a password to be changed within a fixed time window (such as every 90 days). However, this approach has significant limitations in the current threat landscape, and its utility has been reduced in light of the adoption of related protection mechanisms (such as password complexity and computational effort), along with the recognition that regular password changes often caused users to generate more predictable passwords. As a result, this is now a Discouraged Common Practice [REF-1488] [REF-1489], especially as the sole factor in protecting passwords. It is still strongly encouraged to force password changes in case of evidence of compromise, but this is not the same as a forced "expiration" on an arbitrary time frame.
- **Architecture and Design**: Ensure that password aging is limited so that there is a defined maximum age for passwords. Note that if the expiration window is too short, it can cause users to generate poor or predictable passwords.
- **Architecture and Design**: Ensure that the user is notified several times leading up to the password expiration.
- **Architecture and Design**: Create mechanisms to prevent users from reusing passwords or creating similar passwords.
- **Implementation**: Developers might disable clipboard paste operations into password fields as a way to discourage users from pasting a password into a clipboard. However, this might encourage users to choose less-secure passwords that are easier to type, and it can reduce the usability of password managers [REF-1294].

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

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/263.html

---
cwe_id: CWE-262
name: Not Using Password Aging
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-16, CAPEC-49, CAPEC-509, CAPEC-55, CAPEC-555, CAPEC-560, CAPEC-561, CAPEC-565, CAPEC-600, CAPEC-652, CAPEC-653, CAPEC-70]
url: https://cwe.mitre.org/data/definitions/262.html
tags: [mitre-cwe, weakness, CWE-262]
---

# CWE-262 - Not Using Password Aging

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-262](https://cwe.mitre.org/data/definitions/262.html)

## Description
The product does not have a mechanism in place for managing password aging.

## Extended description
Password aging (or password rotation) is a policy that forces users to change their passwords after a defined time period passes, such as every 30 or 90 days. Without mechanisms such as aging, users might not change their passwords in a timely manner. Note that while password aging was once considered an important security feature, it has since fallen out of favor by many, because it is not as effective against modern threats compared to other mechanisms such as slow hashes. In addition, forcing frequent changes can unintentionally encourage users to select less-secure passwords. However, password aging is still in use due to factors such as compliance requirements, e.g., Payment Card Industry Data Security Standard (PCI DSS).

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: As part of a product's design, require users to change their passwords regularly and avoid reusing previous passwords.
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
- CWE-309 (PeerOf)
- CWE-324 (PeerOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/262.html

---
cwe_id: CWE-308
name: Use of Single-factor Authentication
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-16, CAPEC-49, CAPEC-509, CAPEC-55, CAPEC-555, CAPEC-560, CAPEC-561, CAPEC-565, CAPEC-600, CAPEC-644, CAPEC-645, CAPEC-652, CAPEC-653, CAPEC-70]
url: https://cwe.mitre.org/data/definitions/308.html
tags: [mitre-cwe, weakness, CWE-308]
---

# CWE-308 - Use of Single-factor Authentication

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-308](https://cwe.mitre.org/data/definitions/308.html)

## Description
The product uses an authentication algorithm that uses a single factor (e.g., a password) in a security context that should require more than one factor.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: Use multiple independent authentication schemes, which ensures that -- if one of the methods is compromised -- the system itself is still likely safe from compromise. For this reason, if multiple schemes are possible, they should be implemented and required -- especially if they are easy to use.

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
- [CAPEC-644](https://capec.mitre.org/data/definitions/644.html)
- [CAPEC-645](https://capec.mitre.org/data/definitions/645.html)
- [CAPEC-652](https://capec.mitre.org/data/definitions/652.html)
- [CAPEC-653](https://capec.mitre.org/data/definitions/653.html)
- [CAPEC-70](https://capec.mitre.org/data/definitions/70.html)

## Related weaknesses
- CWE-1390 (ChildOf)
- CWE-654 (ChildOf)
- CWE-309 (PeerOf)

## Observed examples (CVE)
- **CVE-2022-35248**: Chat application skips validation when Central Authentication Service (CAS) is enabled, effectively removing the second factor from two-factor authentication

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/308.html
